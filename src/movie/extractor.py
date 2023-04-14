import re
from bs4 import element


class DataExtractor():
    def __init__(self, movies: list, links: list, crew: list, ratings: list, votes: list) -> None:
        """Constructor for the DataExtractor class

        Args:
            movies (list): collection of movie objects
            links (list): collection of the movies' links
            crew (list): collection of the movies' crew members
            ratings (list): collection of the movies' ratings
            votes (list): collection of the movies' votes
        """
        self._movies = movies
        self._links = links
        self._crew = crew
        self._ratings = ratings
        self._votes = votes
        self._data = []
        
    def add_movie(self, movie: dict) -> None:
        """Add a movie to the data object of the DataExtractor class

        Args:
            movie (dict): movie object to be added
        """
        self._data.append(movie)
        
    def get_movies(self) -> list:
        """Return all of the movies added to the data of the class

        Returns:
            list: collection of movies
        """
        return self._data
        
    def movie_splitter(self, movie_obj: element.Tag, index: int) -> tuple:
        """Given a movie, split it to retrieve its title, year and place

        Args:
            movie_obj (element.Tag): movie object retrieved directly from bs4 object
            index (int): index of the object in question

        Returns:
            tuple: immutable collection containing the movie's title, year and place
        """
        movie_string = movie_obj.get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]
        
        return title, year, place

    def compose(self, title: str, year: str, place: str, index: int) -> dict:
        """Create an object to be added to the class' data

        Args:
            title (str): movie title
            year (str): movie year
            place (str): movie place
            index (int): index of the movie in question

        Returns:
            dict: a record containing the movie's information
        """
        record = {
            "movie_title": title,
            "year": year,
            "place": place,
            "star_cast": self._crew[index],
            "rating": self._ratings[index],
            "vote": self._votes[index],
            "link": self._links[index],
            "preference_key": index % 4 + 1
        }
        
        return record
    
    def extract_all(self) -> None:
        """Process all of the movies, extract their attributes and add them to the class' data
        """
        for idx, val in enumerate(self._movies):
            title, year, place = self.movie_splitter(val, idx)
            movie = self.compose(title, year, place, idx)
            self.add_movie(movie)
    