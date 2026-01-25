#!/bin/bash

# 1. Define the Job (Run every minute)
# We use the full path to docker because Cron is picky
JOB="* * * * * /usr/bin/docker run --rm --network host crypto-fetcher >> /tmp/crypto_cron.log 2>&1"

# 2. Write it to Crontab
# This command replaces the current schedule with our new job
echo "$JOB" | crontab -

echo "✅ Pipeline ENABLED. Running every 60 seconds."
echo "📜 Monitor logs with: tail -f /tmp/crypto_cron.log"