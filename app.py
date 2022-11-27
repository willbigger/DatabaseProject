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

    # need to add user deletion (maybe require username AND password)
    matrix=[
        ["Choose a number  ", "", "", "", ""],
        ["0: Exit  ", "1: View All User Profiles  ", "2: View All Movies  ", "3: View All Reviews  ", "4: View All Genres  "], 
        ["5: Add a New Genre  ", "6: View All Actors  ", "7: Change/Update Favorite Actor  ", "8: Change/Update Favorite Actor  ", "9: Search for MovieID  "], 
        ["10: View All Directors  ", "11: View All Authors and their reviews  ", "12: View All Current Favorite Genres  ", "13: Add Favorite Genre  ", "14: Delete Favorite Genre  "],
        ["15: View All Current Favorite Movies  ", "16: Add Favorite Movie  ", "17: Delete Favorite Movie  ", "", ""],
        ["20: View All Reviews  ", "21: Add a Review  ", "22: Delete a Review  ", "23: Update a Review  ", "24: Like a Review  "], 
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
    print("\n\n\n\n\n\n\n\n\n\n----------------------------------------------------------------------")
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
        genre.addGenre()
    elif user_input_number == 6:
        movie_actor.viewActors()
    elif user_input_number == 7:
        user_profile.updateFavoriteActor(current_user_email)
    elif user_input_number == 8:
        user_profile.updateFavoriteDirector(current_user_email)
    elif user_input_number == 9:
        movie.searchMovies()
    elif user_input_number == 10:
        directs_movie.viewDirectors()
    elif user_input_number == 11:
        authored_by.viewAuthors()
    elif user_input_number == 12:
        favorite_genre.viewFavoriteGenres(current_user_email)
    elif user_input_number == 13:
        favorite_genre.addFavoriteGenres(current_user_email)
    elif user_input_number == 14:
        favorite_genre.deleteFavoriteGenres(current_user_email)
    elif user_input_number == 15:
        favorite_movie.viewFavoriteMovies(current_user_email)
    elif user_input_number == 16:
        favorite_movie.addFavoriteMovies(current_user_email)
    elif user_input_number == 17:
        favorite_movie.deleteFavoriteMovie(current_user_email)
    elif user_input_number == 20:
        review.viewReviews()
    elif user_input_number == 21:
        review.addReview(current_user_email)
    elif user_input_number == 22:
        review.deleteReview(current_user_email)
    elif user_input_number == 23:
        review.updateReview()
    elif user_input_number == 24:
        review.likeReview()

    pretty_print()
    user_input_number = input("Enter a number: ")
    if len(user_input_number) == 0 or not user_input_number.isdigit():
        user_input_number = 0
        print("Invalid input\nExiting")
    else:
        user_input_number = int(user_input_number)

print("\nAll changes saved\nBye!")