import os
import pickle

class Movie:
    def __init__(self, title, release_year, genre, imdb_url):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.imdb_url = imdb_url

    def __str__(self):
        return f"{self.title}, {self.release_year}, {self.genre}, {self.imdb_url}"
    
movies = []

if os.path.exists("movies.pkl"):
    with open("movies.pkl", "rb") as file:
        movies = pickle.load(file)
    
running = True

while running:

    user_input = int(input("\nWelcome to movie watchlist. Please choose your command:\nAdd new movie (1)\nShow all movies (2)\nExit (3)\n"))

    if user_input == 1:
        movie_title = input("Movies title: ")
        movie_release_year = input("Movie release year: ")
        movie_genere = input("Movie genre: ")
        movie_imdb_url = input("Movie IMDB URL: ")

        movie = Movie(movie_title, movie_release_year, movie_genere, movie_imdb_url)

        movies.append(movie)
        with open("movies.pkl", "wb") as file:
            pickle.dump(movies, file)
        
    elif user_input == 2:
        if (len(movies) > 0):
            print("All movies saved:")
            for movie in movies:
                print(movie)

    elif user_input == 3:
        running = False
        print("Goodbye!")
    else:
        print("Wrong command. Try again.")