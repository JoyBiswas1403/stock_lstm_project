<!-- HEADER -->
<p align="center">
  <h1 style="font-weight:900; font-size:3rem;">🚀 Stock Trend Predictor & Forecast Dashboard</h1>
  <p><em>Powered by Bidirectional LSTM + Financial Technical Indicators + Interactive Streamlit Charts</em></p>
  
  <p>
    <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/></a>
    <a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-D43F3A?style=for-the-badge&logo=streamlit"/></a>
    <a href="https://www.tensorflow.org/"><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-LSTM-orange?style=for-the-badge&logo=tensorflow"/></a>
    <img alt="Status" src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
    <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
  </p>
</p>

---

<!-- OVERVIEW -->
<section style="background:#f0f4ff; padding: 20px; border-radius: 15px;">
<h2 style="color:#3b49df;">🌟 Project Overview</h2>
<p style="font-size: 1.05rem; color: #333;">
This project fuses cutting-edge <b>Bidirectional LSTM</b> deep learning architecture with financial technical indicators — MA20, RSI, MACD, Bollinger Bands — to build an intuitive <b>interactive Streamlit dashboard</b> for predicting stock price trends.
<br>
Users dynamically explore historical and forecasted market data via fluid charts, KPI cards, and download CSV reports — perfect for analysts, traders, and data enthusiasts.
</p>
</section>

---

<!-- FEATURES -->
<h2 style="color:#3b49df;">🔥 Key Features</h2>
<ul style="line-height:1.6; font-size:1.05rem;">
  <li>🔍 Real-time stock data fetching from <code>Yahoo Finance</code> with detailed date range control</li>
  <li>📈 Calculation of advanced technical indicators with intuitive visual overlays</li>
  <li>🤖 Customizable Bidirectional LSTM for time-series trend forecasting</li>
  <li>🖥️ Dynamic Streamlit UI: tabs for data, training, and forecast with sliders and dropdown menus</li>
  <li>📊 Interactive Plotly charts with zoom, hover, and pan</li>
  <li>💾 Export forecast data in CSV format for seamless post-analysis</li>
</ul>

---

<!-- TECH STACK -->
<h2 style="color:#3b49df;">🛠️ Tech Stack</h2>
<p>
  <b>Languages & Libraries: </b> <code>Python 3.9+</code>, <code>Pandas</code>, <code>NumPy</code>, <code>TA-Lib / ta</code>, <code>TensorFlow / Keras</code>, <code>Scikit-learn</code>, <code>Plotly</code>, <code>Streamlit</code>.
</p>

---

<!-- INSTALLATION -->
<section style="background:#f0f4ff; padding: 20px; border-radius: 15px;">
<h2 style="color:#3b49df;">🚀 Installation & Quick Setup</h2>

<pre style="background:#2d2d2d; color:#f8f8f2; padding:20px; border-radius:10px; overflow-x:auto;">
$ git clone https://github.com/JoyBiswas1403/stock_lstm_project.git
$ cd stock_lstm_project
$ python -m venv venv
$ source venv/bin/activate         <i style="color:#999;"># macOS/Linux</i>
$ venv\Scripts\activate.bat        <i style="color:#999;"># Windows</i>
$ pip install -r requirements.txt
$ streamlit run app.py
</pre>
</section>

---

<!-- USAGE TIPS -->
<h2 style="color:#3b49df;">🧭 Usage Tips</h2>
<ul style="line-height:1.6; font-size:1.05rem;">
  <li>🎯 Select your stock ticker and date range with sidebar controls</li>
  <li>⚙️ Fine-tune LSTM parameters like lookback days, epochs, batch size for optimized results</li>
  <li>📊 Train the model and interact with visually rich charts</li>
  <li>📥 Download your forecast results via CSV for further reporting</li>
</ul>

---

<!-- DEMO -->
<h2 style="color:#3b49df;">🎬 Visual Demo & Snapshot</h2>

<p align="center">
  <img src="screenshots/dashboard_screenshot.png" alt="Stock Trend Dashboard Screenshot" width="720" style="border-radius: 15px; box-shadow: 0 4px 15px rgba(59,73,223,0.3);"/>
</p>

---

<!-- FILES -->
<h2 style="color:#3b49df;">📂 Project Files</h2>

| File/Folder      | Description                              |
|------------------|------------------------------------------|
| `app.py`         | Streamlit dashboard source code          |
| `requirements.txt`| Python dependencies list                  |
| `artifacts/`     | Trained model files and weights           |
| `screenshots/`   | Dashboard images and visual assets        |
| `README.md`      | Documentation & project overview          |

---

<!-- CONTRIBUTING -->
<h2 style="color:#3b49df;">🤝 Contributing & Support</h2>

<p>Contributions to enhance features, add indicators, or improve UX are highly welcome!  
Raise an issue or submit a pull request to collaborate.  
Your feedback drives this project forward.</p>

---

<!-- CONTACT -->
<h2 style="color:#3b49df;">📬 Contact</h2>

<p>
  <b>Joy Biswas</b>  
  <br>Email: <a href="mailto:bjoy1403@gmail.com">bjoy1403@gmail.com</a>
  <br>GitHub: <a href="https://github.com/JoyBiswas1403">https://github.com/JoyBiswas1403</a>
</p>

---

<p align="center" style="font-style:italic; color:#555;">
  Crafted with ❤️ &amp; Streamlit magic — dive into financial AI 🔮  
</p>
