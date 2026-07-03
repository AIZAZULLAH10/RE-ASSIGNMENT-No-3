# Software Reverse Engineering - Assignment 3

This repository contains the complete implementation for Assignment 3 for the Software Reverse Engineering (CSE 327) course. It fulfills the requirements for testing, containerization, data flow analysis, and design pattern implementation.

## Project Structure

The project has been refactored into a clean, professional structure to separate documentation, source code, and assets.

```
/
├── docs/                        # All documentation and Viva preparation materials
│   ├── assignment detail.pdf    # Original assignment specification
│   ├── assignment_text.txt      # Extracted text of the assignment
│   ├── lms_design_document.md   # UML and explanations for LMS Design Patterns
│   ├── viva_prep_docker.md      # Viva notes on Docker (Tool 2)
│   ├── viva_prep_nifi.md        # Viva notes on Apache NiFi (Tool 3)
│   └── viva_prep_selenium.md    # Viva notes on Selenium Testing (Tool 1)
│
├── screenshots/                 # Screenshots demonstrating successful execution
│   ├── dashboard_after_login.png
│   └── invoice_added.png
│
├── source_code/                 # Executable code and configurations
│   ├── legacy_web_app/          # Dockerized Python Flask App (Tool 2)
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   ├── requirements.txt
│   │   ├── templates/
│   │   └── data/
│   │
│   ├── lms_design_patterns/     # Python implementation of Factory & Observer patterns
│   │   └── lms_design_patterns.py
│   │
│   ├── selenium_tests/          # UI Automation scripts (Tool 1)
│   │   └── selenium_test.py
│   │
│   └── utils/                   # Helper scripts used during development
│       └── extract_pdf.py
```

## How to Run the Project Components

### 1. Tool 1: Selenium (UI Automation)
To run the automated tests, the legacy application must be running first (see Tool 2 below).
1. Navigate to the Selenium tests directory:
   ```bash
   cd source_code/selenium_tests
   ```
2. Run the script:
   ```bash
   python selenium_test.py
   ```
*(This will interact with the legacy app, fill forms, and save screenshots in the current directory).*

### 2. Tool 2: Docker (Containerization)
We have containerized a legacy Python application to run in an isolated environment.
1. Navigate to the legacy app directory:
   ```bash
   cd source_code/legacy_web_app
   ```
2. Build and run the container:
   ```bash
   docker-compose up --build -d
   ```
3. Open your browser and visit: `http://localhost:8080`
4. Stop the container when finished:
   ```bash
   docker-compose down
   ```

### 3. Tool 3: Apache NiFi (Data Flow)
To simulate visually mapping a data flow from the legacy system:
1. Run Apache NiFi via Docker in any terminal:
   ```bash
   docker run --name nifi -p 8443:8443 -d apache/nifi:latest
   ```
2. Wait 1-2 minutes for the service to start.
3. Access the visual canvas at `https://localhost:8443/nifi` in your web browser.
4. Drag the `GetFile`, `SplitText`, `LogAttribute`, and `PutDatabaseRecord` processors onto the canvas and connect them to create your pipeline screenshot.
5. Cleanup:
   ```bash
   docker stop nifi
   docker rm nifi
   ```

### 4. Design Pattern Implementation (LMS)
This script demonstrates the **Factory Method** (for role-based dashboards) and **Observer Pattern** (for automatic notifications) applied to a Smart University LMS.
1. Navigate to the design patterns directory:
   ```bash
   cd source_code/lms_design_patterns
   ```
2. Execute the simulation:
   ```bash
   python lms_design_patterns.py
   ```
*(Review `docs/lms_design_document.md` for the UML diagram and detailed justifications).*

---
**Course:** Software Reverse Engineering (CSE 327)
**Department:** Computer Science
