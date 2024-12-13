from bs4 import BeautifulSoup
import requests
import io
content=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_y=content.text
soup=BeautifulSoup(web_y,"html.parser")
all_movies=soup.find_all(name="h3",class_="title")
for movie in range(len(all_movies)-1,-1,-1):
    res=all_movies[movie].getText()
    print(res)
    with io.open("movies.txt",mode='a',encoding="utf-8") as file:
        file.write(f"{res}\n")





