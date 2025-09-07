<p align="center">

# 🚀 Stock Trend Predictor & Forecast Dashboard  
## Powered by Bidirectional LSTM + Financial Technical Indicators + Interactive Streamlit Charts

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/></a>
<a href="https://streamlit.io/"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-D43F3A?style=for-the-badge&logo=streamlit"/></a>
<a href="https://www.tensorflow.org/"><img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-LSTM-orange?style=for-the-badge&logo=tensorflow"/></a>
<img alt="Status" src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>

</p>

---

<section style="background:#eef4ff; padding:25px; border-radius:15px; box-shadow: 0 0 15px rgba(59,73,223,0.3);">
<h2 style="color:#3b49df; font-weight:700;">🌟 Project Overview</h2>
<p style="font-size:1.1rem; color:#222; line-height:1.6;">
This project fuses cutting-edge <b>Bidirectional LSTM</b> deep learning architecture with financial technical indicators — MA20, RSI, MACD, Bollinger Bands — to build an <b>interactive Streamlit dashboard</b> for predicting stock price trends.
<br><br>
Users dynamically explore historical and forecasted market data via fluid charts, KPI cards, and downloadable CSV reports — perfect for traders, analysts, and data enthusiasts.
</p>
</section>

---

<h2 style="color:#3b49df; font-weight:700;">🔥 Key Features</h2>
<ul style="font-size:1.05rem; line-height:1.8; color:#333; list-style-type:none; padding-left:0;">
  <li>✅ <b>Real-time stock data</b> fetching via Yahoo Finance API</li>
  <li>📈 Calculation and visualization of key financial indicators (MA20, RSI, MACD, Bollinger Bands)</li>
  <li>🤖 Train customizable Bidirectional LSTM deep learning model</li>
  <li>📊 Interactive Plotly-powered charts illustrating trends and forecasts</li>
  <li>💾 Exportable forecast results as CSV for post-analysis</li>
  <li>🖥️ Multi-tab, responsive Streamlit interface with intuitive controls</li>
</ul>

---

<h2 style="color:#3b49df; font-weight:700;">🛠️ Tech Stack</h2>
<table style="border-collapse: collapse; width: 100%; font-size: 1.1rem;">
  <thead><tr style="background:#3b49df; color: white;">
    <th style=" padding: 12px; border: 1px solid #ccc;">Technology</th><th style=" padding: 12px; border: 1px solid #ccc;">Purpose</th>
  </tr></thead>
  <tbody>
    <tr><td style="padding: 8px; border: 1px solid #ccc;">Python &amp; Pandas</td><td style="padding: 8px; border: 1px solid #ccc;">Data Manipulation</td></tr>
    <tr style="background:#f0f4ff;"><td style="padding: 8px; border: 1px solid #ccc;">NumPy</td><td style="padding: 8px; border: 1px solid #ccc;">Numerical Computations</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ccc;">TensorFlow/Keras</td><td style="padding: 8px; border: 1px solid #ccc;">Deep Learning Model Building</td></tr>
    <tr style="background:#f0f4ff;"><td style="padding: 8px; border: 1px solid #ccc;">ta/TA-Lib</td><td style="padding: 8px; border: 1px solid #ccc;">Technical Indicators Calculation</td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ccc;">Plotly</td><td style="padding: 8px; border: 1px solid #ccc;">Interactive Charting</td></tr>
    <tr style="background:#f0f4ff;"><td style="padding: 8px; border: 1px solid #ccc;">Streamlit</td><td style="padding: 8px; border: 1px solid #ccc;">Dashboard UI</td></tr>
  </tbody>
</table>

---

<section style="background:#eef4ff; padding:25px; border-radius:15px; box-shadow: 0 0 15px rgba(59,73,223,0.3); margin-top: 25px;">
<h2 style="color:#3b49df; font-weight:700;">🚀 Installation & Setup</h2>

<pre style="background:#2d2d2d; color:#f8f8f2; padding:20px; border-radius:12px; overflow-x:auto; font-size:1.1rem;">
# Clone the repo
git clone https://github.com/JoyBiswas1403/stock_lstm_project.git
cd stock_lstm_project

# (Optional) create and activate virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate  
# Windows
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit
streamlit run app.py
</pre>
</section>

---

<h2 style="color:#3b49df; font-weight:700;">🧭 Usage Tips</h2>
<ul style="font-size:1.1rem; line-height:1.8; color:#333;">
  <li>🎯 Select your stock ticker and date range on the sidebar</li>
  <li>⚙️ Adjust model parameters such as lookback days, epochs, batch size</li>
  <li>🏋️ Start model training and observe live updates of plots</li>
  <li>📉 Analyze predictions through interactive charts</li>
  <li>📥 Export forecast data as CSV for offline use</li>
</ul>

---

<h2 style="color:#3b49df; font-weight:700;">🎬 Visual Demo</h2>

<p align="center" style="margin-bottom:30px;">
  <img src="screenshots/dashboard_screenshot.png" alt="Dashboard screenshot" width="750" style="border-radius:15px; box-shadow:0 6px 25px rgba(59,73,223,0.3);"/>
</p>

---

<h2 style="color:#3b49df; font-weight:700;">📂 Project Files</h2>

| File/Folder         | Description                              |
|---------------------|------------------------------------------|
| `app.py`            | Streamlit dashboard main application    |
| `requirements.txt`  | Project dependencies                     |
| `artifacts/`        | Stored trained models                    |
| `screenshots/`      | Visual assets like screenshots and GIFs |
| `README.md`         | This file                               |

---

<details style="font-size:1.1rem;">
<summary><strong>🤝 Contributing & Support</strong></summary>
<p style="padding:15px; color:#333;">
Thank you for considering contributing! Whether adding features, fixing bugs, or improving design, all contributions are welcome.  
- Open issues to discuss improvements or report problems.<br>
- Fork the repo and submit pull requests with clear descriptions.<br>
- Engage in discussions to help steer future development.
</p>
</details>

---

<h2 style="color:#3b49df; font-weight:700;">📬 Contact</h2>

<p style="font-size:1.1rem;">
<b>Joy Biswas</b><br>
Email: <a href="mailto:bjoy1403@gmail.com">bjoy1403@gmail.com</a><br>
GitHub: <a href="https://github.com/JoyBiswas1403">https://github.com/JoyBiswas1403</a>
</p>

---

<p align="center" style="font-style:italic; color:#555;">
  Made with ❤️ by Joy Biswas — bringing finance and AI closer through elegant code and thoughtful design.
</p>
