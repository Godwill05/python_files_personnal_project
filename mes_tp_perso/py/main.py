import pymysql

con = pymysql.connect(host="localhost", user="root")
cur = con.cursor()
cur.execute("create databse new_projects;")
cur.fetchone()
con.close()