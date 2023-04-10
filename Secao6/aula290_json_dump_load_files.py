# json.dump e json.load com arquivos
import json
import os

FILE_NAME = 'aula290.json'
FILE_PATH_ABS = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(FILE_PATH_ABS, 'w') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(FILE_PATH_ABS, 'r') as file:
    movie_json = json.load(file)
    print(movie_json)
