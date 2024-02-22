from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.implicitly_wait(50)
driver.maximize_window()

driver.get("https://shopee.com.my/buyer/login?from=https%3A%2F%2Fshopee.com.my%2Fuser%2Fpurchase%2F&next=https%3A%2F%2Fshopee.com.my%2Fuser%2Fpurchase%2F")
time.sleep(2)

lang_select = driver.find_element(By.XPATH, "(//button[@class='shopee-button-outline shopee-button-outline--primary-reverse'])[1]")
lang_select.click()
time.sleep(5)
print("Language was selected")

username = driver.find_element(By.XPATH, "//input[@class='pDzPRp EL8Hdg']")
username.click()
username.send_keys("fockbroke88@gmail.com")
time.sleep(3)
print("Username value passed")


password = driver.find_element(By.XPATH, "//input[@class='pDzPRp']")
password.click()
password.send_keys("Fockbroke88")
time.sleep(10)
print("Password value passed")


login_button = driver.find_element(By.XPATH,"//button[@class='wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1']")
login_button.click()
time.sleep(5)
print("Login Successfully")

driver.quit()