import datetime
from random import randint

#1. klasa filmy
class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

#3. dodanie odtworzenia
    def play(self):
        self.plays += 1

#5. tytuł i rok
    def __str__(self):
        return f'{self.title} ({self.year}) '


#2. klasa seriale
class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
#4. odcienk
    def __str__(self):
        return f'{self.title} S{self.episode:0=2d}E{self.season:0=2d}'

#7. funkcje movies/series
def get_movies():
    movies = []
    for movie in list:
        if isinstance(movie, Series):
            continue
        movies.append(movie)
    return sorted(movies, key=lambda movie: movie.title)

def get_series():
    series = []
    for movie in list:
        if isinstance(movie, Series):
            series.append(movie)
    return sorted(series, key=lambda series: series.title)

#8. funkcja search
def search(title):
    for movie in list:
        if movie.title == title:
            return movie

#6. lista filmów i seriali
list = [Movie("Skazani na Shawshank", 1994, "Dramat", 1), 
        Movie("Nietykalni", 2011, "Dramat/Komedia", 1),
        Movie("Zielona mila", 1999, "Dramat", 2), 
        Movie("Ojciec chrzestny", 1972, "Dramat/Gangsterski", 3),
        Movie("Dwunastu gniewnych ludzi", 1957, "Dramat sądowy", 4), 
        Series("Czarnobyl", 2019, "Dramat", 5, 1, 1),
        Series("Breaking Bad", 2008, "Dramat/Kryminał", 6, 1, 2), 
        Series("Gra o tron", 2011, "Dramat/Przygodowy", 7, 2, 3),
        Series("Nasza planeta", 2019, "Dokumentalny", 8, 3, 4),
        Series("Kompania braci", 2001, "Dramat/Wojenny", 9, 4, 5), 
        Series("Biuro", 2005, "Commedy", 10, 5, 6),]