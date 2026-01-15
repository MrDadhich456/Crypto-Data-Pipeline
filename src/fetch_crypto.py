import requests
import datetime
import csv
import os
import time

# --- CONFIGURATION ---
FILE_PATH = "data/crypto_prices.csv"
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=inr"

# 1. Setup the CSV File (Write Headers if file is new)
# Check if file exists, if not, create it with headers
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Bitcoin", "Ethereum", "Solana"])
    print("🆕 Created new data file: crypto_prices.csv")

print("📡 Starting Data Stream (Press Ctrl+C to stop)...")

# 2. The Infinite Loop (Run forever)
while True:
    try:
        # Fetch Data
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Extract
            btc = data["bitcoin"]["inr"]
            eth = data["ethereum"]["inr"]
            sol = data["solana"]["inr"]
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save to CSV (Append Mode 'a')
            with open(FILE_PATH, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([now, btc, eth, sol])
            
            print(f"✅ Saved at {now}: BTC=INR{btc}")
        else:
            print(f"⚠️ API Error: {response.status_code}")

    except Exception as e:
        print(f"❌ System Error: {e}")

    # 3. Wait for 60 seconds (Don't get banned by API)
    time.sleep(60)