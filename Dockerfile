# Use an official Python runtime as the base image
FROM python:3.9.16-slim-buster as builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Use a new stage for the final image
FROM python:3.9.16-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the rest of the application code
COPY . .

# Create a non-root user and switch to it
RUN useradd -m heyhido
USER heyhido

# Set environment variables
ENV FLASK_APP=src.app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 5001

# Run the application with Python module
CMD ["python", "-m", "src.app"]