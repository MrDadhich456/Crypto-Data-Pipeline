#!/bin/bash

# 1. Print a cool banner
echo "=========================================="
echo "🚀 STARTING CRYPTO DATA PIPELINE"
echo "=========================================="

# 2. Check if Docker Database is running
if [ ! "$(docker ps -q -f name=my_postgres)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=my_postgres)" ]; then
        echo "😴 Waking up existing Database..."
        docker start my_postgres
    else
        echo "🐘 Creating NEW Database Container..."
        docker run --name my_postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
        echo "⏳ Waiting 5 seconds for DB to initialize..."
        sleep 5
    fi
else
    echo "✅ Database is already running."
fi

# 3. Build the Python Fetcher (in case code changed)
echo "🔨 Building Python Fetcher Image..."
docker build -t crypto-fetcher .

# 4. Run the Fetcher (connected to the DB)
echo "📡 Launching Data Stream..."
# Note: We use --network host so the container can find localhost
docker run --rm -it --network host crypto-fetcher