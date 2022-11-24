from userlogin import main

"""
Driver for Command Line a loop where each iteration is a action from the user
"""

logged_in = False

while not logged_in:
    logged_in = main()

user_input_number = -1

while user_input_number != 0:
    if user_input_number == 1:
        print("-------------------------------------")
        print("Profile")
        print("-------------------------------------")
    elif user_input_number == 2:
        input_movie_name = input("Enter movie name \nCase insensitive \nSearch returns movies that contain the words you enter \n\nMovie Name:")

        print("-------------------------------------")
        print("Database information from database")
        print("-------------------------------------")
    elif user_input_number == 3:
        print("-------------------------------------")
        print("Switching Accounts")
        print("-------------------------------------")

    print("\n\nChoose a number \n0: Exit \n1: View profile \n2: View Movies \n3:Switch Accounts\n\n")
    user_input_number = input("Enter a number: ")
    if len(user_input_number) == 0 or not user_input_number.isdigit():
        user_input_number = 0
        print("Invalid input\nExiting")
    else:
        user_input_number = int(user_input_number)
    print("\n")

print("All changes saved\nBye!")