class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        if species != None:
            self.species=species.upper()
        elif species == None:
            self.species = species
        if weight != None:
            self.weight=float(weight)
        elif weight == None:
            self.weight = weight
        if age != None:
            self.age=int(age)
        elif age == None:
            self.age = age
        if name != None:
            self.name=name.upper()
        elif name == None:
            self.name = name
    def setSpecies(self, species):
        self.species=species.upper()
    def setWeight(self, weight):
        self.weight=float(weight)
    def setAge(self, age):
        self.age=int(age)
    def setName(self, name):
        self.name=name.upper()
    def toString(self):
        return "Species: {}, Name: {}, Age: {}, Weight: {}"\
              .format(self.species, self.name,self.age,self.weight)
