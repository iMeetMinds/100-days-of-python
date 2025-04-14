from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
response.raise_for_status()
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
for title in titles[::-1]:
    # print(title.getText())
    with open("movies.txt", 'a', encoding="utf-8") as file:
        file.write(f"{title.getText()}\n")


