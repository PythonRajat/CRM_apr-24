import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin@123'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE Customer")

print("All Done!")