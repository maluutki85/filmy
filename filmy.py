import random
from datetime import date

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
        return f"'{self.title}': S{self.season:02d}E{self.episode:02d}"

#6. lista filmów i seriali

movie1 = Movie(title = "Skazani na Shawshank", year = 1994, genre = "Dramat", plays = 1)
movie2 = Movie(title = "Nietykalni", year = 2011, genre = "Dramat/Komedia", plays = 2)
movie3 = Movie(title = "Zielona mila", year = 1999, genre = "Dramat", plays = 3)
movie4 = Movie(title = "Ojciec chrzestny", year = 1972, genre = "Dramat/Gangsterski", plays = 4)
movie5 = Movie(title = "Dwunastu gniewnych ludzi", year = 1957, genre = "Dramat sądowy", plays = 5)
series1 = Series(title = "Czarnobyl", year = 2019, genre = "Dramat", plays = 6, episode = 1, season = 2)
series2 = Series(title = "Breaking Bad", year = 2008, genre = "Dramat/Kryminał", plays = 7, episode = 2, season = 3)
series3 = Series(title = "Gra o tron", year = 2011, genre = "Dramat/Przygodowy", plays = 8, episode = 3, season = 4)
series4 = Series(title = "Nasza planeta", year = 2019, genre = "Dokumentalny", plays = 9, episode = 4, season = 5)
series5 = Series(title = "Kompania braci", year = 2001, genre = "Dramat/Wojenny", plays = 10, episode = 5, season = 6)

list = [movie1, movie2, movie3, movie4, movie5, series1, series2, series3, series4, series5]

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

#9. generowanie odtworzeń
def generate_views():
    movie = random.choice(list)
    movie.plays = random.randint(1, 100)
    return movie.plays

#10. odwtorzenia x10
def generate_views_x10():
    for i in range(10):
        generate_views() 


def top_titles(number, content_type='all'):
    if content_type == 'Movies':
        movies = []
        for movie in list:
            if isinstance(movie, Series):
                continue
            movies.append(movie)
        top_titles = sorted(movies, key=lambda movie: movie.plays, reverse=True)
        return top_titles[:number]
    elif content_type == 'Series':
        series = []
        for movie in list:
            if isinstance(movie, Series):
                series.append(movie)
        top_titles = sorted(series, key=lambda series: series.plays, reverse=True)
        return top_titles[:number]
    else:
        top_titles = sorted(list, key=lambda x: x.plays, reverse=True)
        return top_titles[:number]




if __name__ == '__main__':
    print("Biblioteka filmów")
    generate_views()
    print(f"Najpopularniejsze filmy i seriale dnia {date.today():%d.%m.%Y}:")
    for title in top_titles(3):
        print(title)