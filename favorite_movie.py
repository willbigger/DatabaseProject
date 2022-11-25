'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector

def viewFavoriteMovies():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    userID = input("Please enter the user ID: ")

    cursor = conn.cursor()

    offset = 0

    cont = ""

    print("Favorite Movies:")
    
    #Gets all data from favorite_movie in increments of 50
    while cont != 'q':
        query = "SELECT * FROM favorite_movie WHERE userID = " + userID + " LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[1], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def addFavoriteMovies():
    userID = input("Please enter the user ID: ")
    movieID = input("Please enter the movieID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts movie
    query = "INSERT INTO favorite_movie (userID, movieID) VALUES (%s, %s)"

    values = (userID, movieID)
    cursor.execute(query, values)

    conn.commit()
    
    print("Favorite movie added!")
    
    cursor.close()
    conn.close()

def deleteFavoriteMovie():
    userID = input("Please enter the user ID: ")
    movieID = input("Please enter the movie ID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Deletes movie
    query = "DELETE FROM favorite_movie WHERE userID = '" + str(userID) + "' AND movieID = '" + str(movieID) + "'"

    cursor.execute(query)

    conn.commit()
    
    print("Favorite movie deleted!")
    
    cursor.close()
    conn.close()