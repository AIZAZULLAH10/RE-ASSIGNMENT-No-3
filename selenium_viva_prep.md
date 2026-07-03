# Viva Preparation: Selenium Reverse Engineering

This document explains the Selenium tool and the `selenium_test.py` script step-by-step so you can confidently answer questions during your Viva.

## What is Selenium?
**Selenium** is an open-source suite of tools primarily used for automating web browsers. It provides a way to write scripts (in languages like Python, Java, or C#) that control a browser exactly like a real human would—clicking buttons, typing text, and navigating between pages.

**What is it used for?**
1. **Automated Testing:** Its main purpose is to test web applications automatically to ensure they work correctly across different browsers.
2. **Web Scraping:** It can be used to extract data from dynamic websites where standard scrapers fail (because it can wait for JavaScript to load).
3. **Reverse Engineering (Our Use Case):** When we don't have access to a system's source code, we use Selenium to systematically interact with the UI. By observing how the system reacts to automated inputs, we can map out hidden URLs, form requirements, and business logic.

## 1. Setting Up the Automation
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
```
**What this does:** 
* `webdriver` is the core of Selenium. It acts like a "robot hand" that takes control of your browser.
* `By` is a tool used to search for elements on a web page (like finding a button by its ID or Name).
* `driver = webdriver.Chrome()` tells the script to open a brand-new, automated Google Chrome window.

## 2. Reverse Engineering the Login Page
```python
driver.get("http://localhost:5000/login")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
```
**What this does:**
* `driver.get()` tells the browser to go to your local legacy app's login page.
* `time.sleep(2)` forces the script to pause for 2 seconds. We do this to ensure the page has completely loaded before the robot tries to type anything.
* `find_element(By.NAME, "username")` is where the **Reverse Engineering** happens! The script looks at the page's HTML structure to find an input box named "username". Once it finds it, `.send_keys("admin")` types the word "admin" into the box.
* `By.XPATH` is a way to find elements by their HTML tags. `"//button[@type='submit']"` means: "Search the whole page for a `<button>` that has a `type` equal to `submit`". Then `.click()` clicks it!

## 3. Taking Proof (Screenshots)
```python
driver.save_screenshot("dashboard_after_login.png")
```
**What this does:**
* After clicking login, the page redirects to the dashboard. `save_screenshot()` takes a picture of the automated browser window and saves it to your folder. In reverse engineering, this acts as documented proof that the login action was successful.

## 4. Reverse Engineering the Invoice Feature
```python
driver.get("http://localhost:5000/add-invoice")
time.sleep(2)
driver.find_element(By.NAME, "customer").send_keys("Test Customer")
driver.find_element(By.NAME, "amount").send_keys("500")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

driver.save_screenshot("invoice_added.png")
driver.quit()
```
**What this does:**
* It navigates to the hidden `/add-invoice` URL.
* It finds the form fields named `customer` and `amount` (which we discovered by inspecting the HTML of the legacy app) and fills them in.
* It submits the form, takes another screenshot of the success page, and finally calls `driver.quit()` to close the Chrome window and end the automation.

---
## 💡 Viva Question: "Why are we doing this?"
If the examiner asks: *"Why did you use Selenium for this assignment?"*

**Your Answer:** "In Software Reverse Engineering, we often don't have access to the backend source code or the database. By using Selenium, we can simulate a real user clicking around the interface. This allows us to discover hidden URLs, figure out what data the forms require (like `username`, `customer`, `amount`), and observe how the system responds, all by analyzing it from the outside!"
