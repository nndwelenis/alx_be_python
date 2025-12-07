# book_class.py

class Book:
    # The constructor method.
    # It runs automatically when you create an instance of Book.
    def __init__(self, title, author, year):
        # Public attributes
        self.title = title
        self.author = author
        self.year = year

    # The destructor method.
    # Python calls this when an object is deleted using del,
    # or when the program ends and the object is cleaned up.
    def __del__(self):
        print(f"Deleting {self.title}")

    # The string representation method.
    # This is what gets printed when you use print(my_book).
    # It is meant for humans to read.
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # The official representation of the object.
    # This version is meant for developers and debugging.
    # It returns a string that could recreate the object exactly.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
