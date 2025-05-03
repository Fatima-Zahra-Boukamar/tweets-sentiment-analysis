#dockerfile
#-----------------------------------------------------
# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .
#COPY . /app
# Install dependencies
COPY packages /packages
RUN pip install --no-cache-dir --find-links=/packages -r requirements.txt

# Default command to run your Python producer
CMD ["python", "producer.py"]
