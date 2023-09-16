import os
from time import sleep
from bs4 import BeautifulSoup
import requests

headers ={
    "Accept" : "*/*",
    "User-Agent" : "Mozilla/5.0"
}

def make_dir() -> None:
    dirs = ['dataset/1', 'dataset/2', 'dataset/3', 'dataset/4', 'dataset/5']
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

number_list=1
make_dir()
number_5 = 0
number_4 = 0
while number_5<1001 and number_4<1001:
    sleep(4*number_list)
    print(number_list)
    URL = f"https://www.livelib.ru/reviews/search/rp;ow/~{number_list}#reviews" 
    
    # ссылка номер отвечает за страницу
    html_page = requests.get(URL, headers)
    html_page.encoding = 'utf-8'
    src = html_page.text
    number_list += 1
    # html_page.text - хранит html код веб-страницы
    soup = BeautifulSoup(src, "lxml")

    rating = soup.find_all("span", {"class": "lenta-card__mymark"})
    title = soup.find_all("a", "lenta-card__book-title")
    review = soup.find_all("div", {"id": "lenta-card__text-review-escaped"})

    for i in range(len(rating)-1):
        if float(rating[i].text) == 5.0 and number_5 < 1000:
            number_5_1 = str(number_5 + 1).zfill(4)
            number_5 += 1
            name_file = f'dataset/5/{number_5_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
        if float(rating[i].text) == 4.0 and number_4 < 1000:
            number_4_1 = str(number_4 + 1).zfill(4)
            number_4 += 1
            name_file = f'dataset/4/{number_4_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())