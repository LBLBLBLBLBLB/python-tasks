class Book:
    def __init__(self, title, author, publication_year, available):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available = available
    
    def display_details(self):
        details = f'{self.title} by {self.author} in {self.publication_year} is'
        if self.available == True:
            return details + ' available'
        else:
            return details + ' not available'
    
    def get_book(self):
        if self.available:
            self.available = False
            return True
        print("Book is already checked out")
        return False
    
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        print("Book is already in the library")
        return False
        
book1 = Book('book1', 'author1', 100, False)
print(book1.display_details())
book1.return_book()
print(book1.display_details())
book1.get_book()
print(book1.display_details())
