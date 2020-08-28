import sqlite3

connection = sqlite3.connect("StockX_Tracker.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE shoes(
    names text,
    sell real,
    bid real
 )""")
#text,real,real
connection.commit()
connection.close()
