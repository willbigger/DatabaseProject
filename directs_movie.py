'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
https://stackoverflow.com/questions/47873444/how-to-select-50-rows-everytime-from-mysql-table
'''
import mysql.connector

def viewDirectors():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""

    print("Directors:")
    print("Movie ID    First Name    Last Name")
    
    #Gets all data from directs_movie in increments of 50
    while cont != 'q':
        query = "SELECT * FROM directs_movie ORDER BY movieID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        table = cursor.fetchall()
        
        for row in table:
            print(row[0], end=": ")
            print(row[1], end=" ")
            print(row[2], end="\n")

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

'''
def addDirector():
    
    movieID = input("Please enter the movie ID: ")
    directorFirstName = input("Please enter the director's first name: ")
    directorLastName = input("Please enter the director's last name: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts director
    query = "INSERT INTO directs_movie (movieID, directorFirstName, directorLastName) VALUES (%s, %s, %s)"

    values = (movieID, directorFirstName, directorLastName)
    cursor.execute(query, values)

    conn.commit()
    
    print("New director added!")
    
    cursor.close()
    conn.close()
'''