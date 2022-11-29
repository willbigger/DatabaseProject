'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
https://stackoverflow.com/questions/47873444/how-to-select-50-rows-everytime-from-mysql-table
'''
import mysql.connector

def viewActors():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""

    print("Actors:")
    print("Movie ID    First Name    Last Name")
    
    #Gets all data from movie_actor in increments of 50
    while cont != 'q':
        query = "SELECT * FROM movie_actor ORDER BY movieID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[0], end=":    ")
            print(row[1], end=" ")
            print(row[2], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()
'''
def addActor():
    movieID = input("Please enter the movie ID: ")
    actorFirstName = input("Please enter the actor's first name: ")
    actorLastName = input("Please enter the actor's last name: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts actor
    query = "INSERT INTO movie_actor (movieID, actorFirstName, actorLastName) VALUES (%s, %s, %s)"

    values = (movieID, actorFirstName, actorLastName)
    cursor.execute(query, values)

    conn.commit()
    
    print("New actor added!")
    
    cursor.close()
    conn.close()
'''