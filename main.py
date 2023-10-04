import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def make_dir() -> None:
    dirs = ['dataset/1', 'dataset/2', 'dataset/3', 'dataset/4', 'dataset/5']
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

def get_link_review(index, links):
    driver.get("https://www.livelib.ru"+links[index].get("href"))
    sleep(2)
    soup_review = BeautifulSoup(driver.page_source, "lxml")
    return (soup_review.find("div",{"id": "lenta-card__text-review-full"}).text.strip() if soup_review.find("div",{"id": "lenta-card__text-review-full"}) else ' ')


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
    URL = f"https://www.livelib.ru/reviews/~{number_list}#reviews"
    print(number_list, '- страничка') 
    driver.get(URL)
    sleep(2)
    
    number_list += 1
    soup = BeautifulSoup(driver.page_source, "lxml")

    rating = soup.find_all("span", {"class": "lenta-card__mymark"})
    title = soup.find_all("a", "lenta-card__book-title")
    links = soup.find_all("a", {"class": "footer-card__link"})
    
    for i in range(len(rating)-1):
        if float(rating[i].text) == 5.0 and number_5 < 1001:
            number_5 += 1
            name_file = f'dataset/5/{str(number_5).zfill(4)}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + get_link_review(i, links))
        elif float(rating[i].text) == 4.0 and number_4 < 1001:
            number_4 += 1
            name_file = f'dataset/4/{str(number_4).zfill(4)}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + get_link_review(i, links))
        elif float(rating[i].text) == 3.0 and number_3 < 1001:
            number_3 += 1
            name_file = f'dataset/3/{str(number_3).zfill(4)}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + get_link_review(i, links))
        elif float(rating[i].text) == 2.0 and number_2 < 1001:
            number_2 += 1
            name_file = f'dataset/2/{str(number_2).zfill(4)}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + get_link_review(i, links))
        elif float(rating[i].text) == 1.0 and number_1 < 1001:
            number_1 += 1
            name_file = f'dataset/1/{str(number_1).zfill(4)}.txt'
            with open(name_file, 'w', encoding="utf-8") as f:
                f.write(title[i].text.strip() + '\n' + get_link_review(i, links))

driver.quit()
driver.close()
