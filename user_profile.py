'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector
import matrixView

def viewUserProfiles():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""
    
    #Gets all data from user_profile in increments of 50
    while cont != 'q':
        query = "SELECT * FROM user_profile ORDER BY userID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)

        user_list = [["User ID", "Email", "First Name", "Last Name", "Favorite Actor", "Favorite Director"]]
        user_list += cursor.fetchall()
        
        matrixView.clean_print(user_list)
        
        # table = cursor.fetchall()
        
        # for row in table:
        #     print(row[0], end=": ")
        #     print(row[1], end=" ")
        #     print(row[2], end=" ")
        #     print(row[3], end=" ")
        #     print(row[4], end=" ")
        #     print(row[5], end="\n")

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

def deleteUserProfile(email):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    #Deletes author
    deleteQuery = "DELETE FROM authored_by WHERE userID = " + str(userID)
    cursor.execute(deleteQuery)
    conn.commit()

    #Deletes favorite genre
    deleteQuery = "DELETE FROM favorite_genre WHERE userID = " + str(userID)
    cursor.execute(deleteQuery)
    conn.commit()

    #Deletes favorite movie
    deleteQuery = "DELETE FROM favorite_movie WHERE userID = " + str(userID)
    cursor.execute(deleteQuery)
    conn.commit()

    #Deletes profile
    deleteQuery = "DELETE FROM user_profile WHERE userID = " + str(userID)
    cursor.execute(deleteQuery)
    conn.commit()

    #Deletes email
    deleteQuery = "DELETE FROM user_passwords WHERE email = '" + str(email) + "'"
    cursor.execute(deleteQuery)
    conn.commit()
    
    print("User deleted!")
    
    cursor.close()
    conn.close()

def updateFavoriteActor(email):
    favoriteActor = input("Please enter your new favorite actor: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]


    #Updates favorite actor
    query = "UPDATE user_profile SET favoriteActor = '" + favoriteActor + "' WHERE userID = " + str(userID)

    cursor.execute(query)

    conn.commit()
    
    print("Favorite actor updated!")
    
    cursor.close()
    conn.close()

def updateFavoriteDirector(email):
    favoriteDirector = input("Please enter your new favorite director: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    #Updates favorite director
    query = "UPDATE user_profile SET favoriteDirector = '" + favoriteDirector + "' WHERE userID = " + str(userID)

    cursor.execute(query)

    conn.commit()
    
    print("Favorite director updated!")
    
    cursor.close()
    conn.close()