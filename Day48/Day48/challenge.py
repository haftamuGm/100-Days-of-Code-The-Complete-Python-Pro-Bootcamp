from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
option_chrome=webdriver.ChromeOptions()
option_chrome.add_experimental_option("detach",True)
driver=webdriver.Chrome(option_chrome)
driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name=driver.find_element(By.NAME,value="fName")
l_name=driver.find_element(By.NAME,value="lName")
email_=driver.find_element(By.NAME,value="email")
f_name.send_keys("Haftamu")
l_name.send_keys("G/Maryam")
email_.send_keys("haftamu7@gmail.com")
sign_up=driver.find_element(By.CSS_SELECTOR,value="form button")
sign_up.click()



driver.quit()