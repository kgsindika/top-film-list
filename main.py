from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
all_h3_tags = soup.findAll(name="h3")

with open("mytextfile.txt", mode="w", encoding="utf-8") as the_textfile:
    for tag in reversed (all_h3_tags):
        the_textfile.write(tag.getText() + "\n")


