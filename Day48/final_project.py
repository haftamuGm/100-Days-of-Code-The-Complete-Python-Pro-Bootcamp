from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")


all_id=[i.get_attribute("id") for i in driver.find_elements(By.CSS_SELECTOR,value="#store div")]
timeout = time.time() + 5
five_min = time.time() + 60*1  # 5 minutes

while True:
    cookie.click()
    if time.time()>timeout:
        all_price=[]
        all = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for i in all:
            if i.text!="":
                all_price.append(int(i.text.split('-')[1].strip().replace(",","")))
        money=driver.find_element(By.ID,value="money").text
        if ',' in money:
            money.replace(",","")
        money=int(money)
        cookies_upgrade={}
        affordable_cokies={}
        for j in range(len(all_price)):
            cookies_upgrade[all_price[j]]=all_id[j]
        for cost,id in cookies_upgrade.items():
            if money>cost:
                affordable_cokies[cost]=id
        p=max(affordable_cokies)
        purchase_item=affordable_cokies[p]
        driver.find_element(By.ID,value=purchase_item).click()
        timeout=time.time()+5
    if time.time()>five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
driver.quit()


