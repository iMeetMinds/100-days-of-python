from bs4 import BeautifulSoup
import requests

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}/")
response.raise_for_status()
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")

titles = soup.find_all(name='h3', id='title-of-a-story')
title = [n for n in titles]
print(title)
