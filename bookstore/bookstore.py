class Bookstore(object):
    def __init__(self, bookstore_name):
        self.name = bookstore_name
        self.book_inventory = []
        self.results =[]
        
    def add_book(self, book):
        # Take in book variable and append to our book inventory
        self.book_inventory.append(book)
        
    
    def get_books(self):
        return self.book_inventory
    
    def search_books(self, author = None, title = None):
        self.results = []
        if title != None:
            for book in self.book_inventory:
                if book.title.startswith(title.title(), 0 , len(title)) :
                    self.results.append(book)
                    
        elif author != None:
            self.results
            for book in self.book_inventory:
                if author is book.author:
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
