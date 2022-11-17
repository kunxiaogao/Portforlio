from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.pizza = []
        self.time = time

    def getTime(self):
         return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizza.append(pizza)

    def getOrderDescription(self):
        totalprice = 0.00
        s = "******\n\
Order Time: {}\n".format(self.time)
        if self.pizza != []:
            for i in self.pizza:
                totalprice += i.getPrice()
                s += i.getPizzaDetails() + "\n----\n"
        s += "TOTAL ORDER PRICE: ${:.2f}\n\
******\n".format(totalprice)
        return s
