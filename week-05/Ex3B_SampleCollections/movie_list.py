# My favorite movies list
movie_list = ["The Dark Knight", "Titanic" , "Dune"]

# Print length description
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")

# Print the complete list
print(movie_list)

# Print sorted list using sorted() function
print(sorted(movie_list))
# Print original list again - notice sorted() did NOT change the original!
print(movie_list)

# Now sort using .sort() method
movie_list.sort()
print(movie_list)
# Notice .sort() DID permanently change the list!

# Add a new movie using .append()
movie_list.append("The Matrix")
print(movie_list)
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")