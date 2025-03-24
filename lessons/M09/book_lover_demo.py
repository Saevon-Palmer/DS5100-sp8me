from booklover.booklover import BookLover

# Create a BookLover object
reader = BookLover("Jane", "Jane@example.com", "Fiction")

# Add a book
reader.add_book("Lord of the Rings", 5)

# Prints the numbers of books read
print("The number of books read:", reader.num_books_read())