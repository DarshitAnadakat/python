class Book:
    def __init__(self, title, author, publisher, edition, year, price, book_type):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.edition = edition
        self.year = year
        self.price = price
        self.book_type = book_type
        
class Library:
    def __init__(self):
        self.books = []

    def addBook(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publisher = input("Enter book publisher: ")
        edition = input("Enter book edition: ")
        year = input("Enter year of publication: ")
        price = input("Enter book price: ")
        book_type = input("Enter book type (reference or text book): ")
        book = Book(title, author, publisher, edition, year, price, book_type)
        self.books.append(book)
        print("Book added successfully.")

    def modifyBook(self):
        title = input("Enter book title to modify: ")
        for book in self.books:
            if book.title == title:
                book.author = input("Enter new author name: ")
                book.publisher = input("Enter new publisher name: ")
                book.edition = input("Enter new edition: ")
                book.year = input("Enter new year of publication: ")
                book.price = input("Enter new book price: ")
                book.book_type = input("Enter new book type (reference or text book): ")
                print("Book modified successfully.")
                return
        print("Book not found.")

    def deleteBook(self):
        title = input("Enter book title to delete: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book deleted successfully.")
                return
        print("Book not found.")

    def searchBook(self):
        title = input("Enter book title to search: ")
        for book in self.books:
            if book.title == title:
                print("Title:", book.title)
                print("Author:", book.author)
                print("Publisher:", book.publisher)
                print("Edition:", book.edition)
                print("Year of publication:", book.year)
                print("Price:", book.price)
                print("Book type:", book.book_type)
                return
        print("Book not found.")

    def listBooks(self):
        if len(self.books) == 0:
            print("No books available.")
            return
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("Publisher:", book.publisher)
            print("Edition:", book.edition)
            print("Year of publication:", book.year)
            print("Price:", book.price)
            print("Book type:", book.book_type)
            print()

    def sortedView(self):
        sort_by = input("Enter sort by criteria (title, author, publisher, year, price): ")
        if sort_by == "title":
            sorted_books = sorted(self.books, key=lambda book: book.title)
        elif sort_by == "author":
            sorted_books = sorted(self.books, key=lambda book: book.author)
        elif sort_by == "publisher":
            sorted_books = sorted(self.books, key=lambda book: book.publisher)
        elif sort_by == "year":
            sorted_books = sorted(self.books, key=lambda book: book.year)
        