# Software Reverse Engineering (CSE 327) - Assignment 3

## 1. Introduction: The Legacy System
For this assignment, a **Legacy Invoice Management System** was selected as the target system for reverse engineering. It is a monolithic Python Flask application that lacks documentation and automated testing. The system relies on simple HTML forms for logging in and creating invoices, storing data locally, and interacting with users via a web interface. 

The goal of this assignment is to reverse engineer this undocumented legacy application by:
1. Understanding its business logic via automated UI testing (Selenium).
2. Containerizing the outdated environment to safely run and analyze it without breaking the host machine (Docker).
3. Mapping out how data is processed, extracted, and transferred within the system (Apache NiFi).

---

## 2. Applying Tool 1: Selenium (Automated UI Testing)
Since the legacy system lacked documentation regarding its expected behavior, Selenium was applied to automate interactions with the UI. This allowed us to extract the hidden logic, trace the workflow from login to invoice creation, and confirm how the system responds to valid inputs.

### How it was applied:
- We created a Python script using the `selenium` and `webdriver` libraries.
- The script automatically launches a Chrome browser and navigates to the legacy app's login page.
- It simulates a user entering credentials (`admin` / `admin123`) and clicking the submit button.
- It then navigates to the invoice creation page, simulates form filling (`Test Customer`, `500`), and submits the data.
- During this process, it captures screenshots to visually document the UI states.

### Code Implemented:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Test Login
driver.get("http://localhost:8081/login")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.save_screenshot("../screenshots/dashboard_after_login.png")

# Test Add Invoice
driver.get("http://localhost:8081/add-invoice")
time.sleep(2)
driver.find_element(By.NAME, "customer").send_keys("Test Customer")
driver.find_element(By.NAME, "amount").send_keys("500")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.save_screenshot("../screenshots/invoice_added.png")
driver.quit()
```

### Execution Output (Screenshots):
<br><br><br><br><br>

---

## 3. Applying Tool 2: Docker (Containerization)
Legacy systems often have very specific, outdated dependencies that can conflict with modern operating systems. Docker was applied to encapsulate the legacy Flask application into an isolated container. This allowed us to successfully replicate, run, and reverse engineer the environment without risking any damage to the host machine.

### How it was applied:
- A `Dockerfile` was used to define the base environment and install legacy requirements via `pip`.
- A `docker-compose.yml` file was created to map port `8081` on the host to port `5000` inside the container.
- Persistent volumes were configured to ensure that legacy data is safely stored outside the container.
- The application was deployed as the `legacy_invoice_system` container.

### Docker Configuration (docker-compose.yml):
```yaml
services:
  legacy-app:
    build:
      context: ../app
      dockerfile: ../docker/Dockerfile
    container_name: legacy_invoice_system
    ports:
      - "8081:5000"
    volumes:
      - ../app/data:/app/data
    restart: unless-stopped
```

### Execution Command:
```powershell
docker-compose up --build -d
```

### Execution Output (Docker Desktop Screenshot):
<br><br><br><br><br>

---

## 4. Applying Tool 3: Apache NiFi (Data Flow Automation)
To reverse engineer how data moves and is processed within the legacy system architecture, Apache NiFi was applied to visually trace and document the data flow pipeline.

### How it was applied:
- An Apache NiFi container was launched on port `8443`.
- By accessing the NiFi web canvas, we reverse-engineered the data extraction process by designing a pipeline.
- The pipeline represents pulling raw files (`GetFile`), breaking them down into manageable records (`SplitText`), logging the structure of the data (`LogAttribute`), and finally pushing the structured data into a database (`PutDatabaseRecord`).

### Execution Command:
```powershell
docker run --name nifi -p 8443:8443 -d apache/nifi:latest
```

### Pipeline Flowchart (NiFi Canvas Screenshot):
<br><br><br><br><br>

---

## 5. Part 4: Design Pattern Implementation (Smart University LMS)
To address the challenges of creating customized dashboards for different roles and sending automated notifications, we applied two software design patterns.

### Selected Design Patterns:
1. **Factory Method Pattern**: Implemented to dynamically generate the correct dashboard (`StudentDashboard`, `TeacherDashboard`, `ParentDashboard`) based on the user type, keeping the instantiation logic encapsulated.
2. **Observer Pattern**: Implemented to handle the notification requirements. The course acts as the Subject, and relevant users (Students, Teachers, Parents) act as Observers who automatically receive updates when the state changes.

### Execution Output (Terminal Screenshot):
<br><br><br><br><br>
