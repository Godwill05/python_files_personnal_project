import sqlite3
connectio = sqlite3.connect("./db.sqlite3")

cursor= connectio.cursor()

new_user = (cursor.lastrowid, "Julie", "4sd", "xwdc", 23)
cursor.execute('INSERT INTO user VALUES(?, ?, ?, ?, ?)', new_user)
connectio.commit()

connectio.close()