# Dockerfile

# 1. Base Image: Start with a lightweight Python version
FROM python:3.9-slim

# 2. Work Directory: Create a folder inside the container
WORKDIR /app

# 3. Dependencies: Copy the file and install libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Code: Copy your main.py into the container
COPY main.py .

# 5. Command: What happens when the container starts?
# We use 'uvicorn' to start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]