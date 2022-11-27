import genre, movie, directs_movie, movie_actor, movie_genre, user_profile, favorite_genre, favorite_movie, authored_by, review, userlogin, user_passwords_audit
"""
Driver for Command Line a loop where each iteration is a action from the user
"""

logged_in = False
trys = 3
main_list = []
print("Log into App\nYou have 3 tries\n")


def pretty_print():
    #code from https://stackoverflow.com/questions/13214809/pretty-print-2d-list
    matrix=[
        ["Choose a number  ", "", "", "", ""],
        ["0: Exit  ", "1: View All User Profiles  ", "2: View All Movies  ", "3: View All Reviews  ", "4: View All Genres  "], 
        ["5: Search for a MovieID", "", "", "", ""],
        ["", "", "", "", ""]
    ]

    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n")


while not logged_in and trys > 0:
    print("\nAttempts left: ", trys)
    main_list = userlogin.main()
    logged_in = main_list[0]
    trys -= 1

if trys == 0 and not logged_in:
    print("\nAll attempts exhausted\nLogin failed")
    user_input_number = 0
else:
    current_user_email = main_list[1]
    user_input_number = -1

print("\nCurrent user email: " + current_user_email + "\n")

while user_input_number != 0:
    if user_input_number == 1:
        user_profile.viewUserProfiles()
    elif user_input_number == 2:
        movie.ViewMovies()
    elif user_input_number == 3:
        review.viewReviews()
    elif user_input_number == 4:
        genre.viewGenres()
    elif user_input_number == 5:
        movie.searchMovies()

    pretty_print()
    user_input_number = input("Enter a number: ")
    if len(user_input_number) == 0 or not user_input_number.isdigit():
        user_input_number = 0
        print("Invalid input\nExiting")
    else:
        user_input_number = int(user_input_number)

print("\nAll changes saved\nBye!")