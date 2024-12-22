from selenium import webdriver
import time
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
class Form:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLScHmN417_3Fjs6wxeAtSklnyK7v7wIPVoTyiXuTMKEbPd-L_g/viewform')
        self.address='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.price_per_month='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.link_to_property='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.submit='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        self.submit_again='/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
    def fill_form(self,all_adress,all_price,all_link_to_property):
        time.sleep(2)
        for i in range(len(all_adress)):
            each_adress=self.driver.find_element(By.XPATH,self.address)
            each_adress.send_keys(all_adress[i])
            time.sleep(2)
            each_price=self.driver.find_element(By.XPATH,value=self.price_per_month)
            each_price.send_keys(all_price[i])
            time.sleep(2)
            each_link_to_pro=self.driver.find_element(By.XPATH,value=self.link_to_property)
            each_link_to_pro.send_keys(all_link_to_property[i])
            time.sleep(2)
            self.driver.find_element(By.XPATH,self.submit).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,self.submit_again).click()
