# Use Python base image
FROM python:3.10-slim

# Install system dependencies (must update first)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    espeak-ng \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirement files safely (if they exist)
COPY requirements.txt* setup.py* /workspace/

# Install Python dependencies
RUN pip install --upgrade pip \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Create non-root user (optional)
RUN useradd --create-home devuser && chown -R devuser:devuser /workspace
USER devuser

# Expose default port for Streamlit / Gradio apps
EXPOSE 8501