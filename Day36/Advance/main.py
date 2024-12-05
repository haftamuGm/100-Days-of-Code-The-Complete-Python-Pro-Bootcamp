import requests
from twilio.rest import Client
account_sid = 'ACd92151af03bcf3d5a2500184102e4d28'
auth_token = '597662aada2ef7d8504c5626c46d8b4a'
MY_STOCK_API= "BK8PYSYN2S7S0EAY"
MY_STOCK_NEWS_API="aa6c79bb00f642da93e2326abff7db46"
url="https://www.alphavantage.co/query"
my_news_url="https://newsapi.org/v2/everything"

parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":MY_STOCK_API,
    "outputsize":"compact",
    #"datatype":"csv",
}
parameterr ={
    "q":"tesla",
    "from": "2024-12-03",
    "to":"2024-12-04",
    "language":"en",
    "sortBy":"publishedAt",
    "apikey":MY_STOCK_NEWS_API

}
result=requests.get(url,params=parameter)
data=requests.get(my_news_url,params=parameterr)
title=data.json()['articles'][0]['title']
describe=data.json()['articles'][0]['description']
today=result.json()['Time Series (Daily)']['2024-12-04']['4. close']
yesterday=result.json()['Time Series (Daily)']['2024-12-03']['4. close']
print(today)
print(yesterday)

percent=((float(today)-float(yesterday))*100)//float(today)

if percent:
    percent=f"🔺{percent}%"
else:
    percent = f"🔻{percent*-1}%"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=percent,
  from_='+17752589981',
  to='+251953485998'
)

print(message.sid)

