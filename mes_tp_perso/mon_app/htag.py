import pymysql

age= int(input("enter your age\n"))
name= str(input("your name"))
 
data = pymysql.connect(host="localhost", user="root", database="sephora")
cur=data.cursor()
cur.execute("insert into phacochere(nom, age) values(%s, %s)", (name ,age))
cur1=data.cursor()
cur1.execute("select * from phacochere where nom=%s and age=%s", (name, age))
row=cur1.fetchone()[0]
data.commit()
data.close()
print(row)