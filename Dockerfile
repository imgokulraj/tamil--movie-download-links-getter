# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Streamlit
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit application code into the container
COPY . .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py"]
