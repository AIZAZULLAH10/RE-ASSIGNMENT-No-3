# Viva Preparation: Docker Reverse Engineering

This document explains the Docker part of your assignment so you can answer questions confidently during your Viva.

## What is Docker?
**Docker** is a containerization tool. It packages an application and all its dependencies (like Python, Flask, libraries) into a single, isolated box called a **Container**. This container can run on any machine (Windows, Mac, Linux) exactly the same way without worrying about "it works on my machine" issues.

**Why use it for Reverse Engineering?**
When you find a legacy system, it usually requires a very specific, old environment (like an old version of Python or PHP) to run. If you try to install all that old software on your main laptop, it can break things. Docker allows us to replicate that old environment in an isolated container safely. We can run it, test it, break it, and reverse engineer it without messing up our host computer.

## Understanding the Dockerfile
```dockerfile
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
```
**What this does:**
* `FROM`: Grabs a base Linux environment with Python 3.9 pre-installed.
* `WORKDIR`: Creates a folder called `/app` inside the container.
* `COPY` & `RUN`: Copies our `requirements.txt` and installs Flask and Selenium inside the container.
* `CMD`: Tells the container to run `python app.py` as soon as it starts up.

## Understanding docker-compose.yml
```yaml
version: '3.8'
services:
  legacy-app:
    build: .
    ports:
      - "8081:5000"
    volumes:
      - ./data:/app/data
```
**What this does:**
* `build: .` tells Docker Compose to look for the `Dockerfile` in the same folder and build it.
* `ports: "8081:5000"` is crucial! It maps port 5000 (where the app runs *inside* the container) to port 8081 on your actual laptop. We specifically chose 8081 because port 8080 is often in use by other system services. This allows us to access it via `http://localhost:8081`.
* `volumes:` Maps the `data` folder inside the container to your local `data` folder so the invoices you create are saved to your actual hard drive.
