from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "my_email"
ACCOUNT_PASSWORD = "my_password"
PHONE = "0912213443"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)
time.sleep(3)
x=driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/button')
x.click()
time.sleep(3)
sign_in=driver.find_element(By.XPATH,value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
time.sleep(3)
username=driver.find_element(By.ID,value="username")
username.send_keys(ACCOUNT_EMAIL)
time.sleep(3)
password=driver.find_element(By.ID,value="password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(40)
apply=driver.find_element(By.CSS_SELECTOR,value=".jobs-s-apply button")
apply.click()
phone=driver.find_element(By.CLASS_NAME,value="artdeco-text-input--input")
phone.send_keys(PHONE)
time.sleep(10)
next=driver.find_element(By.CLASS_NAME,value="artdeco-button--primary")
next.click()
next_=driver.find_element(By.CLASS_NAME,value="artdeco-button--primary")
next_.click()
time.sleep(3)
legal_authorize=driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4105589364-11393393730-multipleChoice"]/div[1]/label')
legal_authorize.click()
working_remote=driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4105589364-11393393714-multipleChoice"]/div[1]/label')
working_remote.click()
visa_status=driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4105589364-11393393770-multipleChoice"]/div[1]/label')
visa_status.click()
select=driver.find_element(By.XPATH,value='//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4105589364-11393393754-multipleChoice"]/option[2]')
select.click()
next_to=driver.find_element(By.CLASS_NAME,value='artdeco-button--primary')
next_to.click()
yes=driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4105589364-11393393762-multipleChoice"]/div[1]/label')
yes.click()
review=driver.find_element(By.CLASS_NAME,value='artdeco-button--primary')
review.click()
