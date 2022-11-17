from Shape2D import Shape2D
from Circle import Circle
from Square import Square

def test_Shape2D():
    assert Shape2D("blue").getShapeProperties() == "Shape: N/A, Color: blue"
    assert Shape2D().getShapeProperties() == "Shape: N/A, Color: None"
    a = Shape2D("red")
    assert a.getColor() == "red"
    a.setColor("yellow")
    assert a.getColor() == "yellow"

def test_Circle():
    c = Circle("blue", 2.5)
    d = Circle()
    assert c.getRadius() == 2.5
    assert d.getRadius() == None
    assert c.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 2.5, Area: 19.6349375, Perimeter: 15.70795"
    assert d.getShapeProperties() == "Shape: CIRCLE, Color: None, Radius: None, Area: None, Perimeter: None"
    c.setRadius(3)
    assert c.computeArea() == 28.27431
    assert c.computePerimeter() == 18.849539999999998
    assert c.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 3, Area: 28.27431, Perimeter: 18.849539999999998"

def test_Square():
    e = Square("blue", 2.5)
    f = Square()
    assert e.getSide() == 2.5
    assert f.getSide() == None
    assert e.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 2.5, Area: 6.25, Perimeter: 10.0"
    assert f.getShapeProperties() == "Shape: SQUARE, Color: None, Side: None, Area: None, Perimeter: None"
    e.setSide(3)
    assert e.computeArea() == 9
    assert e.computePerimeter() == 12
    assert e.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 3, Area: 9, Perimeter: 12"

