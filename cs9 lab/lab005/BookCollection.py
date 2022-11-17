from BookCollectionNode import BookCollectionNode
from Book import Book
class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        temp = self.head
        s = ''
        while temp != None:
            if temp.getData().getAuthor().upper() == author.upper():
                s += temp.getData().getBookDetails()+'\n'
            temp = temp.getNext()
        return s

    def getAllBooksInCollection(self):
        temp = self.head
        s = ''
        while temp != None:
            s += temp.getData().getBookDetails() + '\n'
            temp = temp.getNext()
        return s

