# 1. Start with a lightweight Python OS
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the ingredient list
COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code
COPY . .

# 6. The Command to run when the container starts
CMD ["python", "src/fetch_crypto.py"]