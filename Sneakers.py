import requests
from bs4 import BeautifulSoup

class Sneakers:
    code = 0
    headers = {
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    def __init__(self, name):
        Sneakers.code += 1
        self.code = Sneakers.code
        self.name = str(name).lower()

        self.google_url = self.create_scraping_Url_news()
        self.info_url = self.create_scraping_Url_stockx()
        self.info_soup = self.create_soup(self.info_url)

        self.bid = self.get_bid(self.info_soup)
        self.ask = self.get_ask(self.info_soup)
        self.last_sale = self.get_last_sale(self.info_soup)

    def create_soup(self, url):
        page = requests.get(url, headers=Sneakers.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def divided_name(self, symbol):

        name = self.name.split(" ")
        s_name = ""
        for sub_name in name:
            s_name += sub_name + symbol
        # s_name.replace(s_name[-1], '')
        return s_name[:-1]

    # function for creating the google news scraping urls
    def create_scraping_Url_news(self):
        s_name = self.divided_name("+")

        url = f"https://www.google.com/search?q={s_name}&rlz=1C1CHBF_zh-TWHK913HK913&sxsrf=ALeKk00x15OsxYxkKhz-ZhxeXTJy-N7p6A:1598525921393&source=lnms&tbm=nws&sa=X&ved=2ahUKEwirxdWNnbvrAhUdyIsBHSLPAPcQ_AUoAnoECBYQBA&biw=1536&bih=754"

        return url

    # function for creating the stock x scraping urls
    # maybe make a dict that contain all the data that need to be deleted
    def create_scraping_Url_stockx(self):
        s_name = self.divided_name("-")
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

    def get_ask(self,soup):
        try:
            prizes = soup.find_all("div", class_="stats")
            return prizes[0].get_text()

        except:
            return None

    def get_bid(self,soup):
        try:
            prizes = soup.find_all("div", class_="stats")
            return prizes[1].get_text()

        except:
            return None

    def get_last_sale(self,soup):
        try:
            last_sale = soup.find("div", class_="last-sale")
            return last_sale.get_text()
        except:
            return None
#clean data find the number of bid and ask and make them integer