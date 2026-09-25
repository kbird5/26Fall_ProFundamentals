fav_movies = []

fav_numbers = [1, 5, 7, 3]
mixed = [1, 5.5, True, "hello"]

fav_movies = ["Sandlot", "The Lego Movie", "Dune"]
print(fav_movies)

print(fav_movies[0])
print(fav_movies[1])
print(fav_movies[2])

fav_numbers = [4, 11, 27]
print(fav_numbers[0])

print(len(fav_movies))

fav_movies.append("Iron Man")

print(fav_movies)
print(len(fav_movies))

fav_movies.insert(1, "Batman")
print(fav_movies)

del fav_movies[2]
print(fav_movies)

del fav_movies[0]
del fav_movies[0]
del fav_movies[0]

print(fav_movies)