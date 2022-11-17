from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        Pizza.__init__(self,size)
        self.toppings = []
        if self.size == 'S':
            self.price = 8.00
        elif self.size == 'M':
            self.price = 10.00
        elif self.size == 'L':
            self.price = 12.00

    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == 'S':
            self.price += 0.50
        elif self.size == 'M':
            self.price += 0.75
        elif self.size == 'L':
            self.price += 1.00

    def getPizzaDetails(self):
        if self.toppings == []:
            return "CUSTOM PIZZA\nSize: {}\nToppings:\nPrice: ${:.2f}\n".format(self.size,self.price)
        else:
            s = ""
            for i in self.toppings:
                s += "\t+ {}\n".format(i)
            return "CUSTOM PIZZA\nSize: {}\nToppings:\n".format(self.size) + s + "Price: ${:.2f}\n".format(self.price)

