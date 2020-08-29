import sqlite3
import requests
from bs4 import BeautifulSoup
import Sneakers

# soup set up
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
    if counter > 10:
        break
    counter += 1

# sneakers setuo
sneakers = []
for i in names:
    x = Sneakers.Sneakers(i)
    sneakers.append(x)

# database setup
conn = sqlite3.connect("stockx_tracker.db")
cursor = conn.cursor()

#insert value
cursor.execute("SELECT * FROM SNEAKERS")
exist = cursor.fetchall()
check_exist = sneakers[len(sneakers)-1].code
for sneaker in sneakers:
        try:
            if sneaker.code <= check_exist:
                print("value already there")
                cursor.execute("""UPDATE SNEAKERS SET name =?,bid =?,ask=?last_sale=? WHERE
                                CODE = ?;""",(sneaker.name, sneaker.bid, sneaker.ask, sneaker.last_sale, sneaker.code))
            else:
                cursor.execute("""INSERT INTO SNEAKERS (code, name, bid, ask, last_sale)
                VALUES (?,?,?,?,?);""", (sneaker.code, sneaker.name, sneaker.bid, sneaker.ask, sneaker.last_sale))
        except:
            print("the url is none")


cursor.execute("SELECT * FROM SNEAKERS")
print(cursor.fetchall())

conn.commit()
conn.close()
