#Inspired by https://realpython.com/python-mysql and https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python

import mysql.connector

def viewGenre():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Gets all data from genre
    query = "SELECT * from genre"
    cursor.execute(query)
    
    table = cursor.fetchall()
    
    print("Movie genres:")
    for row in table:
        print(row[0], end=": ")
        print(row[1], end="\n")

    cursor.close()
    conn.close()

#https://www.w3schools.com/python/python_mysql_insert.asp
def addGenre():
    genreName = input("Please enter the genre name: ")
    description = input("Please enter the genre description: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Gets all data from genre
    query = "INSERT INTO genre (genreName, description) VALUES (%s, %s)"

    values = (genreName, description)
    cursor.execute(query, values)

    conn.commit()
    
    print("New genre added!")
    
    cursor.close()
    conn.close()