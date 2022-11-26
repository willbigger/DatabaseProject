'''
Inspired by:
https://realpython.com/python-mysql 
https://www.geeksforgeeks.org/extract-data-from-database-using-mysql-connector-and-xampp-in-python
https://www.w3schools.com/python/python_mysql_insert.asp
'''
import mysql.connector

def viewAudit():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    #Gets all data from user_passwords_audit
    query = "SELECT * FROM user_passwords_audit"
    cursor.execute(query)
    
    table = cursor.fetchall()
    
    print("Audit:")
    print("Email    Time    Action")
    for row in table:
        print(row[0], end=": ")
        print(row[1], end=" ")
        print(row[2], end="\n")

    cursor.close()
    conn.close()