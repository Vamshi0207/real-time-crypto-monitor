# 📈 Real-Time Cryptocurrency Market Monitor

![Project Screenshot](screenshot.png)

## 📖 Project Overview
This project is an end-to-end **Data Engineering & Analytics Pipeline** designed to track cryptocurrency market volatility in real-time. 

Unlike static datasets, this system builds its own historical database by fetching live data from the **CoinGecko API** every 60 seconds, storing it in a **SQLite** database, and visualizing trends dynamically in **Power BI**.

**Goal:** To identify undervalued assets and monitor "Pump and Dump" price action using a custom-built automated pipeline.

## 🛠️ Tech Stack
* **Python:** Core ETL logic (Extract, Transform, Load).
* **SQLite:** Relational database for time-series storage.
* **Power BI:** Interactive dashboard with Python script integration.
* **Pandas:** Data manipulation and SQL interfacing.
* **Requests:** API connectivity.

## ⚙️ Architecture
1.  **Extract:** Python script hits CoinGecko API endpoints to fetch Top 50 coins by market cap.
2.  **Transform:** Cleans raw JSON data, filters for key metrics (Price, Volume, Market Cap), and adds timestamp sequencing.
3.  **Load:** Inserts structured records into a local `crypto_data.db` SQLite database.
4.  **Visualize:** Power BI connects via Python script to render live price tickers, trend lines, and volume heatmaps.

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Vamshi0207/crypto-market-monitor.git](https://github.com/Vamshi0207/crypto-market-monitor.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the ETL Pipeline:**
    ```bash
    python main.py
    ```
    *The script will begin fetching data every 60 seconds. Keep the terminal open.*

4.  **Open Power BI:**
    * Launch `crypto_dashboard.pbix`.
    * Click **Refresh** in the Home ribbon to see the latest data flow in.

## 📊 Dashboard Features
* **Live Trend Line:** Visualizes second-by-second price volatility (Heartbeat Monitor).
* **Top Movers:** Bar chart dynamically highlighting top gainers vs. losers.
* **Market Depth:** Detailed table with sorting capabilities for volume and market cap.
* **Slicer Control:** Filter specific assets (e.g., Bitcoin, Ethereum) for focused analysis.

---
*Created by Vamshi Krishna 
