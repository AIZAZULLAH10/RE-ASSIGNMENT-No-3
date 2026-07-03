from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Test Login
driver.get("http://localhost:8080/login")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# Save Screenshot of dashboard
driver.save_screenshot("../../screenshots/dashboard_after_login.png")

# 2. Test Add Invoice
driver.get("http://localhost:8080/add-invoice")
time.sleep(2)
driver.find_element(By.NAME, "customer").send_keys("Test Customer")
driver.find_element(By.NAME, "amount").send_keys("500")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

# Save Screenshot of invoice added
driver.save_screenshot("../../screenshots/invoice_added.png")
driver.quit()
