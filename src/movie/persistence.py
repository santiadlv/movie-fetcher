import csv


class FileWriter():
    def __init__(self) -> None:
        """Constructor for the FileWriter class
        """
        self._fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        
    def write_to_file(self, filename: str, movie_list: list) -> None:
        """Write the movies' data to a CSV file

        Args:
            filename (str): ame of the file where the data will be written
            movie_list (list): list of movies retrieved from set URL
        """
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self._fields)
            writer.writeheader()
            for movie in movie_list:
                writer.writerow({**movie})

        print(f'Movie data written to file named \'{filename}\'')
