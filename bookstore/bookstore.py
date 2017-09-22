class Bookstore(object):
    def __init__(self, bookstore_name):
        self.name = bookstore_name
        self.book_inventory = []
        
        # This needs to be initialized for search_books
        self.results =[]
        
    def add_book(self, book):
        # Take in book variable and append to our book inventory
        self.book_inventory.append(book)
        
    
    def get_books(self):
        return self.book_inventory
    
    # Made None the default variable because it is falsey and we can use it below.
    def search_books(self, author = None):
        # I restarted this list becasue we want a new list everytime this is called
        self.results = []
        
        # When author is None the statement is false if it has a value it is truth
        if author:
            # We search through our list of objects in book_inventory which are 
            # instances of the Book() Class and because of this we can check the author
            # by doing book.author and compare it to the author given
            for book in self.book_inventory:
                if book.author == author:
                    # we append it to the results list for the  bookstore object
                    self.results.append(book)
        
        return self.results
    
    
class Author(object):
    # Use the magic method to initialize the instance of the object
    def __init__ (self, name, nationality):
        # adding the variables given when Author() is called
        self.name = name
        self.nationality = nationality
        # adding in a variable we need but was not given
        self.list_of_books = []
        
    def get_books(self):
        # Return the list of books the author is related to
        return self.list_of_books
        
        

class Book(object):
    # initializing book when Book() is called
    def __init__(self, title, author):
        # Adding variables given when Book() is called
        self.title = title
        self.author = author
        # Adding self (book just created) to the instance of the authors list
        # of books. ** From this object we are modifiying another object**
        author.list_of_books.append(self)
