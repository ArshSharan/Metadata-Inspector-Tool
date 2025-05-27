# Use the official Python image as the base
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        exiftool \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code
COPY Streamlit_app.py .

# Expose the port Streamlit will run on
EXPOSE 8080

# Set Streamlit to listen on all interfaces and port 8080 (Render default)
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Command to run the app
CMD ["streamlit", "run", "Streamlit_app.py"]
