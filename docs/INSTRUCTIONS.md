# Project Instructions

> **🟢 PROGRESS CHECKPOINT (Read after PC Restart):**
> *   **What we just did:** We successfully installed WSL (Ubuntu) and set up the UNIX username (`aizaz`).
> *   **What to do right now:** 
>     1. Make sure Docker Desktop is open and running.
>     2. Open your terminal in VS Code, navigate to `docker`, and run `docker-compose up --build -d`.
>     3. Tell me (the AI) that you are back and Docker is running, and we will move on to the Selenium tests!


This project is a legacy Python Flask app acting as an Invoice Management System, containerized with Docker, and tested using Selenium.

Here are the instructions on how to run everything, along with troubleshooting steps if Docker fails.

---

## 1. Starting the Application

You have two choices for running the application: using Docker (recommended) or running the Python app directly.

### Option A: Using Docker (Recommended)
1. Open Docker Desktop and ensure it is running (the icon in your system tray should be green).
2. Open PowerShell and navigate to the `docker` directory:
   ```powershell
   cd "f:\Desktop\UNIVERSITY\7 semester\RE\Asiigment\assignment3\selenium-legacy-app\docker"
   ```
3. Build and start the container:
   ```powershell
   docker-compose up --build -d
   ```
4. The app will be available at: **http://localhost:8080**
5. To stop the application later, run:
   ```powershell
   docker-compose down
   ```

> **Troubleshooting Docker:** 
> If you get a "WSL not installed" or "failed to connect to the docker API" error, it means Windows Subsystem for Linux is missing.
> 1. Open PowerShell as Administrator.
> 2. Run: `wsl --install`
> 3. Restart your computer.
> 4. Open Docker Desktop and try the Docker instructions again.

### Option B: Running Python Natively (No Docker)
If you cannot use Docker, you can run the app directly using Python.
1. Open PowerShell and navigate to the `app` directory:
   ```powershell
   cd "f:\Desktop\UNIVERSITY\7 semester\RE\Asiigment\assignment3\selenium-legacy-app\app"
   ```
2. Install the necessary Python packages:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the application:
   ```powershell
   python app.py
   ```
4. The app will be available at: **http://localhost:5000**

*(Note: If you use Option B, you must edit `selenium/selenium_test.py` to target port 5000 instead of 8080).*

---

## 2. Running Selenium Automated Tests

Once the application is running (via Option A or Option B), you can run the automated tests.

1. Open a new terminal and navigate to the `selenium` folder:
   ```powershell
   cd "f:\Desktop\UNIVERSITY\7 semester\RE\Asiigment\assignment3\selenium-legacy-app\selenium"
   ```
2. Make sure Selenium is installed:
   ```powershell
   pip install selenium
   ```
3. Run the test script:
   ```powershell
   python selenium_test.py
   ```
4. The script will automatically open a browser window, log in, create an invoice, and take screenshots.
5. You can view the output images in the `screenshots/` directory.

---

## Project Structure Overview
* **`app/`**: The legacy Flask application source code and data.
* **`docker/`**: Docker configurations (`Dockerfile` and `docker-compose.yml`).
* **`selenium/`**: Selenium automated end-to-end test scripts.
* **`lms/`**: LMS Design Patterns Python scripts.
* **`nifi/`**: Dedicated folder for any Apache NiFi configs/flows.
* **`screenshots/`**: Where Selenium saves its output images.
* **`docs/`**: Project documentation (like this file!).
