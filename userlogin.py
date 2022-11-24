def main():
    """
    returns true if successful, false otherwise
    """
    print("Choose a number \n1: Login \n2: Create an account\n\n")
    user_input_number = input("Enter a number: ")
    print("\n")

    if len(user_input_number) == 0 or not user_input_number.isdigit():
        print("Invalid input\nFailed")
        return False
    else:
        user_input_number = int(user_input_number)

    if user_input_number == 1:
        input_username = input("Username: ")
        input_password = input("Password: ")
        if loginUser(input_username, input_password):
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False
    elif user_input_number == 2:
        input_username = input("Username: ")
        input_password = input("Password: ")
        input_password2 = input("Confirm Password: ")
        if input_password != input_password2:
            print("Passwords don't match")
            return False
        else:
            if createAccount(username, password):
                print("Created account successfully")
                return True
            else:
                print("Creation failed (Probably the username already exists, try a different one)")
                return False
    else:
        print("Invalid input\nFailed")
        return False


def loginUser(username, password):
    """
    Log in for user, returns true if login successful, false if login failed
    """
    return True

def createAccount(username, password):
    """
    Creates a query for adding a row for the user
    Returns true if successful, false if failed
    
    >>>Make sure to check if username already exists, if it does fail the creation<<<
    """
    return False