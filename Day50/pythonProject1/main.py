from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

my_phone_number = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com")
time.sleep(5)

# Click on the login button
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()
time.sleep(10)

# Click on the Google login button
google_button = driver.find_element(By.XPATH, value='//*[@id="q369688754"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
google_button.click()
time.sleep(5)
main_window = driver.window_handles[0]
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)
email = driver.find_element(By.ID, value='email')
email.send_keys(my_phone_number)

password = driver.find_element(By.ID, value='pass')
password.send_keys('password')
password.send_keys(Keys.ENTER)
driver.switch_to.window(main_window)
time.sleep(80)
driver.switch_to.window(login_window)
login=driver.find_element(By.XPATH,value='//*[@id="q369688754"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login.click()
con=driver.find_element(By.XPATH,value='//*[@id="mount_0_0_FV"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]')
con.click()
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
