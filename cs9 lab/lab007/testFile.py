from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
def test_pizza():
    a = Pizza('S')
    assert a.getPrice() == 0.00
    assert a.getSize() == 'S'
    a.setSize('L')
    a.setPrice(12.00)
    assert a.getPrice() == 12.00
    assert a.getSize() == 'L'

def test_Custompizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("sausage")
    assert cp2.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $14.00\n"


def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"


def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000)
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_OrderQueue():
    a = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order1 = PizzaOrder(123000)
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    order2 = PizzaOrder(133030)
    order2.addPizza(cp1)
    order3 = PizzaOrder(220000)
    order3.addPizza(sp1)
    a.addOrder(order3)
    a.addOrder(order2)
    a.addOrder(order1)
    assert a.OrderList[1].getTime() == 123000
    assert a.processNextOrder() == "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"
    assert a.OrderList[1].time == 133030
    order4 = PizzaOrder(100000)
    order4.addPizza(sp1)
    a.addOrder(order4)
    assert a.OrderList[1].getTime() == 100000

