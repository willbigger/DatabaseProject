'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector

def viewUserProfiles():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""

    print("User Profiles:")
    print("User ID    Email    First Name    Last Name    Favorite Actor    Favorite Director")
    
    #Gets all data from user_profile in increments of 50
    while cont != 'q':
        query = "SELECT * FROM user_profile ORDER BY userID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[0], end=": ")
            print(row[1], end=" ")
            print(row[2], end=" ")
            print(row[3], end=" ")
            print(row[4], end=" ")
            print(row[5], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def addUserProfile(email):
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    favoriteActor = input("Please enter your favorite actor: ")
    favoriteDirector = input("Please enter your favorite director: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    countQuery = "SELECT COUNT(*) FROM user_profile"
    cursor.execute(countQuery)
    
    #checks if table is empty
    if (cursor.fetchall()[0][0] == 0):
        newID = 1
    else:
        #calculates a new ID for the new entry
        lastIDQuery = "SELECT userID FROM user_profile ORDER BY userID DESC LIMIT 1"
        cursor.execute(lastIDQuery)
        newID = cursor.fetchall()[0][0] + 1
    
    print("Your user ID is: " + str(newID))
    
    #Adds movie
    insertQuery = "INSERT INTO user_profile (userID, email, firstName, lastName, favoriteActor, favoriteDirector) VALUES (%s, %s, %s, %s, %s, %s)"

    values = (newID, email, firstName, lastName, favoriteActor, favoriteDirector)
    cursor.execute(insertQuery, values)

    conn.commit()
    
    print("Welcome new user!")
    
    cursor.close()
    conn.close()

def deleteUserProfile():
    userID = input("Please enter your user ID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()
    
    #Deletes userID
    deleteQuery = "DELETE FROM user_profile WHERE userID = " + str(userID)
    cursor.execute(deleteQuery)
    conn.commit()
    
    print("User deleted!")
    
    cursor.close()
    conn.close()

def updateFavoriteActor():
    userID = input("Please enter your user ID: ")
    favoriteActor = input("Please enter your new favorite actor: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts genre
    query = "UPDATE user_profile SET favoriteActor = '" + favoriteActor + "' WHERE userID = " + str(userID)

    cursor.execute(query)

    conn.commit()
    
    print("Favorite actor updated!")
    
    cursor.close()
    conn.close()

def updateFavoriteDirector():
    userID = input("Please enter your user ID: ")
    favoriteDirector = input("Please enter your new favorite director: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts genre
    query = "UPDATE user_profile SET favoriteDirector = '" + favoriteDirector + "' WHERE userID = " + str(userID)

    cursor.execute(query)

    conn.commit()
    
    print("Favorite director updated!")
    
    cursor.close()
    conn.close()