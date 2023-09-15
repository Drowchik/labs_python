import os
from bs4 import BeautifulSoup
import requests

number_list = 2
URL = f"https://www.livelib.ru/reviews/~{number_list}#reviews" #ссылка номер отвечает за страницу
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
html_page.encoding = 'utf-8'
src=html_page.text
# html_page.text - хранит html код веб-страницы
soup = BeautifulSoup(src, "lxml")

rating = soup.find_all("span", {"class":"lenta-card__mymark"})
title = soup.find_all("a", "lenta-card__book-title")
review = soup.find_all("div", {"id":"lenta-card__text-review-escaped"})

for i in range(len(rating)):
    if float(rating[i].text) == 5:
        print(title[i].text.strip())
    
def make_dir():
    dirs = ['dataset/1', 'dataset/2', 'dataset/3', 'dataset/4', 'dataset/5']
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
#     print(key.text.strip())
    
# for key in review:
#     print(key.text)

     
