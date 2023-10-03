import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

URL = f"https://www.livelib.ru/reviews/search/rz;ow/~2#reviews" 

# ссылка номер отвечает за страницу
# html_page = requests.get(URL, headers)
# html_page.encoding = 'utf-8'
# src = html_page.text
# print(src)
def make_dir() -> None:
    dirs = ['dataset/1', 'dataset/2', 'dataset/3', 'dataset/4', 'dataset/5']
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)


driver = webdriver.Edge()
driver.maximize_window()

number_list=1
make_dir()
number_5 = 0
number_4 = 0
number_3 = 0
number_2 = 0
number_1 = 0
while number_5<1001 or number_4<1001 or number_1<1001 or number_2<1001 or number_3<1001:
    sleep(1)
    URL = f"https://www.livelib.ru/reviews/~{number_list}#reviews" 
    driver.get(URL)
    
    # ссылка номер отвечает за страницу
    number_list += 1
    # html_page.text - хранит html код веб-страницы
    soup = BeautifulSoup(driver.page_source, "lxml")

    rating = soup.find_all("span", {"class": "lenta-card__mymark"})
    title = soup.find_all("a", "lenta-card__book-title")
    review = soup.find_all("div", {"id": "lenta-card__text-review-escaped"})

    for i in range(len(rating)-1):
        if float(rating[i].text) == 5.0 and number_5 < 1001:
            number_5_1 = str(number_5 + 1).zfill(4)
            number_5 += 1
            name_file = f'dataset/5/{number_5_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
        elif float(rating[i].text) == 4.0 and number_4 < 1001:
            number_4_1 = str(number_4 + 1).zfill(4)
            number_4 += 1
            name_file = f'dataset/4/{number_4_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
        elif float(rating[i].text) == 3.0 and number_3 < 1001:
            number_3_1 = str(number_3 + 1).zfill(4)
            number_3 += 1
            name_file = f'dataset/3/{number_3_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
        elif float(rating[i].text) == 2.0 and number_2 < 1001:
            number_2_1 = str(number_2 + 1).zfill(4)
            number_2 += 1
            name_file = f'dataset/2/{number_2_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
        elif float(rating[i].text) == 1.0 and number_1 < 1001:
            number_1_1 = str(number_1 + 1).zfill(4)
            number_1 += 1
            name_file = f'dataset/1/{number_1_1}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + review[i].text.strip())
    