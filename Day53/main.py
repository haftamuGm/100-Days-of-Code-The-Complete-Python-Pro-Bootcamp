from bs4 import BeautifulSoup
from fill_form import Form

ADDRESS='https://appbrewery.github.io/Zillow-Clone/'
import requests
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
content=response.text
soup=BeautifulSoup(content,"html.parser")
all_link=[i.get("href") for i in soup.select(".StyledPropertyCardDataWrapper a")]
all_price=[price.text.split('+')[0] for  price in soup.select(".StyledPropertyCardDataWrapper span")]
all_address=[i.text.strip().replace('|',' ') for i in soup.select(".StyledPropertyCardDataWrapper address")]
print(all_address)
form=Form()
form.fill_form(all_address,all_price,all_link)


