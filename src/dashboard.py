import streamlit as st
import pandas as pd
import psycopg2
import time

st.set_page_config(page_title="Crypto V2", page_icon="🧪")

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1234"

# 4. FUNCTION: load_data()
def load_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    
    query = "SELECT timestamp, bitcoin_inr, ethereum_inr, solana_inr FROM crypto_prices ORDER BY timestamp ASC"
    
    df = pd.read_sql(query, conn)
    
    conn.close()
    return df

st.title("🧪 Project Bit-Stream V2")

selected_coin = st.sidebar.selectbox("select currency",["Bitcoin", "Ethereum", "Solana"])

column_map = {
    "Bitcoin":"bitcoin_inr",
    "Ethereum":"ethereum_inr",
    "Solana":"solana_inr"
    }

selected_column = column_map[selected_coin]

placeholder = st.empty()

while True:
    df = load_data()
    
    df = df.set_index("timestamp")
    
    with placeholder.container():
        latest_price = df[selected_column].iloc[-1]
        
        st.metric(label=f"{selected_coin} Price", value=f"₹{latest_price:,.2f}")
        
        st.line_chart(data=df[selected_column])

        
    time.sleep(2)