# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask legacy application
CMD ["python", "app.py"]
