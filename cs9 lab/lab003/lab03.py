def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    return x + multiply(x,y-1)

def collectOddValues(listOfInt):
    if listOfInt == []:
        return []
    if listOfInt[0] % 2 == 0:
        return [] + collectOddValues(listOfInt[1:])
    if listOfInt[0] % 2 != 0:
        return [listOfInt[0]] + collectOddValues(listOfInt[1:])

def countInts(listOfInt, num):
    if listOfInt == []:
        return 0
    if listOfInt[0] == num:
        return 1 + countInts(listOfInt[1:], num)
    if listOfInt[0] != num:
        return 0 + countInts(listOfInt[1:], num)

def reverseString(s):
    if s == '':
        return ''
    return s[-1] + reverseString(s[:-1])

def removeSubString(s, sub):
    if s == '':
        return ''
    if s[0:len(sub)] == sub:
        return '' + removeSubString(s[len(sub):],sub)
    if s[0:len(sub)] != sub:
        return s[0] + removeSubString(s[1:],sub)