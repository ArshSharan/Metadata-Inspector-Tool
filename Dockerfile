
# Use official lightweight Python image
FROM python:3.10-slim

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
CMD curl -f http://localhost:8501/_stcore/health || exit 1
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Add this near the top of your Dockerfile
RUN apt-get update && apt-get install -y \
    wget \
    && wget -q -O /tmp/exiftool.tar.gz https://exiftool.org/Image-ExifTool-12.67.tar.gz \
    && tar xzf /tmp/exiftool.tar.gz -C /tmp \
    && cd /tmp/Image-ExifTool-* \
    && perl Makefile.PL \
    && make install \
    && rm -rf /tmp/*
# Set working directory
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    exiftool \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
