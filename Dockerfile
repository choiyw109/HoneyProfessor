# Use an official Python runtime as base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Set the working directory to src (where main.py is located)
WORKDIR /app/src

# Run the script
CMD ["python", "-u", "main.py"]
