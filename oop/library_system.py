# library_system.py

class Book:
    """Base Book class with common attributes."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    """EBook class inheriting from Book, adds file_size."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """PrintBook class inheriting from Book, adds page_count."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """Library class demonstrating composition."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds any type of book to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints all books in the library with correct formatting."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
