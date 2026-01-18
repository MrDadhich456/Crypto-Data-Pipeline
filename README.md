🪙 Project Bit-Stream

A Dockerized Data Pipeline for Real-Time Crypto Analytics.

💡 Why I Built This

I wanted to move beyond basic Python scripts and build a production-grade pipeline. My goal was to solve a simple problem: "How do I track and visualize Bitcoin volatility in real-time without keeping my laptop on 24/7?"

Instead of just saving data to a CSV file (which is fragile), I containerized the entire application to simulate a real microservices architecture.

🏗️ How It Works

The system consists of three Docker containers talking to each other:

The Fetcher: A Python script hits the CoinGecko API every 60 seconds to grab live prices (BTC, ETH, SOL) in INR.

The Vault: A PostgreSQL instance stores the data. I used Docker Volumes to ensure data persists even if the container crashes.

The Dashboard: A Streamlit app reads from the database and visualizes trends with an interactive sidebar.

graph LR

    A[CoinGecko API] -->|JSON| B(Python Service)
    B -->|Ingest| C[(Postgres DB)]
    C -->|Query| D[Streamlit Dashboard]


🛠️ The Stack

Ingestion: Python (requests, pandas)

Storage: PostgreSQL (Dockerized)

Visualization: Streamlit

DevOps: Docker, Docker Compose, Bash Scripting

🚀 Quick Start

You don't need to install Python. You just need Docker.

1. Clone the repo

        git clone https://github.com/MrDadhich456/Crypto-Data-Pipeline.git
        cd Crypto-Data-Pipeline


2. Launch the Engine
I wrote a bash script to handle the build and network bridging automatically.

      
        ./start_pipeline.sh


3. Open the Dashboard

        streamlit run src/dashboard_drill.py


🧠 What I Learned

Docker Networking: Learned how to bridge containers using --network host so the Python script can talk to the Database.

State Management: How to use Docker Volumes to prevent data loss during container restarts.

SQL Optimization: Used psycopg2 for efficient batch inserts instead of opening/closing connections repeatedly.

🔮 Future Roadmap

[ ] Replace time.sleep(60) with a real Cron Job.

[ ] Add Alerts (Email me if Bitcoin drops 5%).

[ ] Migrate the database to AWS RDS (Cloud).

Author: Mr.Dadhich
