import sqlite3


con = sqlite3.connect(r"C:\examples\Day4\01_DataBase\test.db")
cur = con.cursor()
#cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
#cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-1234');")
#cur.execute("INSERT INTO PhoneBook VALUES('Derick3', '010-5678-1234');")
#con.commit()

cur.execute("SELECT * FROM PhoneBook")

for i in con.iterdump():
    print(i)

con.close()


