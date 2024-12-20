from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_option=webdriver.ChromeOptions()
gmail="my_own_email"
password="my_own_password"
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(chrome_option)
driver.get("https://www.linkedin.com/login")
time.sleep(3)
my_gmail=driver.find_element(By.ID,value="username")
my_password=driver.find_element(By.ID,value="password")
my_gmail.send_keys(gmail)
my_password.send_keys(password)
sign_up=driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
sign_up.click()
time.sleep(20)
job=driver.find_element(By.XPATH,value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job.click()
time.sleep(10)
skill= driver.find_element(By.XPATH, value="//*[starts-with(@id, 'jobs-search-box-keyword-id-ember')]")
skill.send_keys("Deep learningEngineer")
location=driver.find_element(By.XPATH,value='//*[starts-with(@id,"jobs-search-box-location-id-ember")]')
location.clear()
location.send_keys("Addis Ababa, Ethiopia",Keys.ENTER)
time.sleep(5)
apply=driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")

apply.click()
time.sleep(5)
phone_number=driver.find_element(By.CLASS_NAME,value="artdeco-text-input--input")
phone_number.send_keys("0912212927")
time.sleep(3)
next=driver.find_element(By.CLASS_NAME,value="artdeco-button--primary")
next.click()
next_=driver.find_element(By.CLASS_NAME,value="artdeco-button--primary")

next_.click()
time.sleep(10)
yes=driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4091902143-7038908801-multipleChoice"]/div[2]/label')
yes.click()
python_expriance=driver.find_element(By.ID,value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4091902143-7038908785-numeric")

python_expriance.send_keys("1")
java_expriance=driver.find_element(By.ID,value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4091902143-7038908793-numeric")

java_expriance.send_keys("1")
time.sleep(5)
span_element = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
span_element.click()
submit=driver.find_element(By.CLASS_NAME,value="artdeco-button__text")
submit.click()






































































































































































