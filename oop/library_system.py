# library_system.py

# ---------------------------
# Base Class: Book
# ---------------------------
class Book:
    """
    A general book with common attributes: title and author.
    This is the parent class (superclass) for EBook and PrintBook.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        """
        Returns a simple description of a standard book.
        Subclasses will override or extend this.
        """
        return f"Book: {self.title} by {self.author}"


# ---------------------------
# Derived Class: EBook
# ---------------------------
class EBook(Book):
    """
    Represents a digital book.
    Inherits title and author from Book.
    Adds file_size, an attribute unique to EBooks.
    """

    def __init__(self, title, author, file_size):
        # Call the parent class constructor to initialize title and author
        super().__init__(title, author)
        self.file_size = file_size

    def details(self):
        """
        Overrides the parent details() method to include file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# ---------------------------
# Derived Class: PrintBook
# ---------------------------
class PrintBook(Book):
    """
    Represents a physical printed book.
    Inherits title and author from Book.
    Adds page_count, unique to printed books.
    """

    def __init__(self, title, author, page_count):
        # Initialize common attributes using the parent constructor
        super().__init__(title, author)
        self.page_count = page_count

    def details(self):
        """
        Overrides the details() method to include page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# ---------------------------
# Composition: Library Class
# ---------------------------
class Library:
    """
    A Library contains multiple Book objects.
    This demonstrates composition: a Library is composed of Books.
    """

    def __init__(self):
        # Store all types of books (Book, EBook, PrintBook)
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of every book in the library.
        It relies on each object’s own details() method.
        """
        for book in self.books:
            print(book.details())
