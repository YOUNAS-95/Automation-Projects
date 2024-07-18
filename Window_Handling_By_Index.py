from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

Service_obj=Service("C:\chromedriver.exe") 
driver=webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(30)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Example_dropdown=Select(driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']"))
Example_dropdown.select_by_value("option2")
time.sleep(5)

check_box2=driver.find_element(By.XPATH,"//label[@for='radio2']/input").click()
time.sleep(3)

check_box3=driver.find_element(By.XPATH,"//input[@id='checkBoxOption3']").click()
time.sleep(2)

country=driver.find_element(By.XPATH,"//input[@type='text']").send_keys("pak")
countries=driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/div")

for x in countries:
    if x.text=="Spain":
        x.click()
        time.sleep(3)
tab=driver.find_element(By.XPATH,"//a[@id='opentab']").click()
time.sleep(10)

# driver.window_handles()
new_window_handle=driver.window_handles[-1]
driver.switch_to.window(new_window_handle)

courses=driver.find_element(By.XPATH,"//ul[@class='navbar-nav ml-auto']/li[2]/a")
courses.click()
time.sleep(4)

back_up=driver.window_handles[0]
driver.switch_to.window(back_up)
Enter_your_Name=driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Younas Khan")
time.sleep(5)

conform=driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
alert=Alert(driver)
alert.accept()
time.sleep(10)

Hide=driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
Show_example=driver.find_element(By.XPATH,"//input[@name='show-hide']").send_keys("coder12345")
time.sleep(3)