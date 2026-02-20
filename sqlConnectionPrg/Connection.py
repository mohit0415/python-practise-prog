import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="empover#1",database="practdata")

myCursor = mydb.cursor()

