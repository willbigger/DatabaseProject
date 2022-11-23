import mysql.connector

#Inspired by https://realpython.com/python-mysql and https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "movie_database")

cursor = conn.cursor()

#Gets the column information from movie_genre
query1 = "desc movie_genre"
cursor.execute(query1)
query1Fetch = cursor.fetchall()
print('\n Table Description:')
for attributes in query1Fetch:
    print(attributes)