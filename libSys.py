class Library:
    # initializing the object library
    def __init__(self, availableBooks):
        self.availableBooks = availableBooks

    def displayAvailableBook(self):
        print()
        print("Available Books: ")
        for key, value in self.availableBooks.items():  # print books
            print(key, ":", value)

    def lendBook(self, requested_book):
        if requested_book in self.availableBooks:
            print('You have now borrowed the book')
            self.availableBooks.pop(requested_book)
        else:
            print('Sorry,the book is not available in our list.')

    def addBook(self, return_book):
        i = 1
        while True:
            if i not in self.availableBooks:
                self.availableBooks[i] = return_book
                break
            i += 1
        print("You have returned the book, Thank you :) ")


class Customer:
    def __init__(self):
        self.book = None
        self.bookNo = None

    def requestBook(self):
        print("Enter the name of book you would like to borrow: ")
        self.bookNo = int(input())
        return self.bookNo

    def returnBook(self):
        print("Enter the name of book which you want to return")
        self.book = input()
        return self.book


books = {1: "Harry Potter and the Philosopher\'s Stone",
         2: "Think and grow rich",
         3: "Atomic Habits",
         4: "Who Will Cry When you Die"}
# object for library
library = Library(books)
# object for customer
customer = Customer()
while True:
    print("Enter a : Display available books")
    print("Enter b : Request the book")
    print("Enter c : Return the book")
    print("Enter d : Exit")
    userChoise = input()
    if userChoise == 'a':
        library.displayAvailableBook()
    elif userChoise == 'b':
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoise == 'c':
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoise == 'd':
        quit()





# ----------------------------------------------------------------------------------------------------------------------#
"""Implement a library management s/m which will handle following tasks:
   1.Customer should be able to display all the books available in the library
   2.Handle the process when a customer requested to borrow a book
   3.Update the library collection when the customer returns a book

   steps:
   --find out the nouns from problem: Customer, Library (class)
   --class => library
     layers of abstraction => display available book,to lend a book, to add a book
   --class => Customer
     layers of abstraction => request for a book, return a book
   --object => library
     at time of creation of our lib obj we want to initialize our lib obj with list of available books so pass the list
     we have to initialize it at obj creation with __int__ and we will pass listOfBook variable then create instance 
     variable and pass to it
     # display all books in method displayAvailableBook with for loop
     # ask customer for book in requestBook assign it to instance variable book and return it
     #once customer places request to borrow book, lib should lend it if book is available so book requested by customer 
     should accessed as para in lendBook method and check for it, if it is present then given  it and remove from list                                                                            
    #now when customer returns the book ,ask for book name then add into list with help of instance attribute book and 
    return attribute
   # add the book into lib list , it should accept the para returnBook
   --object => customer
   as customer what he wants to do
   """
# ---------------------------------------------------------------------------------------------------------------------#

