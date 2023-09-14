import os
from bs4 import BeautifulSoup
import requests

URL = "https://www.livelib.ru/reviews/~2#reviews"
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
src=html_page.text
# html_page.text - хранит html код веб-страницы

soup = BeautifulSoup(src, "lxml")
print(soup)
title = soup.find("div", class_="lenta-card__mymark")
print(title)
     