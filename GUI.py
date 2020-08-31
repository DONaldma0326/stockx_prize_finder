import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return"Hello!"




# conn = sqlite3.connect("stockx_tracker.db")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM SNEAKERS")
# print(cursor.fetchall())
# conn.commit()
# conn.close()


# search = requests.get(create_scraping_Url_news(names[0]), headers=headers)
# news_soup = BeautifulSoup(search.content, "html.parser")
# # find time,links,titles
# for i in news_soup.find_all("div", class_="wxp1Sb"):
#     if counter >= 5:
#         break
#     counter += 1
#     print(i.get_text())
#
# counter = 0
# for i in news_soup.find_all('a', href=True, style="text-decoration:none;display:block"):
#     if counter >= 5:
#         break
#     counter += 1
#     print(i["href"])
# counter = 0
# for i in news_soup.find_all("div", class_="JheGif nDgy9d"):
#     if counter >= 5:
#         break
#     counter += 1
#
#     print(i.get_text())
