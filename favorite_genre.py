'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector

def viewFavoriteGenres(email):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    offset = 0

    cont = ""

    print("Favorite Genres:")
    
    #Gets all data from favorite_genre in increments of 50
    while cont != 'q':
        query = "SELECT * FROM favorite_genre WHERE userID = " + userID + " LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[1], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def addFavoriteGenres(email):
    genreName = input("Please enter the genre: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    #Inserts genre
    query = "INSERT INTO favorite_genre (userID, genreName) VALUES (%s, %s)"

    values = (userID, genreName)
    cursor.execute(query, values)

    conn.commit()
    
    print("Favorite genre added!")
    
    cursor.close()
    conn.close()

def deleteFavoriteGenre(email):
    genreName = input("Please enter the genre: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    #Deletes genre
    query = "DELETE FROM favorite_genre WHERE userID = '" + str(userID) + "' AND genreName = '" + str(genreName) + "'"

    cursor.execute(query)

    conn.commit()
    
    print("Favorite genre deleted!")
    
    cursor.close()
    conn.close()