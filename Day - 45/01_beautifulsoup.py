from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
html_file = response.text

soup = BeautifulSoup(html_file, 'html.parser')

whole_lists = soup.select(selector="tr.athing.submission")
sub_lines = soup.select(selector="span.subline span.score")
# print(whole_lists)
for whole_list in whole_lists:
    time_line = whole_list.select_one(selector="span.titleline a[href^='https://']")
    name_value = time_line.getText()
    href_value = time_line.get('href')
    print(f"name_value =>{name_value}")
    print(f"href_value =>{href_value}")


for sub_line in sub_lines:
    score_value = sub_line.getText()
    print(f"score_value =>{score_value}")



















# with open("website.html") as content:
#     file_data = content.read()
#
# soup = BeautifulSoup(file_data, 'html.parser')
