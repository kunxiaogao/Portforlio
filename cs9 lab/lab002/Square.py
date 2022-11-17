from Shape2D import Shape2D
class Square(Shape2D):
    def __init__(self, color=None, side=None):
        Shape2D.__init__(self, color)
        self.side = side
        if side != None:
            self.area = self.side ** 2
            self.perimeter = 4 * self.side
        else:
            self.area=None
            self.perimeter=None

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        if self.side != None:
            self.area = self.side ** 2
        return self.area

    def computePerimeter(self):
        if self.side != None:
            self.perimeter = 4 * self.side
        return self.perimeter

    def getShapeProperties(self):
        return "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}".format(self.color, self.side, self.area,
                                                                                 self.perimeter)