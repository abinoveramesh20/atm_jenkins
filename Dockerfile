# Use the official Python image from Docker Hub
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application code and requirements into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 (or the port you want to use for the web server)
EXPOSE 8000

# Use Gunicorn to serve the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
