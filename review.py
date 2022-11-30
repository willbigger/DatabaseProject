'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector, datetime
import matrixView

def viewReviews():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    offset = 0

    cont = ""
    
    #Gets all data from review in increments of 10
    while cont != 'q':
        query = "SELECT * FROM review NATURAL JOIN movie ORDER BY reviewID LIMIT 10 OFFSET " + str(offset)
        
        cursor.execute(query)
        
        review_list = [["MovieID", "Review ID", "Write Date", "Number Rating", "Comment Text", "Number of Likes"]]
        review_list += cursor.fetchall()
        
        matrixView.clean_print(review_list)

        cont = input("Enter \'q\' to quit, anything else to continue\n")
        offset += 10
        
    cursor.close()
    conn.close()

def addReview(email):
    movieID = input("Please enter movie ID: ")
    numberRating = input("Please enter your rating number on a scale of 1-10: ")
    commentText = input("Please enter your comments: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]

    countQuery = "SELECT COUNT(*) FROM review"
    cursor.execute(countQuery)
    
    #checks if table is empty
    if (cursor.fetchall()[0][0] == 0):
        newID = 1
    else:
        #calculates a new ID for the new entry
        lastIDQuery = "SELECT reviewID FROM review ORDER BY reviewID DESC LIMIT 1"
        cursor.execute(lastIDQuery)
        newID = cursor.fetchall()[0][0] + 1
        
    #Adds review
    insertQuery = "INSERT INTO review (reviewID, movieID, writeDate, numberRating, commentText, numberOfLikes) VALUES (%s, %s, %s, %s, %s, %s)"

    values = (newID, movieID, datetime.datetime.now(), numberRating, commentText, 0)
    try:
        cursor.execute(insertQuery, values)
        print("Review added!")
    except mysql.connector.errors.IntegrityError:
        print("\nFailed. Comment must contain text\n\nExit")
        cursor.close()
        conn.close()
        return

    conn.commit()

    #Adds to author_by
    insertQuery = "INSERT INTO authored_by (userID, reviewID) VALUES (%s, %s)"

    values = (userID, newID)
    cursor.execute(insertQuery, values)

    conn.commit()
    cursor.close()
    conn.close()

def deleteReview(email):
    viewReviews()
    reviewID = input("Please enter your review ID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    userIDQuery = "SELECT userID FROM user_profile WHERE email = '" + email + "'"
    cursor.execute(userIDQuery)
    userID = cursor.fetchall()[0][0]
    
    #Deletes review
    deleteQuery = "DELETE FROM review WHERE reviewID = " + str(reviewID)
    cursor.execute(deleteQuery)
    conn.commit()

    #Deletes author
    deleteQuery = "DELETE FROM authored_by WHERE reviewID = " + str(reviewID)
    cursor.execute(deleteQuery)
    conn.commit()
    
    print("Review deleted!")
    
    cursor.close()
    conn.close()

def updateReview():
    viewReviews()
    reviewID = input("Please enter your review ID: ")
    numberRating = input("Please enter your review number rating update: ")
    commentText = input("Please enter your review comment update: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Updates review
    query = "UPDATE review SET numberRating = '" + numberRating + "', commentText = '" + commentText + "' WHERE reviewID = " + str(reviewID)

    try:
        cursor.execute(query)
        print("Review updated!")
    except mysql.connector.errors.IntegrityError:
        print("\nFailed. Comment must contain text\n\nExit")

    conn.commit()
    cursor.close()
    conn.close()

def likeReview():
    viewReviews()
    reviewID = input("Please enter the review ID: ")

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    getLikeQuery = "SELECT numberOfLikes FROM review WHERE reviewID = " + str(reviewID)
    cursor.execute(getLikeQuery)
    newNumberOfLikes = cursor.fetchall()[0][0] + 1

    #Adds a like
    query = "UPDATE review SET numberOfLikes = " + str(newNumberOfLikes) + " WHERE reviewID = " + str(reviewID)

    cursor.execute(query)

    conn.commit()
    
    print("Likes updated!")
    
    cursor.close()
    conn.close()