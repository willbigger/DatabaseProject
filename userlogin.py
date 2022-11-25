from hashlib import sha512
from user_profile import addUserProfile
import mysql.connector

def main():
    """
    returns true if successful, false otherwise
    """
    print("Choose a number \n1: Login \n2: Create an account\n")
    user_input_number = input("Enter a number: ")
    print("\n")

    if len(user_input_number) == 0 or not user_input_number.isdigit():
        print("Invalid input\nFailed")
        return [False, ""]
    else:
        user_input_number = int(user_input_number)

    if user_input_number == 1:
        input_username = input("Email: ")
        input_password = input("Password: ")
        if loginUser(input_username, input_password):
            print("Login successful")
            return [True, input_username]
        else:
            print("Login failed")
            return [False, ""]
    elif user_input_number == 2:
        input_username = input("Email: ")
        print("Max 50 characters")
        input_password = input("Password: ")
        input_password2 = input("Confirm Password: ")
        if input_password != input_password2 or len(input_password) > 50:
            print("Passwords don't match or password is too long")
            return [False, ""]
        else:
            if createAccount(input_username, input_password):
                print("Created account successfully")
                return [True, input_username]
            else:
                print("Creation failed (Probably the username already exists, try a different one)")
                return [False, ""]
    else:
        print("Invalid input\nFailed")
        return [False, ""]


def loginUser(username, password):
    """
    Log in for user, returns true if login successful, false if login failed
    """
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    m = sha512()
    m. update(password. encode("utf8"))
    hashed_password = m.hexdigest()

    countQuery = f"SELECT COUNT(*) FROM user_passwords WHERE email='{username}' and password='{hashed_password}'"
    cursor.execute(countQuery)

    if (cursor.fetchall()[0][0] == 0):
        return False
    return True

def createAccount(username, password):
    """
    Creates a query for adding a row for the user
    Returns true if successful, false if failed
    
    >>>Make sure to check if username already exists, if it does fail the creation<<<
    """
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "movie_database")

    cursor = conn.cursor()

    countQuery = f"SELECT COUNT(*) FROM user_passwords WHERE email='{username}'"
    cursor.execute(countQuery)

    if (cursor.fetchall()[0][0] != 0):
        print("Email already exists, try a different one")
        return False
    
    insertQuery = "INSERT INTO user_passwords (email, password) VALUES (%s, %s)"

    m = sha512()
    m. update(password. encode("utf8"))
    hashed_password = m.hexdigest()

    print(hashed_password)
    values = (username, hashed_password)
    cursor.execute(insertQuery, values)

    conn.commit()
    cursor.close()
    conn.close()

    addUserProfile(username)
    return True