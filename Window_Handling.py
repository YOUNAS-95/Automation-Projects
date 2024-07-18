from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj=Service("C:\chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://www.w3schools.com/")
driver.find_element (By.CLASS_NAME,"user-anonymous tnb-signup-btn w3-bar-item w3-button w3-right ws-green ws-hover-green ga-top ga-top-signup").click()
# time.sleep(15)


print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.maximize_window()
driver.refresh()
driver.forward()
driver.close()