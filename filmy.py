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



