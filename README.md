<p align="center">

# 🚀 Stock Trend Predictor & Forecast Dashboard  
## Powered by Bidirectional LSTM + Financial Technical Indicators + Interactive Streamlit Charts

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/></a>
<a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-D43F3A?style=for-the-badge&logo=streamlit"/></a>
<a href="https://www.tensorflow.org/"><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-LSTM-orange?style=for-the-badge&logo=tensorflow"/></a>
<img alt="Status" src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

</p>

---

<section style="background:#eef4ff; padding:20px; border-radius:12px;">
<h2 style="color:#3b49df;">🌟 Project Overview</h2>
<p style="font-size:1.1rem; color:#222;">
This project fuses cutting-edge <b>Bidirectional LSTM</b> deep learning architecture with financial technical indicators — MA20, RSI, MACD, Bollinger Bands — to build an intuitive <b>interactive Streamlit dashboard</b> for predicting stock price trends.<br>
Users dynamically explore historical and forecasted market data via fluid charts, KPI cards, and download CSV reports — perfect for analysts, traders, and data enthusiasts.
</p>
</section>

---

<h2 style="color:#3b49df;">🔥 Key Features</h2>
<ul style="font-size:1.05rem; line-height:1.7; color:#333;">
  <li>🔍 Real-time stock data fetching from <code>Yahoo Finance</code> with detailed date range selection</li>
  <li>📈 Advanced technical indicator calculation and overlays</li>
  <li>🤖 Customizable Bidirectional LSTM models for time-series forecasting</li>
  <li>🖥️ Dynamic multi-tab Streamlit UI with sliders, dropdowns, and real-time updates</li>
  <li>📊 Interactive Plotly charts with zoom, pan, and hover info</li>
  <li>💾 Exportable forecast data as CSV</li>
</ul>

---

<h2 style="color:#3b49df;">🛠️ Tech Stack</h2>
<p>
  <b>Languages & Libraries:</b> Python 3.9+, Pandas, NumPy, TA-Lib/ta, TensorFlow/Keras, Scikit-learn, Plotly, Streamlit.
</p>

---

<section style="background:#eef4ff; padding:20px; border-radius:12px;">
<h2 style="color:#3b49df;">🚀 Installation & Quick Setup</h2>

<pre style="background:#2d2d2d; color:#f8f8f2; padding:15px 20px; border-radius:10px; overflow-x:auto;">
# Clone the repo
git clone https://github.com/JoyBiswas1403/stock_lstm_project.git
cd stock_lstm_project

# (Optional) Create virtualenv and activate
python -m venv venv
# macOS/Linux
source venv/bin/activate  
# Windows
venv\Scripts\activate.bat  

# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run app.py
</pre>
</section>

---

<h2 style="color:#3b49df;">🧭 Usage Tips</h2>
<ul style="line-height:1.7; font-size:1.05rem; color:#333;">
  <li>🎯 Select stock ticker and date range using sidebar controls</li>
  <li>⚙️ Fine-tune model parameters like lookback window, epochs, and batch size</li>
  <li>🏋️ Train the LSTM model to fit the stock data</li>
  <li>📉 Visualize technical indicators, forecasts, and actual prices interactively</li>
  <li>📥 Export forecast data as CSV for external use</li>
</ul>

---

<h2 style="color:#3b49df;">🎬 Visual Demo & Dashboard Snapshot</h2>

<p align="center">
  <img src="screenshots/dashboard_screenshot.png" alt="Dashboard Screenshot" width="720" style="border-radius:15px; box-shadow:0 6px 25px rgb(59 73 223 / 0.3);"/>
</p>

---

<h2 style="color:#3b49df;">📂 Project Files & Structure</h2>

| File / Folder         | Description                         |
|----------------------|-----------------------------------|
| `app.py`             | Streamlit dashboard application   |
| `requirements.txt`   | Python dependencies                |
| `artifacts/`         | Saved trained model files          |
| `screenshots/`       | Dashboard visuals and assets       |
| `README.md`          | This documentation file            |

---

<details>
<summary><b style="font-size:1.1rem; cursor:pointer;">🤝 Contributing & Community</b></summary>

<p style="padding:10px; font-size:1.05rem;">
Thanks for your interest! Contributions, issues, suggestions, and feature requests are warmly welcome.<br>
- Fork the repo and create a pull request<br>
- Open an issue to report bugs or request features<br>
- Join discussions and help improve the project
</p>
</details>

---

<h2 style="color:#3b49df;">📬 Contact & Socials</h2>

<p>
  <b>Joy Biswas</b><br>
  Email: <a href="mailto:bjoy1403@gmail.com">bjoy1403@gmail.com</a><br>
  GitHub: <a href="https://github.com/JoyBiswas1403">JoyBiswas1403</a>
</p>

---

<p align="center" style="font-style:italic; color:#555;">
  Crafted with ❤️ and Streamlit magic — dive into financial AI and visualization!  
</p>
