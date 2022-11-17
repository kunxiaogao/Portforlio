from Shape2D import Shape2D
class Circle(Shape2D):
    def __init__(self, color=None, radius=None):
        Shape2D.__init__(self,color)
        self.radius = radius
        if radius != None:
            self.area = 3.14159*(self.radius)**2
            self.perimeter = 2*3.14159*self.radius
        else:
            self.area = None
            self.perimeter = None
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def computeArea(self):
        if self.radius != None:
            self.area = 3.14159 * (self.radius) ** 2
        return self.area
    def computePerimeter(self):
        if self.radius != None:
            self.perimeter = 2 * 3.14159 * self.radius
        return self.perimeter
    def getShapeProperties(self):
        return "Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}".format(self.color,self.radius,self.area,self.perimeter)

