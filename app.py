import genre, movie, directs_movie, movie_actor
"""
Driver for Command Line a loop where each iteration is a action from the user
"""
user_input_number = -1

while user_input_number != 0:
    if user_input_number == 1:
        input_username = input("Username: ")
        input_password = input("Password: ")
    elif user_input_number == 2:
        print("-------------------------------------")
        print("Profile")
        print("-------------------------------------")
    elif user_input_number == 3:
        input_movie_name = input("Enter movie name \nCase insensitive \nSearch returns movies that contain the words you enter \n\nMovie Name:")

        print("-------------------------------------")
        print("Database information from database")
        print("-------------------------------------")
    elif user_input_number == 4:
        movie_actor.addActor()

    
    print("\n\nChoose a number \n0: Exit \n1: User login \n2: View profile (if currently logged in) \n3: View Movies\n\n")
    user_input_number = int(input("Enter a number: "))
    print("\n")

print("All changes saved\nBye!")