import requests
import sqlite3
import time
import pandas as pd

# 1. Setup Database (This only needs to happen once)
conn = sqlite3.connect('crypto_data.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS crypto_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    current_price REAL,
    market_cap REAL,
    total_volume REAL,
    high_24h REAL,
    low_24h REAL,
    price_change_24h REAL,
    market_cap_change_24h REAL,
    circulating_supply REAL
)
'''
cursor.execute(create_table_query)
conn.commit()
print("Table checked/created successfully.")

# 2. Start the Loop
while True:
    print("Fetching new data...")
    
    # --- EXTRACT (Inside the loop!) ---
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    try:
        response = requests.get(url)
        raw_data = response.json()
        
        # --- TRANSFORM (Inside the loop!) ---
        clean_data = []
        for coin in raw_data:
            simplified_coin = {
                'name': coin['name'],
                'current_price': coin['current_price'],
                'market_cap': coin['market_cap'],
                'total_volume': coin['total_volume'],
                'high_24h': coin['high_24h'],
                'low_24h': coin['low_24h'], 
                'price_change_24h': coin['price_change_24h'], 
                'market_cap_change_24h': coin['market_cap_change_24h'], 
                'circulating_supply': coin['circulating_supply']
            }
            clean_data.append(simplified_coin)

        # --- LOAD (Inside the loop!) ---
        insert_query = '''
        INSERT INTO crypto_data (
            name, current_price, market_cap, total_volume, high_24h, low_24h, 
            price_change_24h, market_cap_change_24h, circulating_supply
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        for coin in clean_data:
            cursor.execute(insert_query, (
                coin['name'], coin['current_price'], coin['market_cap'], coin['total_volume'],
                coin['high_24h'], coin['low_24h'], coin['price_change_24h'],
                coin['market_cap_change_24h'], coin['circulating_supply']
            ))
        
        conn.commit()
        print("Data inserted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    # --- WAIT ---
    print("Sleeping for 60 seconds...")
    time.sleep(60)

# Note: We technically never reach conn.close() because the loop is infinite, 
# but you can stop the script manually (Ctrl+C).