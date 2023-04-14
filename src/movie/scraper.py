import requests
from bs4 import BeautifulSoup, ResultSet


class WebScraper():
    def __init__(self, url: str) -> None:
        """Constructor for the WebScraper class

        Args:
            url (str): URL of the site to scrape the data from
        """
        self._url = url
        self._parser = 'lxml'
        
    def fetch(self) -> requests.Response:
        """Download data from set URL

        Returns:
            requests.Response: Response object from the GET request
        """
        return requests.get(self._url)
    
    def parse(self, response: str) -> BeautifulSoup:
        """Create a BeautifulSoup instance for scraping after parsing the response

        Args:
            response (str): Response object from the previous GET request

        Returns:
            BeautifulSoup: bs4 instance with own properties and functions
        """
        return BeautifulSoup(response.text, self._parser)
    
    def get_movies(self, soup: BeautifulSoup) -> ResultSet:
        """Retrieve the movies from the BeautifulSoup object

        Args:
            soup (BeautifulSoup): bs4 instance parsed from the GET request's response

        Returns:
            ResultSet: collection of movie objects
        """
        return soup.select('td.titleColumn')
    
    def get_links(self, soup: BeautifulSoup) -> list[str]:
        """Filter movie objects to get their respective hyperlinks

        Args:
            soup (BeautifulSoup): bs4 instance parsed from the GET request's response

        Returns:
            list[str]: collection of the movies' links
        """
        return [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    
    def get_crew(self, soup: BeautifulSoup) -> list[str]:
        """Filter movie objects to get their respective crew members

        Args:
            soup (BeautifulSoup): bs4 instance parsed from the GET request's response

        Returns:
            list[str]: collection of the movies' crew members
        """
        return [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        
    def get_ratings(self, soup: BeautifulSoup) -> list[str]:
        """Filter movie objects to get their respective ratings

        Args:
            soup (BeautifulSoup): bs4 instance parsed from the GET request's response

        Returns:
            list[str]: collection of the movies' ratings
        """
        return [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        
    def get_votes(self, soup: BeautifulSoup) -> list[str]:
        """filter movie objects to get their respective votes

        Args:
            soup (BeautifulSoup): bs4 instance parsed from the GET request's response

        Returns:
            list[str]: collection of the movies' votes
        """
        return [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=nv]')]
    
    def process_data(self) -> tuple:
        """Main method to request, process and return the desired movie data

        Returns:
            tuple(list[str]): multiple collections containing the movies and their attributes
        """
        response = self.fetch()
        soup = self.parse(response)
        
        movies = self.get_movies(soup)
        links = self.get_links(soup)
        crew = self.get_crew(soup)
        ratings = self.get_ratings(soup)
        votes = self.get_votes(soup)
        
        return movies, links, crew, ratings, votes
    