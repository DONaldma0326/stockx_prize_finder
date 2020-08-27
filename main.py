import requests
from bs4 import BeautifulSoup
#find popular sneakers on stockx
URL = "https://stockx.com/sneakers/most-popular"
headers = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
counter = 0
# find sneaker's name
divs = soup.find_all("div", class_="css-1tky8yn e1inh05x0")
names = []
for i in divs:
    names.append(i.get_text())
for name in names:
    name = name.split(" ")
# set search_name
search_name = ""

for sub_name in name:
    search_name += sub_name + "+"
search_name.replace(search_name[-1], '')
print(search_name)
search_url = f"https://www.google.com/search?q={search_name}&rlz=1C1CHBF_zh-TWHK913HK913&sxsrf=ALeKk00x15OsxYxkKhz-ZhxeXTJy-N7p6A:1598525921393&source=lnms&tbm=nws&sa=X&ved=2ahUKEwirxdWNnbvrAhUdyIsBHSLPAPcQ_AUoAnoECBYQBA&biw=1536&bih=754"
search = requests.get(search_url, headers=headers)
news_soup = BeautifulSoup(search.content, "html.parser")
# find time,links,titles
for i in news_soup.find_all("div", class_="wxp1Sb"):
    if counter >= 5:
        break
    counter += 1
    print(i.get_text())

counter = 0
for i in news_soup.find_all('a', href=True, style="text-decoration:none;display:block"):
    if counter >= 5:
        break
    counter += 1
    print(i["href"])
counter = 0
for i in news_soup.find_all("div", class_="JheGif nDgy9d"):
    if counter >= 5:
        break
    counter += 1

    print(i.get_text())
