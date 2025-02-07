import requests
import csv
import BeautifulSoup
context=requests.get('https://ethsat.com/').text
soup=BeautifulSoup(context,'html.parser')
body=soup.find("body")
head=body.find("nav")
lists=head.find_all('a')
amharic=requests.get(lists[1].get('href')).text

soup=BeautifulSoup(amharic,'html.parser')
body=soup.find("body")
head=body.find("nav")
lists=head.find_all('a')
news=[]
for i in lists:
  if i.text in ['AMHARIC','OROMIFFA','ENGLISH']:
    news.append(i.get('href'))
def content(url):
  contents=requests.get(url).text
  soup=BeautifulSoup(contents,'html.parser')
  body=soup.find("body")
  news=body.find(class_="entry")
  head=news.find_all('p')
  paragraphs = news.find_all('p')
  article_text = "\n".join([p.text.strip() for p in paragraphs])
  print(article_text)
with open ("amharic_news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Link"])
    pages=1
    while True:
      url =f"{news[0]}/page/{pages}"
      if requests.get(url).status_code!=200 :
        print("Not Found")
        break
      amharic_news=requests.get(url)
      soup=BeautifulSoup(amharic_news.text,'html.parser')
      body=soup.find('body')
      articles=body.find(class_='post-listing')
      h2=articles.find_all('h2')
      for i in h2:


        head_line=i.text
        link=i.find('a')['href']
        writer.writerow([head_line, link])

        #content(p)
      pages+=1
