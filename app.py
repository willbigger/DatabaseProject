import genre, movie, directs_movie, movie_actor, movie_genre, user_profile, favorite_genre, favorite_movie, authored_by, review, userlogin, user_passwords_audit
"""
Driver for Command Line a loop where each iteration is a action from the user
"""

logged_in = False
trys = 3
main_list = []
print("\n\n\n\n\n\n\n\n\n\n----------------------------------------------------------------------")
print("Log In\n")


def pretty_print():
    #code from https://stackoverflow.com/questions/13214809/pretty-print-2d-list

    matrix=[
        ["USER ACTIONS:  ", "", "", "", ""],
        ["", "", "", "", ""],
        ["General", "", "", "", ""], 
        ["", "", "", "", ""],
        ["0: Exit  ", "", "", "", ""], 
        ["1: View All User Profiles  ", "2: View All Movies  ", "3: View All Genres  ", "4: View All Actors  ", "5: View All Directors  "], 
        ["6: Add a New Genre  ", "7: Search for MovieID (on title)  ", "8: Search for MovieID (on year)  ",  "9: View Movies with Their Genres  ", ""], 
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["Favorites", "", "", "", ""],
        ["", "", "", "", ""],
        ["11: Change/Update Favorite Actor  ", "12: Change/Update Favorite Actor  ", "", "", ""],
        ["16: View All Current Favorite Genres  ", "17: Add Favorite Genre  ", "18: Delete Favorite Genre  ", "", ""],
        ["21: View All Current Favorite Movies  ", "22: Add Favorite Movie  ", "23: Delete Favorite Movie  ", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["Reviews", "", "", "", ""],
        ["", "", "", "", ""],
        ["26: View All Authors and their reviews  ", "", "", "", ""], 
        ["31: View All Reviews  ", "32: Add a Review  ", "33: Delete a Review  ", "34: Update a Review  ", "35: Like a Review  "], 
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["Deleting Your Account", "", "", "", ""],
        ["", "", "", "", ""],
        ["36: Delete your account  ", "", "", "", ""], 
    ]

    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n")


while not logged_in and trys > 0:
    print("\nLogin attempts left: ", trys)
    main_list = userlogin.main()
    logged_in = main_list[0]
    trys -= 1

if trys == 0 and not logged_in:
    print("\nAll attempts exhausted\nLogin failed")
    user_input_number = 0
else:
    current_user_email = main_list[1]
    user_input_number = -1

while user_input_number != 0:
    print("----------------------------------------------------------------------")
    print("\n\n\n\n\n\n\n\n\n\n----------------------------------------------------------------------")
    print("\nCurrent user email: " + current_user_email + "\n")
    pretty_print()
    user_input_number = input("Enter a number: ")
    if len(user_input_number) == 0 or not user_input_number.isdigit():
        user_input_number = 0
        print("Invalid input\nExiting")
    else:
        user_input_number = int(user_input_number)


    if user_input_number == 1:
        user_profile.viewUserProfiles()
    elif user_input_number == 2:
        movie.viewMovies()
    elif user_input_number == 3:
        genre.viewGenres()
    elif user_input_number == 4:
        movie_actor.viewActors()
    elif user_input_number == 5:
        directs_movie.viewDirectors()

    elif user_input_number == 6:
        genre.addGenre()
    elif user_input_number == 7:
        movie.searchMoviesName()
    elif user_input_number == 8:
        movie.searchMoviesYear()
    elif user_input_number == 9:
        movie_genre.viewMovieGenres()
    

    elif user_input_number == 11:
        user_profile.updateFavoriteActor(current_user_email)
    elif user_input_number == 12:
        user_profile.updateFavoriteDirector(current_user_email)

    elif user_input_number == 16:
        favorite_genre.viewFavoriteGenres(current_user_email)
    elif user_input_number == 17:
        favorite_genre.addFavoriteGenres(current_user_email)
    elif user_input_number == 18:
        favorite_genre.deleteFavoriteGenres(current_user_email)

    elif user_input_number == 21:
        favorite_movie.viewFavoriteMovies(current_user_email)
    elif user_input_number == 22:
        favorite_movie.addFavoriteMovies(current_user_email)
    elif user_input_number == 23:
        favorite_movie.deleteFavoriteMovie(current_user_email)

    elif user_input_number == 26:
        authored_by.viewAuthors()

    elif user_input_number == 31:
        review.viewReviews()
    elif user_input_number == 32:
        review.addReview(current_user_email)
    elif user_input_number == 33:
        review.deleteReview(current_user_email)
    elif user_input_number == 34:
        review.updateReview()
    elif user_input_number == 35:
        review.likeReview()

    elif user_input_number == 36:
        user_profile.deleteUserProfile(current_user_email)
        user_input_number = 0
    

print("----------------------------------------------------------------------")
print("\nAll changes saved\nBye!")