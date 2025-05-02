# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

RUN apt-get update && apt-get install -y make

ENV PYTHONPATH=/app

# Install project and dependencies via setup.py
RUN pip install --no-cache-dir .

# Expose both FastAPI and Streamlit ports
EXPOSE 8000
EXPOSE 8501

# Start both services
CMD ["make", "run"]
