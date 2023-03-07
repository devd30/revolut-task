# This Dockerfile defines a lightweight Python image that installs the required packages, exposes port 80 for HTTP traffic, and sets the command to start the server using Gunicorn.

FROM python:3.9-slim-buster

ARG DEFAULT_REDIS_HOST="0.0.0.0"
ENV REDIS_HOST=$DEFAULT_REDIS_HOST

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for HTTP traffic
EXPOSE 5000

# Set the command to start the server
CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:5000", "--log-level", "info"]
