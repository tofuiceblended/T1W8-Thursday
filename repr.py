class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
    
# Ceating an instance of Book
book1 = Book("1984", "George Orwell", 1949)

# Using repr to get the string representation
print(repr(book1))

# Printing the object directly also calls __repr__
print(book1)
