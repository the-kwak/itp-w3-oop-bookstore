class Bookstore(object):
    def __init__(self, bookstore_name):
        self.name = bookstore_name
        self.book_inventory = []
        
        self.results = []
        
    def add_book(self, book):
        # Take in book variable and append to our book inventory
        self.book_inventory.append(book)
        
    
    def get_books(self):
        return self.book_inventory
    
    
    # author was set to none because none is falsey and we could use it in the
    # if author is a string it will be truthy
    def search_books(self, author = None, title = None):
        self.results =[]
        
        if title:
            #here?
            for book in self.book_inventory:
                # let's try with print statements
                if book.title.startswith(title.title()):
                    self.results.append(book)
        
        elif author:
            for book in self.book_inventory:
                if book.author is author:
                    self.results.append(book)
        
        return self.results
        
    
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
