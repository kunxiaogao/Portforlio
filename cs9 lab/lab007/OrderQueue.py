class OrderQueue:
    def __init__(self):
        self.OrderList = [0]
        self.OrderSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.OrderList[i].getTime() < self.OrderList[i // 2].getTime():
                tmp = self.OrderList[i // 2]
                self.OrderList[i // 2] = self.OrderList[i]
                self.OrderList[i] = tmp
            i = i // 2

    def addOrder(self,pizzaOrder):
        self.OrderList.append(pizzaOrder)
        self.OrderSize = self.OrderSize + 1
        self.percUp(self.OrderSize)

    def percDown(self,i):
        while (i * 2) <= self.OrderSize:
            mc = self.minChild(i)
            if self.OrderList[i].getTime() > self.OrderList[mc].getTime():
                tmp = self.OrderList[i]
                self.OrderList[i] = self.OrderList[mc]
                self.OrderList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.OrderSize:
            return i * 2
        else:
            if self.OrderList[i*2].getTime() < self.OrderList[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def processNextOrder(self):
        if self.OrderSize == 0:
            raise QueueEmptyException()
        retval = self.OrderList[1]
        self.OrderList[1] = self.OrderList[self.OrderSize]
        self.OrderSize = self.OrderSize - 1
        self.OrderList.pop()
        self.percDown(1)
        return retval.getOrderDescription()

class QueueEmptyException(Exception):
    pass