# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables
# Default KB_PATH inside container (should be mounted)
ENV KB_PATH=/app/knowledge_base
# Ensure output is not buffered
ENV PYTHONUNBUFFERED=1

# Create the directory for mounting the knowledge base
RUN mkdir -p /app/knowledge_base

# Run the application
CMD ["uvicorn", "tutor_api:app", "--host", "0.0.0.0", "--port", "8000"]
