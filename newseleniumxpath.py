from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

service_obj=Service("C:\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
time.sleep(10)

driver.get("https://www.w3schools.com/")
driver.title
print(driver.title)
driver.current_url

# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/ul/li[2]/a" ).click()


