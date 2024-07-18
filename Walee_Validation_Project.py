from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
Service_obj=Service("C:\chromedriver.exe")
driver=webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(50)

#  Color definations
green_color = "\033[92m"
reset_color = "\033[0m"
red_color = "\033[91m"
yellow_color = "\033[93m"


def LoginAskWalee():
    # login
    driver.get("https://staging.iir.walee.pk/auth/login")
    time.sleep(5)
    
    Title = driver.title
    print(f"Title of the webpage: {Title}")
    Email = driver.find_element(By.XPATH, "(//input[@placeholder='Email'])")
    Email.send_keys("jehanzaib.altaf@walee.pk")
    time.sleep(5)
    Password = driver.find_element(By.XPATH, "//input[@placeholder='*******']")
    Password.send_keys("Example@123")
    SignIn = driver.find_element(By.XPATH, "//button[@type='submit']")
    SignIn.click()
    time.sleep(3)    
    print(f"{green_color}Test Case passed: Logged in to Ask Walee successfully{reset_color}")
    time.sleep(5)


LoginAskWalee()

def MyNetwork():
    MyNetworkIcon = driver.find_element(By.XPATH, "//li[@routerlink='/im/my-network']//*[name()='svg']")
    MyNetworkIcon.click()
    time.sleep(3)
    NetworkValidationText = driver.find_element(By.XPATH, "//h2[normalize-space()='My Network']").text
    print(NetworkValidationText)
    OriginalNetworkValidationText = "My Network"
    if NetworkValidationText == OriginalNetworkValidationText:
        print(f"{green_color}My Network module displayed successfully{reset_color}")
    else:
        print(f"{red_color}My Network module display testcase failed :({reset_color}")
    time.sleep(5)
MyNetwork()

def Instagram_Validation ():

    MoreFilter=driver.find_element(By.XPATH,"//span[normalize-space()='More Filters']")
    MoreFilter.click()
    time.sleep(10)

    plateformButton=driver.find_element(By.XPATH,"//nz-collapse-panel[@nzheader='Platform']/div[1]")
    plateformButton.click()
    time.sleep(5)

    instagramShowResult=driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    instagramShowResult.click()
    time.sleep(5)

    src="https://staging.iir.walee.pk/assets/images/platforms/instagram.svg"
    websrc=driver.find_element(By.XPATH,"(//img[@alt='Platform'])[1]")
    websrc.click()

    attribute_value=websrc.get_attribute('src')
    print(attribute_value)
    time.sleep(7)

    if src==attribute_value:
        print(f"{green_color}instagram  displayed successfully{reset_color}")
    else:
        print(f"{red_color}instagram  display testcase failed :({reset_color}")
Instagram_Validation()

def youtubeValidation():
    AgainMoreFilter=driver.find_element(By.XPATH,"//span[normalize-space()='More Filters']")
    AgainMoreFilter.click()
    time.sleep(5)

    AgainplateformButton=driver.find_element(By.XPATH,"//nz-collapse-panel[@nzheader='Platform']/div[1]")
    AgainplateformButton.click()

    close=driver.find_element(By.XPATH,"//div[normalize-space()='Instagram']")
    close.click()
    time.sleep(5)

    uncheck=driver.find_element(By.XPATH,"(//div[normalize-space()='Instagram'])[2]")
    uncheck.click()
    time.sleep(5)

    search=driver.find_element(By.XPATH,"//div[normalize-space()='Youtube']")
    search.click()

    YoutubeShowResult=driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    YoutubeShowResult.click()

    Src="https://staging.iir.walee.pk/assets/images/platforms/youtube.svg"
    youtubelogo_path=driver.find_element(By.XPATH,"(//img[@src='./assets/images/platforms/youtube.svg'])[1]")
    youtubelogo_path.click()

    Youtube_value=youtubelogo_path.get_attribute('Src')
    print(Youtube_value)

    if Src==Youtube_value:
        print(f"{green_color}Youtube displayed successfully{reset_color}")
    else:
        print(f"{red_color}Youtube display testcase failed :({reset_color}")
youtubeValidation()
        
def TiktotValidation():
    Tiktok_MoreFilter=driver.find_element(By.XPATH,"//span[normalize-space()='More Filters']")
    Tiktok_MoreFilter.click()
    time.sleep(5)

    Tiktok_plateformButton=driver.find_element(By.XPATH,"//nz-collapse-panel[@nzheader='Platform']/div[1]")
    Tiktok_plateformButton.click()

    close=driver.find_element(By.XPATH,"//div[normalize-space()='Youtube']")
    close.click()
    time.sleep(5)

    desselect=driver.find_element(By.XPATH,"(//div[normalize-space()='Youtube'])[2]")
    desselect.click()
    time.sleep(5)

    Tiktok_search=driver.find_element(By.XPATH,"//div[normalize-space()='Tiktok']")
    Tiktok_search.click()

    TiktokShowResult=driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    TiktokShowResult.click()
    time.sleep(5)

    Src="https://staging.iir.walee.pk/assets/images/platforms/tiktok.svg"
    Tiktoklogo_path=driver.find_element(By.XPATH,"(//img[@src='./assets/images/platforms/tiktok.svg'])[1]")
    Tiktoklogo_path.click()

    Tiktok_value=Tiktoklogo_path.get_attribute('Src')
    print(Tiktok_value)
    time.sleep(5)
    if Src==Tiktok_value:
        print(f"{green_color}Tiktok displayed successfully{reset_color}")
    else:
        print(f"{red_color}Tiktok display testcase failed :({reset_color}")
TiktotValidation()