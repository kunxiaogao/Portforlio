from Card import Card
class PlayerHand:
    def __init__(self):
        self.root = None  # A BST just needs a reference to the root node
        self.size = 0  # Keeps track of number of nodes

    def getTotalCards(self):
        return self.size

    def getMin(self):
        if self.size == 0:
            return None
        current = self.root
        while current.hasLeftChild():
            current = current.left
        return current

    def getMax(self):
        if self.size == 0:
            return None
        current = self.root
        while current.hasRightChild():
            current = current.right
        return current

    def get(self, suit, rank):
        if self.root:
            card = Card(suit, rank)
            res = self._get(card, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self, card, currentNode):
        if not currentNode:
            return None
        elif currentNode == card:
            return currentNode
        elif card < currentNode:
            return self._get(card, currentNode.left)
        else:
            return self._get(card, currentNode.right)

    def getSuccessor(self, suit, rank):
        if self.size == 0:
            return None
        a = self.get(suit, rank)
        if a:
            if self.getMax() == a:
                return None
            if a.right:
                b = a.findSuccessor()
                return b
            else:
                if a.isLeftChild():
                    return a.parent
                elif a.isRightChild():
                    current = a
                    while current.getParent() and current.isRightChild():
                        current = current.parent
                    return current.parent
        return None

    def put(self, suit, rank):
        card = Card(suit, rank)
        if self.get(suit, rank):
            self.get(suit, rank).count += 1
        else:
            if self.root:
                self._put(card, self.root)
            else:
                self.root = card
        self.size = self.size + 1

    def _put(self, card, currentNode):
        if card < currentNode:
            if currentNode.hasLeftChild():
                self._put(card, currentNode.left)
            else:
                currentNode.left = card
                currentNode.getLeft().setParent(currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(card, currentNode.right)
            else:
                currentNode.right = card
                currentNode.getRight().setParent(currentNode)

    def delete(self, suit, rank):
        card = Card(suit, rank)
        if self.size > 1:
            nodeToRemove = self._get(card, self.root)
            if nodeToRemove:
                if nodeToRemove.count == 1:
                    self.remove(nodeToRemove)  # remove modifies the tree
                    self.size = self.size - 1
                else:
                    nodeToRemove.count -= 1
                    self.size = self.size - 1
                return True
            else:
                return False
        elif self.size == 1 and self.root == card:
            self.root = None
            self.size = self.size - 1
            return True
        else:
            return False

    def remove(self, currentNode):
        # Case 1: Node to remove is leaf
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

        # Case 3: Node to remove has both children
        elif currentNode.hasBothChildren():
            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.setSuit(succ.getSuit())
            currentNode.setRank(succ.getRank())
            currentNode.setCount(succ.getCount())

        # Case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:  # currentNode is the Root
                    self.root = currentNode.getLeft()
                    self.root.setParent(None)

            # Node has rightChild
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    self.root = currentNode.getRight()
                    self.root.setParent(None)

    def isEmpty(self):
        return self.size == 0

    def inOrder(self):
        ret = self._inOrder(self.root)
        return ret

    def _inOrder(self, node):
        ret = ""
        if node:
            ret += self._inOrder(node.getLeft())
            ret += node.__str__()
            ret += self._inOrder(node.getRight())
        return ret

    def preOrder(self):
        ret = self._preOrder(self.root)
        return ret

    def _preOrder(self,node):
        ret = ""
        if node:
            ret += node.__str__()
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())
        return ret
