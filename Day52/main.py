
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
chrome_options = webdriver.ChromeOptions()
INSTAGRAM="https://www.instagram.com/"
USERNAME="email"
PASSWORD="password"
class InstaFollower:
    def __init__(self):
        chrome_options.add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(chrome_options)
    def login(self):
        self.driver.get(INSTAGRAM)
        time.sleep(3)
        self.driver.find_element(By.NAME,value='username').send_keys(USERNAME)
        self.driver.find_element(By.NAME,value='password').send_keys(PASSWORD)
        self.driver.find_element(By.NAME, value='password').send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]").click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(5.2)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,value='followers').click()
        time.sleep(10)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        all_button=self.driver.find_elements(By.XPATH,value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[84]/div/div/div/div[3]/div/button')
        for button in all_button:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
auth_follower=InstaFollower()
auth_follower.login()
auth_follower.find_followers()
auth_follower.follow()
