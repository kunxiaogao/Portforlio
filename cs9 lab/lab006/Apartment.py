class Apartment:
    def __init__(self, rent = 0, metersFromUCSB = 0, condition = "N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent,self.metersFromUCSB,self.condition)

    def __lt__(self,rhs):
        if self.rent != rhs.rent:
            return self.rent < rhs.rent
        if self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB < rhs.metersFromUCSB
        if self.condition != rhs.condition:
            return len(self.condition) > len(rhs.condition)
        return False

    def __gt__(self,rhs):
        if self.rent != rhs.rent:
            return self.rent > rhs.rent
        if self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB > rhs.metersFromUCSB
        if self.condition != rhs.condition:
            return len(self.condition) < len(rhs.condition)
        return False

    def __eq__(self, rhs):
        return self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition

