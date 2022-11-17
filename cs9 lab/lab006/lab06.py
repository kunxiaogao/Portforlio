from Apartment import Apartment
def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList):
    for i in range(0,len(apartmentList)-1):
        if apartmentList[i] > apartmentList[i+1]:
            return False
        return True

def getNthApartment(apartmentList, n):
    if n >= len(apartmentList):
        return "(Apartment) DNE"
    return apartmentList[n].getApartmentDetails()

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    if len(apartmentList) <= 3:
        s = ""
        for i in range(len(apartmentList)-1):
            if i == 0:
                place = '1st: '
            elif i == 1:
                place = '2nd: '
            s += place + apartmentList[i].getApartmentDetails() + "\n"
        if len(apartmentList)-1 == 0:
            place = '1st: '
        elif len(apartmentList)-1 == 1:
            place = '2nd: '
        elif len(apartmentList)-1 == 2:
            place = '3rd: '
        s += place + apartmentList[-1].getApartmentDetails()
    else:
        s = ""
        for i in range(2):
            if i == 0:
                place = '1st: '
            elif i == 1:
                place = '2nd: '
            s += place + apartmentList[i].getApartmentDetails() + "\n"
        s += "3rd: " + apartmentList[2].getApartmentDetails()
    return s

