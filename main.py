import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def make_dir() -> None:
    dirs = [f'dataset/{i}' for i in range(1,6)]
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    for dir_name in dirs:
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)


def get_link_review(driver, links) -> str:
    driver.get("https://www.livelib.ru" + links.get("href"))
    sleep(2)
    soup_review = BeautifulSoup(driver.page_source, "lxml")
    return (soup_review.find("div", {"id": "lenta-card__text-review-full"}).text.strip() if soup_review.find("div", {
        "id": "lenta-card__text-review-full"}) else ' ')


def write_review(number: int, title: str, links: str, rating: int, driver) -> None:
    name_file = f'dataset/{rating}/{str(number).zfill(4)}.txt'
    with open(name_file, 'w', encoding="utf-8") as f:
        f.write(title.text.strip() + '\n' + get_link_review(driver, links))


def download_reviews():
    number_list = 1
    rating_review = [0] * 5
    driver = webdriver.Edge()
    driver.maximize_window()
    while rating_review[4] < 1001 or rating_review[3] < 1001 or rating_review[2] < 1001 or rating_review[1] < 1001 or rating_review[0] < 1001:
        URL = f"https://www.livelib.ru/reviews/~{number_list}#reviews"
        driver.get(URL)
        sleep(2)
        number_list += 1
        soup = BeautifulSoup(driver.page_source, "lxml")

        rating = soup.find_all("span", {"class": "lenta-card__mymark"})
        title = soup.find_all("a", "lenta-card__book-title")
        links = soup.find_all("a", {"class": "footer-card__link"})

        for i in range(len(rating) - 1):
            if float(rating[i].text) == 5.0 and rating_review[4] < 1001:
                rating_review[4] += 1
                write_review(rating_review[4], title[i], links[i], 5, driver)
            elif float(rating[i].text) == 4.0 and rating_review[3] < 1001:
                rating_review[3] += 1
                write_review(rating_review[3], title[i], links[i], 4, driver)
            elif float(rating[i].text) == 3.0 and rating_review[2] < 1001:
                rating_review[2] += 1
                write_review(rating_review[2], title[i], links[i], 3, driver)
            elif float(rating[i].text) == 2.0 and rating_review[1] < 1001:
                rating_review[1] += 1
                write_review(rating_review[1], title[i], links[i], 2, driver)
            elif float(rating[i].text) == 1.0 and rating_review[0] < 1001:
                rating_review[0] += 1
                write_review(rating_review[0], title[i], links[i], 1, driver)
                     
    driver.close()
    driver.quit()

def main():
    make_dir()
    download_reviews()
    
if __name__ == '__main__':
    main()
