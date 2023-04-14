from movie.scraper import WebScraper
from movie.extractor import DataExtractor
from movie.persistence import FileWriter


def main():
    # Set the URL to be fetched
    url = 'http://www.imdb.com/chart/top'

    # Scrape the data from the web response
    scraper = WebScraper(url)
    movies, links, crew, ratings, votes = scraper.process_data()
    
    # Extract and process the data from the retrieved data
    extractor = DataExtractor(movies, links, crew, ratings, votes)
    extractor.extract_all()
    movie_list = extractor.get_movies()

    # Write and save the data to an external file
    writer = FileWriter()
    filename = 'movie_results.csv'
    writer.write_to_file(filename, movie_list)

if __name__ == '__main__':
    main()
