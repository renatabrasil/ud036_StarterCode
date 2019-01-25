class Movie():
    """Class which represent a movie"""
    def __init__(self, title, genre, language, poster_image_url, trailer_url, duration, year):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url
        self.genre = genre
        self.language = language
        # In minutes
        self.duration = duration
        self.year = year
