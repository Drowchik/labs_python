import os
from bs4 import BeautifulSoup
import requests

URL = "https://www.livelib.ru/reviews/~2#reviews"
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
html_page.encoding = 'utf-8'
src=html_page.text
# html_page.text - хранит html код веб-страницы

soup = BeautifulSoup(src, "lxml")

rating = soup.find_all("span", {"class":"lenta-card__mymark"})
title = soup.find_all("div", {"id":"lenta-card__text-review-escaped"})

for key in rating:
    print(float(key.text))
    
# for key in title:
#     print(key.text)

     
