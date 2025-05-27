# Use official Python image with slim Debian base
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    procps \
    perl \
    make \
    && rm -rf /var/lib/apt/lists/*

# Manually install the latest ExifTool (always works)
RUN wget https://exiftool.org/Image-ExifTool.tar.gz && \
    tar -xzf Image-ExifTool.tar.gz && \
    cd Image-ExifTool-* && \
    perl Makefile.PL && \
    make && make test && make install && \
    cd .. && rm -rf Image-ExifTool*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Start the Streamlit app
CMD ["streamlit", "run", "Streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
