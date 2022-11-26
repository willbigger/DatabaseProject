'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector

def viewAuthors():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""

    print("Review Authors:")
    print("user ID    Review ID")
    #Gets all data from authored_by in increments of 50
    while cont != 'q':
        query = "SELECT * FROM authored_by LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[0], end=": ")
            print(row[1], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def deleteAuthor(email):
    reviewID = input("Please enter the review ID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]
    
    #Deletes movie
    query = "DELETE FROM authored_by WHERE userID = '" + str(userID) + "' AND reviewID = '" + str(reviewID) + "'"

    cursor.execute(query)

    conn.commit()
    
    print("Author deleted!")
    
    cursor.close()
    conn.close()