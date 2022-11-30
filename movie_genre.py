'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector
import matrixView

def viewMovieGenres():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""
    
    #Gets all data from movie_genre in increments of 50
    while cont != 'q':
        query = "SELECT * FROM movie_genre ORDER BY movieID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        movie_list = [["MovieID", "Genre"]]
        movie_list += cursor.fetchall()
        
        matrixView.clean_print(movie_list)

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def addMovieGenre():
    movieID = input("Please enter the movie ID: ")
    genreName = input("Please enter the genre: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Inserts genre
    query = "INSERT INTO movie_genre (movieID, genreName) VALUES (%s, %s)"

    values = (movieID, genreName)
    cursor.execute(query, values)

    conn.commit()
    
    print("New movie genre added!")
    
    cursor.close()
    conn.close()
    cont = input("Press Enter to quit")