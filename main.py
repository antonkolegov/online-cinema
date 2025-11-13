class Movie:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    def __str__(self):
        return f" {self.title} ({self.year})"

# Создадим объект
movie = Movie("Dune", 2021)
print(movie)
