from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome options
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=option)

# Open the Python.org website
driver.get("https://www.python.org")

# Find elements for event dates and names
time_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
name_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# Create a dictionary with event data
res = {i: {"name": name_elements[i].text, "time": time_elements[i].text} for i in range(len(time_elements))}

# Print the result
print(res)

# Quit the driver
driver.quit()
