# You have two lists, one for thriller movies and one for romantic movies
thriller_movies = ["Inception", "The Dark Knight", "Gone Girl"]
romantic_movies = ["The Notebook", "La La Land", "Eternal Sunshine of the Spotless Mind"]

# TODO: Ask the user for their name and their preferred movie genre
user_name = input("Hi, what is your name: ")
user_preferred_movie = input("What movie genre do you enjoy (thriller or romantic):  ")

# TODO: Based on their preference, recommend a movie from the corresponding list

if user_preferred_movie == "thriller":
    print(f"Since like thriller movies, i would recommend the movie '{thriller_movies[0]}' ")
    answer = input("Would you like another movie recommendation?: ")
    if(answer == "yes"):
        print(f"'{thriller_movies[1]}'")
    else:
        print("Program ended....")
    
elif user_preferred_movie == "romantic":
    print(f"Since like romantic movies, i would recommend the movie '{romantic_movies[0]}' ")
    answer = input("Would you like another movie recommendation?: ")
    if(answer == "yes"):
        print(f"'{romantic_movies[1]}'")
    else:
        print("Program ended....")

else:
    print("Sorry, that genre isnt available")
    print("Program ended....")
