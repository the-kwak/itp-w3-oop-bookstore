class Bookstore(object):
    def __init__(self, bookstore_name):
        self.name = bookstore_name
        self.book_inventory = []
        
    def add_book(self, book):
        # Take in book variable and append to our book inventory
        self.book_inventory.append(book)
        
    
    def get_books(self):
        return self.book_inventory

class Author(object):
    def __init__ (self, name, nationality):
        self.name = name
        self.nationality = nationality
        # initialize a list of books for the author
        self.list_of_books = []
        
    def get_books(self):
        # Return the list of books for the author
        return self.list_of_books
        
        

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Takes the author object and adds the current book to the list in the
        # Author object
        author.list_of_books.append(self)
