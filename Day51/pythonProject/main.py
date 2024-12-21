from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
import time
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(chrome_options)
PROMISED_UP=10
PROMISED_DOWN=150
SPEED="https://www.speedtest.net/"

X='gmail'
USER_NAME='username'
password='password'
x_link="https://twitter.com/login"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.up =0
        self.down =0
    def get_internet_speed(self):
        driver.get(SPEED)
        go = driver.find_element(By.XPATH,
        value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(100)
        self.down = driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        driver.get(x_link)
        time.sleep(10)
        email=driver.find_element(By.NAME,value='text')
        email.send_keys(X)
        email.send_keys(Keys.ENTER)
        time.sleep(10)
        user=driver.find_element(By.NAME,value='text')
        user.send_keys(USER_NAME)
        user.send_keys(Keys.ENTER)
        time.sleep(10)
        pass_=driver.find_element(By.NAME,value='password')
        pass_.send_keys(password)
        pass_.send_keys(Keys.ENTER)
        time.sleep(10)
        name=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        message=f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        name.send_keys(message)
        post=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()
commit=InternetSpeedTwitterBot()
commit.get_internet_speed()
commit.tweet_at_provider()
