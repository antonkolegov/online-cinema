from typing import List

class InvalidRatingError(Exception):
    """Рейтинг должен быть целым числом от 1 до 10."""
    pass

class MovieNotFoundError(Exception):
    """Фильм с таким названием не найден."""
    pass