from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
Service_obj=Service("C:\chromedriver.exe") 
driver=webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(30)

driver.get("https://www.daraz.pk/")
login=driver.find_element(By.XPATH,"//a[@class='bld-txt']")
login.click()

email=driver.find_element(By.XPATH,"//input[@placeholder='Please enter your Phone Number or Email']")
email.send_keys("0315>>>>....")

password=driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("Your Password")
time.sleep(2)
submit=driver.find_element(By.XPATH,"//button[@type='submit']")
submit.click()
time.sleep(2)

search=driver.find_element(By.XPATH,"//input[@type='search']")
search.send_keys("Toys")
drop=driver.find_elements(By.XPATH,"//a[@class='suggest-common--2KmE ']/span/span/b")

for x in drop:
    if x.text=="Toys":
        x.click()
        break

time.sleep(2)

car=driver.find_element(By.XPATH,"//a[@title='Rock Crawler Electric RC Vehicles Alloyed Remote Control Toy Car for Kids & Boys']")
car.click()
time.sleep(3)

add_to_cart=driver.find_element(By.XPATH,"//button[@class='add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl']")
add_to_cart.click()
time.sleep(5)

print("1 new item(s) have been added to your cart")

go_to=driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(2)

delete=driver.find_element(By.XPATH,"//span[@class='lazada lazada-ic-Delete lazada-icon icon delete']").click()
time.sleep(2)

remove=driver.find_element(By.XPATH,"//button[@class='next-btn next-btn-primary next-btn-medium']").click()
time.sleep(2)

print("There are no items in this cart")

shop=driver.find_element(By.XPATH,"//button[@class='next-btn next-btn-secondary next-btn-large cart-empty-button']").click()
time.sleep(2)