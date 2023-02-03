import datetime
from random import randint

#1. klasa filmy
class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        # variables
        self.played = 0
#3. dodanie odtworzenia
    def play(self):
        self.played += 1
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
    only_movies_list = [movie for movie in list if not isinstance(movie, Series)]
    print(only_movies_list)


def get_series():
    only_series_list = [movie for movie in list if isinstance(movie, Series)]
    print(only_series_list)

list = [Movie("Skazani na Shawshank", 1994, "Dramat"), 
        Movie("Nietykalni", 2011, "Dramat/Komedia"),
        Movie("Zielona mila", 1999, "Dramat"), 
        Movie("Ojciec chrzestny", 1972, "Dramat/Gangsterski"),
        Movie("Dwunastu gniewnych ludzi", 1957, "Dramat sądowy"), 
        Series("Czarnobyl", 2019, "Dramat", 1, 1),
        Series("Breaking Bad", 2008, "Dramat/Kryminał", 1, 2), 
        Series("Gra o tron", 2011, "Dramat/Przygodowy", 2, 3),
        Series("Nasza planeta", 2019, "Dokumentalny", 3, 4),
        Series("Kompania braci", 2001, "Dramat/Wojenny", 4, 5), 
        Series("Biuro", 2005, "Commedy", 5, 6),]