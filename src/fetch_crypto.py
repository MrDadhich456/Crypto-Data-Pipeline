import requests
import datetime
import time
import psycopg2
import os

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1234"  # The password you set for Docker

print("Connecting to The Vault (PostgreSQL)...")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=inr"

print("Starting Data Pipeline to SQL...")

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            btc = data["bitcoin"]["inr"]
            eth = data["ethereum"]["inr"]
            sol = data["solana"]["inr"]
            now = datetime.datetime.now()

            # Insert into PostgreSQL
            conn = get_db_connection()
            cur = conn.cursor()
            
            insert_query = """
            INSERT INTO crypto_prices (timestamp, bitcoin_inr, ethereum_inr, solana_inr)
            VALUES (%s, %s, %s, %s)
            """
            
            cur.execute(insert_query, (now, btc, eth, sol))
            conn.commit()  # IMPORTANT: Save the transaction
            
            cur.close()
            conn.close()
            
            print(f"Inserted into DB at {now}: BTC=₹{btc}")
        else:
            print(f"API Error: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")


    time.sleep(30)