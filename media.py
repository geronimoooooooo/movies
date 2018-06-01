import webbrowser

class Movie(): 
    """Represents a movie."""
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Method shows a trailer (opens a browser) of the clicked movie."""
        webbrowser.open(self.trailer_youtube_url)