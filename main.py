AvailableBookList = ["Think and Grow Rich", "Who Moved My Cheese"]
rented_books = []
print("Welcome to AtoZ Bookstore\n")
while 1:
    class Library:
        def __init__(self, bookslist):
                self.bookslist = bookslist

        @property
        def listallbook(self):
            return f"List of all books are -> {self.bookslist}"

        def __add__(self, bookname):
            self.bookslist.append(bookname)
            return f"{bookname} is successfully added in the library here is the updated list of available books {self.bookslist}"

        def rentbook(self, bookname, personname):
            if bookname not in self.bookslist:
                return f"Can't rent the book may be This book '{bookname}' is not available in the library"
            self.bookslist.remove(bookname)
            rented_books.append(bookname)

            return f" The book '{bookname}' is successfully rented to'{personname}' and now available booklist are '{self.bookslist}'"

        def returnbook(self, bookname):
            if bookname in rented_books:
                rented_books.remove(bookname)
                self.__add__(bookname)
            else:
                return f"Sorry!! {bookname} is never rented from this store"
            return f" The book '{bookname}' is successfully returned to library and now available booklist are '{self.bookslist}'"

    var = Library(AvailableBookList)

    ask = int(input("\npress 1 for list all books\n press 2 for add"
                    "book\n press 3 for rent book\n press 4 for return book\n"))

    if ask == 1:
        print(var.listallbook)
    elif ask == 2:
        ip = input("plz enter the book name\n")
        print(var.__add__(ip))
    elif ask == 3:
        ip = input("which book do u want to rent\n")
        ip1 = input("what is your name\n")
        print(var.rentbook(ip, ip1))
    else:
        bookname = input("Enter bookname\n")
        print(var.returnbook(bookname))
