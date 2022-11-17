class Card:
    def __init__(self, suit, rank):
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.count = 1

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit.upper()

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank.upper()

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        return "{} {} | {}\n".format(self.suit, self.rank, self.count)

    def __lt__(self, rhs):
        if self.rank != rhs.rank:
            if self.rank == 'A':
                numl = 1
            elif self.rank == 'J':
                numl = 11
            elif self.rank == 'Q':
                numl = 12
            elif self.rank == 'K':
                numl = 13
            else:
                numl = int(self.rank)
            if rhs.rank == 'A':
                numr = 1
            elif rhs.rank == 'J':
                numr = 11
            elif rhs.rank == 'Q':
                numr = 12
            elif rhs.rank == 'K':
                numr = 13
            else:
                numr = int(rhs.rank)
            return numl < numr
        if self.suit != rhs.suit:
            return self.suit < rhs.suit
        return False

    def __gt__(self, rhs):
        if self.rank != rhs.rank:
            if self.rank == 'A':
                numl = 1
            elif self.rank == 'J':
                numl = 11
            elif self.rank == 'Q':
                numl = 12
            elif self.rank == 'K':
                numl = 13
            else:
                numl = int(self.rank)
            if rhs.rank == 'A':
                numr = 1
            elif rhs.rank == 'J':
                numr = 11
            elif rhs.rank == 'Q':
                numr = 12
            elif rhs.rank == 'K':
                numr = 13
            else:
                numr = int(rhs.rank)
            return numl > numr
        if self.suit != rhs.suit:
            return self.suit > rhs.suit
        return False

    def __eq__(self, rhs):
        return (self.suit == rhs.suit) and (self.rank == rhs.rank)

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        if self.parent:
            if self.parent.left:
                if self.parent.left == self:
                    return True
        return False

    def isRightChild(self):
        if self.parent:
            if self.parent.right:
                if self.parent.right == self:
                    return True
        return False

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, suit, rank, left, right, count):
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.left = left
        self.right = right
        self.count = count
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.right.findMin()
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def spliceOut(self):
        # Case 1:
        # If node to be removed is a leaf, set parent's left or right
        # child references to None
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None

        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent