import os
import json
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


class Movie():
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)
            return "Add file in .json"
if __name__ == "__main__":
    m = Movie("harry potter")
    print(m._write_movies(["test1", "test2"]))