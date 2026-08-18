class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


class Patron:

    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:

    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron_id, isbn):

        for p in self.patrons:

            if p.patron_id == patron_id:

                for b in self.books:

                    if b.isbn == isbn:

                        if b.is_borrowed == False:

                            b.borrow()
                            p.borrow_book(b)
                            print(p.name, "borrowed", b.title)

                        else:
                            print("Book is already borrowed")

                        return

        print("Book or Patron not found")

    def return_book(self, patron_id, isbn):

        for p in self.patrons:

            if p.patron_id == patron_id:

                for b in self.books:

                    if b.isbn == isbn:

                        if b in p.borrowed_books:

                            b.return_book()
                            p.return_book(b)
                            print(p.name, "returned", b.title)

                        else:
                            print("Book not borrowed by this patron")

                        return

        print("Book or Patron not found")

    def show_books(self):

        print("\nBooks in Library")

        for b in self.books:

            if b.is_borrowed:
                status = "Borrowed"
            else:
                status = "Available"

            print("---------------------")
            print("Title :", b.title)
            print("Author:", b.author)
            print("ISBN  :", b.isbn)
            print("Status:", status)

    def show_patrons(self):

        print("\nPatron Details")

        for p in self.patrons:

            print("---------------------")
            print("Name :", p.name)
            print("ID   :", p.patron_id)

            print("Borrowed Books :")

            if len(p.borrowed_books) == 0:
                print("None")
            else:
                for book in p.borrowed_books:
                    print(book.title)


# Main Program

library = Library()

b1 = Book("Python Basics", "Amit Shah", "101")
b2 = Book("Data Structures", "Riya Mehta", "102")
b3 = Book("DBMS", "Karan Patel", "103")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

p1 = Patron("Shreya", "P01")
p2 = Patron("Rahul", "P02")

library.register_patron(p1)
library.register_patron(p2)

library.show_books()

print("\nBorrowing Books")
library.borrow_book("P01", "101")
library.borrow_book("P02", "103")

library.show_books()
library.show_patrons()

print("\nReturning Book")
library.return_book("P01", "101")

library.show_books()
library.show_patrons()