import requests
from bs4 import BeautifulSoup

URL = "https://stockx.com/air-jordan-12-retro-stone-blue"
headers = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# product name
name_tag = soup.find("div", class_="mobile-name only-mobile").getText()
print(name_tag)
