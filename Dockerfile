# Use official Python image with slim Debian
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Required for exiftool
    libimage-exiftool-perl \
    # Required for subprocess and temp files
    procps \
    # Clean up apt cache
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501

# Create and set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Verify exiftool installation
RUN exiftool -ver || { echo "ExifTool verification failed"; exit 1; }

# Expose the Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "Streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]