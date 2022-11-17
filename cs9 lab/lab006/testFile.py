from lab06 import mergesort,ensureSortedAscending,getNthApartment,getTopThreeApartments
from Apartment import Apartment

def test_Apartment():
    a = Apartment()
    assert a.getRent() == 0
    assert a.getMetersFromUCSB() == 0
    assert a.getCondition() == "N/A"
    b = Apartment(2400, 50, "average")
    assert b.getRent() == 2400
    assert b.getMetersFromUCSB() == 50
    assert b.getCondition() == "average"
    assert b.getApartmentDetails() == "(Apartment) Rent: $2400, Distance From UCSB: 50m, Condition: average"
    c = Apartment(2300,60,"bad")
    assert (b > c) == True
    assert (b < c) == False
    assert (b == c) == False
    c = Apartment(2400,60,"bad")
    assert (b < c) == True
    c = Apartment(2400, 50, "bad")
    assert (b < c) == True

def test_getNthApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    length = len(apartmentList)
    assert getNthApartment(apartmentList, 0) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert getNthApartment(apartmentList, length-1) == "(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    assert getNthApartment(apartmentList, 11) == "(Apartment) DNE"
def test_mergesort():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    length = len(apartmentList)
    mergesort(apartmentList)
    assert getNthApartment(apartmentList, 0) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getNthApartment(apartmentList, length-1) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test_ensureSortedAscending():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getTopThreeApartments():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert getTopThreeApartments(apartmentList) == '1st: (Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n' \
                                                   '2nd: (Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent\n' \
                                                   '3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average'