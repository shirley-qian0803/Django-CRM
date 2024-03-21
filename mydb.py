import mysql.connector

dataBase = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = 'shirley050803'
	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE hahaco")

print("All Done!")