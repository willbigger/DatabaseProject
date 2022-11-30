'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
https://stackoverflow.com/questions/47873444/how-to-select-50-rows-everytime-from-mysql-table
'''
import mysql.connector
import matrixView

def searchMoviesName():
    #string manipulation for the movie title
    movie_title = input("Please enter the movie name to search: ")
    movie_title = movie_title.strip().lower()

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    searchQuery = f"SELECT movieID, name FROM movie Where lower(name) LIKE '%{movie_title}%'"
    cursor.execute(searchQuery)
    movie_list = [["MovieID", "Movie Title"]]
    movie_list += cursor.fetchall()
    
    print("\nList of matching movies\n")
    matrixView.clean_print(movie_list)

    if len(movie_list) == 1:
        print("No matches")

    cursor.close()
    conn.close()
    cont = input("Press Enter to quit")

def searchMoviesYear():
    #string manipulation for the movie title
    movie_year = int(input("Please enter the movie year to search (4-digit year): "))

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    searchQuery = f"SELECT movieID, name FROM movie Where YEAR(releaseDate) = {movie_year}"
    cursor.execute(searchQuery)
    movie_list = [["MovieID", "Movie Title"]]
    movie_list += cursor.fetchall()
    
    print("\nList of matching movies\n")
    matrixView.clean_print(movie_list)
    
    if len(movie_list) == 1:
        print("No matches")

    cursor.close()
    conn.close()
    cont = input("Press Enter to quit")



def viewMovies():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""
    
    #Gets all data from movie in increments of 50
    while cont != 'q':
        query = "SELECT * FROM movie ORDER BY movieID LIMIT 50 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        movie_list = [["MovieID", "Title", "Runtime", "Date"]]
        movie_list += cursor.fetchall()
        
        matrixView.clean_print(movie_list)

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 50
        
    cursor.close()
    conn.close()

def addMovie():
    name = input("Please enter the movie name: ")
    runtime = input("Please enter the runtime: ")
    releaseDate = input("Please enter the release date (year-month-day XXXX-XX-XX): ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #calculates a new ID for the new entry
    lastIDQuery = "SELECT movieID FROM movie ORDER BY movieID DESC LIMIT 1"
    cursor.execute(lastIDQuery)
    newID = cursor.fetchall()[0][0] + 1

    #Adds movie
    insertQuery = "INSERT INTO movie (movieID, name, runtime, releaseDate) VALUES (%s, %s, %s, %s)"

    values = (newID, name, runtime, releaseDate)
    cursor.execute(insertQuery, values)

    conn.commit()
    
    print("New movie added!")
    
    cursor.close()
    conn.close()
    cont = input("Press Enter to quit")