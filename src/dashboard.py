# 1. IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import psycopg2
import time

# 2. PAGE CONFIGURATION
st.set_page_config(page_title="Crypto V2", page_icon="🧪")

# 3. DATABASE VARIABLES
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1234"

# 4. FUNCTION: load_data()
def load_data():
    # A. Connect to Database (FILL THIS IN)
    # Hint: Use psycopg2.connect(...)
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    
    # B. Write the Query to get ALL data
    query = "SELECT timestamp, bitcoin_inr, ethereum_inr, solana_inr FROM crypto_prices ORDER BY timestamp ASC"
    
    # C. Read into DataFrame
    df = pd.read_sql(query, conn)
    
    conn.close()
    return df

# 5. UI SETUP - SIDEBAR (The New Feature!)
st.title("🧪 Project Bit-Stream V2")

# A. Create a Sidebar Selector
# Hint: Use st.sidebar.selectbox("Label", ["Option1", "Option2", ...])
selected_coin = st.sidebar.selectbox("select currency",["Bitcoin", "Ethereum", "Solana"])

# B. Map the readable name to the database column name
# (e.g., "Bitcoin" -> "bitcoin_inr")
column_map = {
    "Bitcoin":"bitcoin_inr",
    "Ethereum":"ethereum_inr",
    "Solana":"solana_inr"
    }

# Get the actual column name to use in the chart
selected_column = column_map[selected_coin]

# 6. PLACEHOLDER
placeholder = st.empty()

# 7. THE INFINITE LOOP
while True:
    # A. Load Data
    df = load_data()
    
    # B. Set Index
    df = df.set_index("timestamp")
    
    # C. Display inside the placeholder
    with placeholder.container():
        # Get the latest price for the SELECTED column
        # Hint: Use df[selected_column] instead of df["bitcoin_inr"]
        latest_price = df[selected_column].iloc[-1]
        
        # Display Metric
        st.metric(label=f"{selected_coin} Price", value=f"₹{latest_price:,.2f}")
        
        # Display Chart for the SELECTED column
        st.line_chart(data=df[selected_column])

        
    # D. Refresh Rate
    time.sleep(2)