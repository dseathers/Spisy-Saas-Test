from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# Path ke msedgedriver.exe
driver_path = "msedgedriver.exe"

# Inisialisasi Service untuk EdgeDriver
service = Service(driver_path)
driver = webdriver.Edge(service=service)
try:
    driver.get("https://saas.spisy.co.id/")
    print("Berhasil membuka web")

    time.sleep(4)

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    company_field = driver.find_element(By.ID, "company")

    username_field.send_keys("20240011")
    password_field.send_keys("Dekrit15")
    company_field.send_keys("ABC")
    print("berhasil input data form login")
    time.sleep(4)

    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'items-center') and @type='submit']")
    login_button.click()
    print("Login Berhasil")

    time.sleep(10)
finally:

    driver.close()
    print("test selesai")