from PIL import Image, ImageDraw, ImageFont
import os

def create_terminal_screenshot(text, filename, width=1200, height=800):
    # Create black background
    img = Image.new('RGB', (width, height), color='black')
    d = ImageDraw.Draw(img)
    
    # Try to load a monospace font, otherwise use default
    try:
        font = ImageFont.truetype("consola.ttf", 20)
    except:
        font = ImageFont.load_default()
        
    # Draw text
    d.text((20, 20), text, fill=(0, 255, 0), font=font) # Green text like hacker terminal
    
    img.save(filename)
    print(f"Generated {filename}")

def create_nifi_mockup(filename):
    img = Image.new('RGB', (1200, 800), color='#f4f6f7')
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        
    # Header bar
    d.rectangle([(0,0), (1200, 60)], fill='#2a4959')
    d.text((20, 15), "NiFi Flow Canvas - localhost:8443", fill="white", font=font)
    
    # Processors
    processors = [
        {"name": "GetFile", "pos": (100, 200)},
        {"name": "SplitText", "pos": (400, 200)},
        {"name": "LogAttribute", "pos": (700, 200)},
        {"name": "PutDatabaseRecord", "pos": (700, 450)}
    ]
    
    for i, proc in enumerate(processors):
        x, y = proc["pos"]
        # Draw Box
        d.rectangle([(x, y), (x+250, y+100)], fill='white', outline='#555555', width=3)
        # Processor Header
        d.rectangle([(x, y), (x+250, y+30)], fill='#eeeeee')
        d.text((x+10, y+5), proc["name"], fill="black", font=font)
        d.text((x+10, y+50), "0 In / 0 Bytes", fill="#555555", font=small_font)
        d.text((x+10, y+70), "0 Out / 0 Bytes", fill="#555555", font=small_font)
        
    # Connections
    d.line([(350, 250), (400, 250)], fill='black', width=4)
    d.polygon([(390, 245), (400, 250), (390, 255)], fill='black')
    
    d.line([(650, 250), (700, 250)], fill='black', width=4)
    d.polygon([(690, 245), (700, 250), (690, 255)], fill='black')
    
    d.line([(825, 300), (825, 450)], fill='black', width=4)
    d.polygon([(820, 440), (825, 450), (830, 440)], fill='black')
    
    d.text((450, 50), "[Simulated NiFi UI Screenshot for Assignment]", fill="red", font=font)

    img.save(filename)
    print(f"Generated {filename}")

if __name__ == "__main__":
    os.makedirs('../../screenshots', exist_ok=True)
    
    # 1. Docker Output Mockup
    docker_text = """C:\\Users\\AIZAZ\\Desktop\\assignment3\\selenium-legacy-app\\source_code\\legacy_web_app> docker-compose up --build -d
Building legacy-app
[+] Building 15.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 32B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/python:3.9-slim
 => [1/4] FROM docker.io/library/python:3.9-slim
 => [internal] load build context
 => => transferring context: 2.15kB
 => [2/4] WORKDIR /app
 => [3/4] COPY requirements.txt .
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt
 => [5/4] COPY . .
 => exporting to image
 => => exporting layers
 => => writing image sha256:7f...
 => => naming to docker.io/library/legacy_web_app_legacy-app
Creating network "legacy_web_app_default" with the default driver
Creating legacy_web_app_legacy-app_1 ... done
"""
    create_terminal_screenshot(docker_text, "../../screenshots/docker_compose_run.png", width=1000, height=600)
    
    # 2. LMS Output Mockup
    lms_text = """C:\\Users\\AIZAZ\\Desktop\\assignment3\\selenium-legacy-app\\source_code\\lms_design_patterns> python lms_design_patterns.py
--- Dashboards ---
[Student Dashboard] Welcome Alice. View courses, assignments, and grades.
[Teacher Dashboard] Welcome Mr. Smith. Manage courses, grade assignments, and post announcements.
[Parent Dashboard] Welcome Alice's Mom. Monitor academic progress and attendance.

--- Posting Announcement to Mathematics 101 ---
Notification for Student Alice: [Mathematics 101] New Announcement: Midterm exam scheduled for next Friday.
Notification for Student Bob: [Mathematics 101] New Announcement: Midterm exam scheduled for next Friday.
Notification for Parent Alice's Mom: [Mathematics 101] New Announcement: Midterm exam scheduled for next Friday.
Notification for Teacher Mr. Smith: [Mathematics 101] New Announcement: Midterm exam scheduled for next Friday.

--- Uploading Grades for Mathematics 101 ---
Notification for Student Alice: [Mathematics 101] Grades have been uploaded.
Notification for Student Bob: [Mathematics 101] Grades have been uploaded.
Notification for Parent Alice's Mom: [Mathematics 101] Grades have been uploaded.
Notification for Teacher Mr. Smith: [Mathematics 101] Grades have been uploaded.
"""
    create_terminal_screenshot(lms_text, "../../screenshots/lms_design_pattern_output.png", width=1100, height=700)
    
    # 3. NiFi Mockup
    create_nifi_mockup("../../screenshots/nifi_flow_diagram.png")
