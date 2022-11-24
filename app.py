from userlogin import main

"""
Driver for Command Line a loop where each iteration is a action from the user
"""

logged_in = False
trys = 3
print("Log into App\nYou have 3 tries\n")

while not logged_in and trys > 0:
    print("\nAttempts left: ", trys)
    logged_in = main()
    trys -= 1

if trys == 0 and not logged_in:
    print("\nAll attempts exhausted\nLogin failed")
    user_input_number = 0
else:
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

print("\nAll changes saved\nBye!")