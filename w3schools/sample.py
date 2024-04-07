import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="s33008814A",
    database = "imsalione",
)

mycursur = mydb.cursor()