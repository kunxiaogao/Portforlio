from BookCollectionNode import BookCollectionNode
from Book import Book
from BookCollection import BookCollection
def test_Book():
    a = Book()
    assert a.getBookDetails() == 'Title: , Author: , Year: None'
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getTitle() == 'Ready Player One'
    assert b.getYear() == 2011
    assert b.getAuthor() == 'Cline, Ernest'
    assert b.getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'
    c = Book("Ready Player One", "Brane, Ernest", 2011)
    assert (b > c) == True
    c = Book("Ready Player One", "Cline, Ernest", 2012)
    assert (b > c) == False
    c = Book("Player One", "Cline, Ernest", 2011)
    assert (b > c) == True

def test_BookCollectionNode():
    a = BookCollectionNode(1)
    assert a.getData() == 1
    assert a.getNext() == None
    a.setData(2)
    assert a.getData() == 2
    a.setNext(3)
    assert a.getNext() == 3

def test_createList():
    ll = BookCollection()
    assert ll.isEmpty() == True
    assert ll.getNumberOfBooks() == 0

def test_insertBook():
    bc = BookCollection()
    assert bc.isEmpty() == True
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 4
    assert bc.getBooksByAuthor("KING, Stephen") == 'Title: Rage, Author: King, Stephen, Year: 1977\n' \
                                                   'Title: The Shining, Author: King, Stephen, Year: 1977\n' \
                                                   'Title: Cujo, Author: King, Stephen, Year: 1981\n'
def test_AllBooksInCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n'\
                                           'Title: Rage, Author: King, Stephen, Year: 1977\n'\
                                           'Title: The Shining, Author: King, Stephen, Year: 1977\n' \
                                           'Title: Cujo, Author: King, Stephen, Year: 1981\n'