from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object=Service("C:\chromedriver.exe")
driver=webdriver.Chrome(service=service_object)
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=1653377901&extra_1=s%7Cc%7C318305677163%7Ce%7Cfacebook%20login%7C&placement=&creative=318305677163&keyword=facebook%20login&partner_id=googlesem&extra_2=campaignid%3D1653377901%26adgroupid%3D65139787642%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1409285535%26loc_physical_ms%3D1011086%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAiA0syqBhBxEiwAeNx9N7Emrz0exH2Q6odWvfiO1XomW5SBF1bJ4dP_f3gXDg9gOq_ox73RGRoCM2YQAvD_BwE")
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Younas")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Khan")
driver.find_element(By.XPATH,"//input[@name='reg_email__']").send_keys("younassolution95@gmail.com")
driver.find_element(By.XPATH,"//input[@autocomplete='new-password']").send_keys("12345678")
driver.find_element(By.XPATH,"//option[@value='31']").click()
driver.find_element(By.XPATH,"//input[@type='radio']").click()
# driver.find_element(By.XPATH,"//select[@id='year']").send_keys("2024")
# driver.find_element(By.TAG_NAME,'Male').click()
time.sleep(20)
