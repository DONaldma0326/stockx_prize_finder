import requests
from bs4 import BeautifulSoup


# function for creating the google news scraping urls
def divided_name(symbol, name):
    name = name.lower()
    name = name.split(" ")
    s_name = ""
    for sub_name in name:
        s_name += sub_name + symbol
    # s_name.replace(s_name[-1], '')
    return s_name[:-1]


def create_scraping_Url_news(name):
    s_name = divided_name("+", name)

    url = f"https://www.google.com/search?q={s_name}&rlz=1C1CHBF_zh-TWHK913HK913&sxsrf=ALeKk00x15OsxYxkKhz-ZhxeXTJy-N7p6A:1598525921393&source=lnms&tbm=nws&sa=X&ved=2ahUKEwirxdWNnbvrAhUdyIsBHSLPAPcQ_AUoAnoECBYQBA&biw=1536&bih=754"
    return url


# function for creating the stock x scraping urls
# maybe make a dict that contain all the data that need to be deleted
def create_scraping_Url_stockx(name):
    s_name = divided_name("-", name)
    if "jordan" in s_name:
        s_name = "air-" + s_name
    if "denim" in s_name:
        s_name = s_name.replace("denim-", "")
    if s_name[-1] == ")":
        s_name = s_name.replace(s_name[-1], "")
        for i in reversed(s_name):
            if i == "(":
                s_name = s_name.replace(i, "")
                break
    url = f"https://stockx.com/{s_name}"
    return url


# find popular sneakers on stockx
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

# find detils on stockx
detail_URL = []
print(names)
for name in names:
    detail_URL.append(create_scraping_Url_stockx(name))
print(detail_URL)

"""
#find news
search = requests.get(create_scraping_Url_news(name), headers=headers)
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
    """
