from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
drive=webdriver.Chrome(options=option)
drive.get("https://en.wikipedia.org/wiki/Main_Page")
#res=drive.find_element(By.CSS_SELECTOR,value="#articlecount a")
search=drive.find_element(By.CSS_SELECTOR,value="#p-search a")
search.click()
f=drive.find_element(By.NAME,value="search")
print(f.text)
drive.quit()