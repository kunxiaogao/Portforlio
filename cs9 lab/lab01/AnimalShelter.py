from Animal import Animal
class AnimalShelter:
    def __init__(self):
        self.AnimalShelter = {}
    def addAnimal(self, animal):
        if self.AnimalShelter.get(animal.species) == None:
            self.AnimalShelter[animal.species] = [animal]
        elif animal not in self.AnimalShelter[animal.species]:
            self.AnimalShelter[animal.species].append(animal)
    def removeAnimal(self, animal):
        if self.AnimalShelter.get(animal.species) != None:
            for i in self.AnimalShelter[animal.species]:
                if i.species == animal.species and i.weight == animal.weight and i.age == animal.age and i.name == animal.name:
                    self.AnimalShelter[animal.species].remove(i)
    def getAnimalsBySpecies(self, species):
        string = ""
        if self.AnimalShelter.get(species.upper()) == None:
            return ""
        elif self.AnimalShelter.get(species.upper()) != None:
            for j in self.AnimalShelter.get(species.upper()):
                if j != self.AnimalShelter.get(species.upper())[-1]:
                    string += j.toString()+ "\n"
                elif j == self.AnimalShelter.get(species.upper())[-1]:
                    string += j.toString()
        return string
    def doesAnimalExist(self, animal):
        if self.AnimalShelter.get(animal.species) != None:
            for i in self.AnimalShelter[animal.species]:
                if i.species == animal.species and i.weight == animal.weight and i.age == animal.age and i.name == animal.name:
                    return True
            return False
        else:
            return False