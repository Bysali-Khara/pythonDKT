import mysql.connector
mydb=mysql.connector.connect(
    host="local host",
    user= "root",
    password="",
    database="msit"
)
mycur=mydb.cursor()
mycur.execute("CREATE TABLE customers(id AUTO_INCREMENT PRIMARYKEY(11), name VARCHAR (255), address VARCHAR (255))")
print("created successfully")