import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import ta
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.callbacks import EarlyStopping
import plotly.graph_objects as go
import os

# ----- Custom Theme and Logo -----
st.set_page_config(page_title="Stock Trend Predictor & Forecast Dashboard", layout="wide", page_icon="🚀")
st.markdown(
    """
    <style>
    .stButton>button {background-color: #1565c0; color: white; font-size: 1.05rem; padding:0.5rem 2rem; border-radius:8px;}
    .stMetric {background: #f7f9fc !important; border-radius:8px; padding:12px;}
    h1 {font-family: "Roboto", sans-serif;}
    .block-container {padding-top: 1.5rem;}
    </style>
    """, unsafe_allow_html=True
)
st.markdown("<h1 style='font-size:2rem;'>🚀 Stock Trend Predictor & Forecast Dashboard</h1>", unsafe_allow_html=True)

# ----- Sidebar Controls -----
st.sidebar.header("Configuration")
ticker = st.sidebar.selectbox("Ticker", ["AAPL", "MSFT", "GOOG", "TSLA"])
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-01-01"))
st.sidebar.markdown("---")
lookback = st.sidebar.slider("Lookback Days", 30, 180, 60)
epochs = st.sidebar.slider("Epochs", 5, 100, 30)
batch_size = st.sidebar.slider("Batch Size", 16, 128, 32, step=8)
forecast_days = st.sidebar.slider("Forecast Days", 1, 30, 5)
dropout = st.sidebar.slider("Dropout Rate", 0.0, 0.5, 0.2, step=0.05)
units1 = st.sidebar.slider("LSTM Units 1", 32, 128, 64, step=8)
units2 = st.sidebar.slider("LSTM Units 2", 16, 64, 32, step=8)

# ----- Helper Functions -----
@st.cache_data(show_spinner=False)
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
    if df.empty:
        return df
    cols = ['Open','High','Low','Close','Adj Close','Volume']
    available_cols = [c for c in cols if c in df.columns]
    df = df[available_cols].copy()
    if 'Close' in df.columns:
        close_series = df['Close'].squeeze()
        df['MA20'] = close_series.rolling(20, min_periods=1).mean()
        df['MA50'] = close_series.rolling(50, min_periods=1).mean()
        df['RSI14'] = ta.momentum.RSIIndicator(close=close_series, window=14, fillna=True).rsi()
        df['EMA12'] = ta.trend.EMAIndicator(close=close_series, window=12, fillna=True).ema_indicator()
        df['EMA26'] = ta.trend.EMAIndicator(close=close_series, window=26, fillna=True).ema_indicator()
        df['MACD'] = df['EMA12'] - df['EMA26']
        bb = ta.volatility.BollingerBands(close=close_series, window=20, window_dev=2, fillna=True)
        df['BB_High'] = bb.bollinger_hband()
        df['BB_Low'] = bb.bollinger_lband()
        df.dropna(inplace=True)
    return df

def create_sequences(data, lookback=60):
    X, y = [], []
    for i in range(lookback, len(data)):
        X.append(data[i-lookback:i])
        y.append(data[i])
    return np.array(X), np.array(y)

def build_lstm(input_shape, units1=64, units2=32, dropout=0.2):
    model = Sequential()
    model.add(Bidirectional(LSTM(units1, return_sequences=True), input_shape=input_shape))
    model.add(Dropout(dropout))
    model.add(Bidirectional(LSTM(units2)))
    model.add(Dropout(dropout))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def forecast(model, data, lookback, days, scaler):
    forecasted = []
    input_seq = data[-lookback:].reshape(1, lookback, 1)
    for _ in range(days):
        pred = model.predict(input_seq, verbose=0)
        forecasted.append(pred[0,0])
        input_seq = np.concatenate((input_seq[:,1:,:], pred.reshape(1,1,1)), axis=1)
    return scaler.inverse_transform(np.array(forecasted).reshape(-1,1))

def safe_float(val, numfmt):
    try:
        val_float = float(val)
        if np.isnan(val_float):
            return "N/A"
        return numfmt.format(val_float)
    except Exception:
        return "N/A"

# ----- Data Load -----
df = load_data(ticker, start_date, end_date)
if df.empty:
    st.warning("No data found. Check ticker or date range.")
    st.stop()

# ----- Tabs Layout -----
tab1, tab2, tab3 = st.tabs(["Data & Indicators", "Model Training", "Forecast"])

# ----- Data & Indicators Tab -----
with tab1:
    st.subheader("Data & Indicators")
    # Debug: show last rows for troubleshooting
    st.write("Latest data rows for debugging:")
    st.dataframe(df.tail(3))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current Price", safe_float(df['Close'].iloc[-1], "{:,.2f}"))
    col2.metric("MA20", safe_float(df['MA20'].iloc[-1], "{:,.2f}"))
    col3.metric("RSI14", safe_float(df['RSI14'].iloc[-1], "{:,.1f}"))
    col4.metric("MACD", safe_float(df['MACD'].iloc[-1], "{:,.2f}"))

    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Price"
    )])
    fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], line=dict(color='blue', width=2), name="MA20"))
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_High'], line=dict(color='green', width=1, dash='dash'), name="BB High"))
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_Low'], line=dict(color='red', width=1, dash='dash'), name="BB Low"))
    fig.update_layout(
        height=350,
        margin=dict(l=0, r=0, t=26, b=0),
        legend=dict(orientation="h"),
        xaxis_title=None,
        yaxis_title="Price"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    colA, colB = st.columns(2)
    with colA:
        st.subheader("RSI14")
        st.line_chart(df['RSI14'])
    with colB:
        st.subheader("MACD")
        st.line_chart(df['MACD'])

# ----- Model Training Tab -----
with tab2:
    st.subheader("Model Training")
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_close = scaler.fit_transform(df['Close'].values.reshape(-1,1))
    X, y = create_sequences(scaled_close, lookback)
    if st.button("Train LSTM Model"):
        with st.spinner('Training LSTM model...'):
            model = build_lstm(input_shape=(X.shape[1], X.shape[2]), units1=units1, units2=units2, dropout=dropout)
            es = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
            model.fit(X, y, epochs=epochs, batch_size=batch_size, callbacks=[es], verbose=1)
            os.makedirs("artifacts", exist_ok=True)
            model.save(f"artifacts/model_{ticker}.keras")
        st.success("✅ Model trained and saved successfully!")

# ----- Forecast Tab -----
with tab3:
    st.subheader("Forecast")
    if os.path.exists(f"artifacts/model_{ticker}.keras"):
        model = load_model(f"artifacts/model_{ticker}.keras")
        forecasted = forecast(model, scaled_close, lookback, forecast_days, scaler)
        last_date = pd.to_datetime(df.index[-1])
        forecast_dates = pd.bdate_range(last_date, periods=forecast_days+1, freq='B')[1:]
        forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecast": forecasted.flatten()})

        hist_df = df[['Close']].copy().rename(columns={'Close': 'Price'})
        forecast_df = forecast_df.rename(columns={'Forecast': 'Price'}).set_index('Date')
        combined = pd.concat([hist_df, forecast_df])

        st.write("Historical and Forecasted Stock Price")
        fig_forecast = go.Figure()
        fig_forecast.add_trace(go.Scatter(
            x=hist_df.index,
            y=hist_df['Price'],
            mode='lines',
            name='Historical',
            line=dict(color='blue')
        ))
        fig_forecast.add_trace(go.Scatter(
            x=forecast_df.index,
            y=forecast_df['Price'],
            mode='lines',
            name='Forecasted Stock',
            line=dict(color='red')
        ))
        fig_forecast.update_layout(
            height=250,
            margin=dict(l=14, r=14, t=24, b=0),
            xaxis_title="Date",
            yaxis_title="Stock Price"
        )
        st.plotly_chart(fig_forecast, use_container_width=True)
        st.dataframe(forecast_df.reset_index())
        st.download_button(
            "Download CSV",
            forecast_df.reset_index().to_csv(index=False),
            file_name="forecast.csv",
            use_container_width=True
        )
    else:
        st.info("Train the model first in 'Model Training' tab.")
