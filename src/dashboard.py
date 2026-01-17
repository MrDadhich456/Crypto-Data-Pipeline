import streamlit as st
import pandas as pd
import psycopg2
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Crypto Live Dashboard", page_icon="📈")

# Database Connection Details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1234"

# Function to fetch data from Postgres
def load_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    # Read SQL directly into a Pandas DataFrame!
    query = "SELECT timestamp, bitcoin_inr FROM crypto_prices ORDER BY timestamp ASC"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- THE UI ---
st.title("💰 Real-Time Bitcoin Tracker")
st.write("Live data fetched from CoinGecko -> Docker -> Postgres")

# Create a placeholder for the chart
placeholder = st.empty()

# The Infinite Loop (Auto-Refresh)
while True:
    # 1. Get new data
    df = load_data()
    
    # 2. Set the Index to Timestamp (required for charts)
    df = df.set_index("timestamp")
    
    # 3. Draw the Chart inside the placeholder
    with placeholder.container():
        # Show the latest price in big text
        latest_price = df["bitcoin_inr"].iloc[-1]
        st.metric(label="Bitcoin Price (INR)", value=f"₹{latest_price:,.2f}")
        
        # Show the graph
        st.line_chart(df["bitcoin_inr"])
        
    # 4. Refresh every 10 seconds
    time.sleep(10)