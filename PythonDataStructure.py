library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Task: Function to add a book to the library
def add_book(library, book_title, author):
    new_book = (book_title, author)
    if new_book not in library:
        library.append(new_book)
        print(f'Book "{book_title}" by {author} added to the library.')
    else:
        print(f'Book "{book_title}" by {author} is already in the library.')
