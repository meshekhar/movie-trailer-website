"""Module contains Movie class."""

class Movie():
    """ Movie class ."""
        
    VALID_RATINGS = ["G","PG","PG13","R"] # Class variable
    
    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url):
        
        # The __init__ method doesn't return anything.
        # method takes 4 variables to create a movie object
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url