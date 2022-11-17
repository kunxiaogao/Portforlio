from lab03 import multiply,countInts,collectOddValues,reverseString,removeSubString
def test_multiply():
    assert multiply(5, 4) == 20
    assert multiply(1, 1) == 1
    assert multiply(0, 4) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0

def test_collectOddValues():
    assert collectOddValues([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert collectOddValues([1, 1, 1, 4, 5]) == [1, 1, 1, 5]
    assert collectOddValues([ 2, 4]) == []
    assert collectOddValues([]) == []

def test_countInts():
    assert countInts([1, 2, 3, 4, 3, 2, 1], 2) == 2
    assert countInts([1, 2, 3, 4, 3, 1], 2) == 1
    assert countInts([], 2) == 0
    assert countInts([1, 2, 3, 4, 3, 2, 1], 67) == 0

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("C") == "C"
    assert reverseString("kiki") == "ikik"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("Looo", "oo") == "Lo"
    assert removeSubString("L", "L") == ""
    assert removeSubString("Lolololol", "oL") == "Lolololol"

