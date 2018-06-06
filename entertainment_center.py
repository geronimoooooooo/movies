import media
import fresh_tomatoes


# create Movie object
toy_story = media.Movie("Toy Story", "A story of a boy and his toys.",
						"https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg",
            "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

shrek = media.Movie("Shrek", "An ogre goes on an adventure",
        "https://vignette.wikia.nocookie.net/shrek/images/7/7c/Shrek_Poster_02.jpg",
        "https://www.youtube.com/watch?v=W37DlG1i61s")

californiaction = media.Movie("Californication", "An author living in california",
									"https://images-na.ssl-images-amazon.com/images/I/81B9XVkMJ9L._SY445_.jpg",
									"https://www.youtube.com/watch?v=VfxF6UkoX-g")

print ("entertainment started!")

movies = [toy_story, shrek, californiaction]
# invoke method open_movies_page() to display provided movies
fresh_tomatoes.open_movies_page(movies)
