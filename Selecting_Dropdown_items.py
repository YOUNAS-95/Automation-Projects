from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

Service_obj=Service("C:\chromedriver.exe")
driver=webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(30)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(5)
search=driver.find_element(By.XPATH,"//input[@type='text']")
search.send_keys("en")
time.sleep(5)
countries=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/a")
time.sleep(5)

for x in countries:
    print(x)
    if x.text=="Benin":
        x.click()
        time.sleep(3)
        break
another=driver.find_element(By.XPATH,"//input[@type='text']")
another.send_keys("pak")

for y in another:
    if y.text=="Pakistan":
        y.click()
        time.sleep(3)
