from bs4 import BeautifulSoup
import requests
from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# Load environment variables from the .env file
load_dotenv()

# Get sensitive data from environment variables
my_gmail = os.environ.get("gmail")
my_password = os.environ.get("password")
send_to = os.environ.get("received")
my_smtp = os.environ.get("smtp")

# Target price for the item
target = 100.0

# URL to check the price
#url = "https://appbrewery.github.io/instant_pot/"
headers={
"Accept-Language":"en-US,en;q=0.9",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
# Request the page content
res = requests.get(url=url,headers=headers)
content = res.text
soup = BeautifulSoup(content, "html.parser")

# Extract the price from the page
price_tag = soup.find(name="span", class_="a-offscreen")
price = float(price_tag.getText().strip().split('$')[1])
product_title=soup.find(id="productTitle").getText().strip()
message=f"{product_title} is on a sale for {price}"
# Check if the price is below the target
if price < target:
    with SMTP_SSL(my_smtp, port=465) as connection:
        connection.login(user=my_gmail, password=my_password)

        connection.sendmail(from_addr=my_gmail, to_addrs=send_to, msg=f"subject: Amazon Price Alert\n\n{message}{url}".encode("utf-8"))

