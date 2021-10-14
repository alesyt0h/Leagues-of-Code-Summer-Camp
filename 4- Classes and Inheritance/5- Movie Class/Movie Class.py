from typing import List    


class Movie:
    def __init__(self, title: str, genre: str):
        self.title = title
        self.genre = genre

def get_sci_fi(movies: List[Movie]) -> List[Movie]:
    scifi = []
    for movie in movies:
        if movie.genre == "Sci-fi":
            scifi.append(movie)
    return scifi
    
p = Movie("Martian", "Sci-fi");
q = Movie("Romeo and Juliet", "Drama");
r = Movie("Jurassic park", "Sci-fi");
l_movies = [p, q, r]
res = get_sci_fi(l_movies)
for i in range(len(res)):
    print(res[i].title)

# should print
# Martian
# Jurassic park