# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your project files
COPY . /app/

# Expose the port your app runs on (change if needed)
EXPOSE 8000

# Command to run your API server (change for Django or Flask)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
