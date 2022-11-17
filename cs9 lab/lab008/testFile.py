from Card import Card
from PlayerHand import PlayerHand
def test_basic():
    a = PlayerHand()
    assert a.root == None
    assert a.size == 0
    assert a.isEmpty() == True

def test_inOrder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.inOrder() == "D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"

def test_preOrder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.preOrder() == "D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"

def test_Min():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    a = Card('D', 'A')
    assert hand.getMin() == a

def test_Max():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    a = Card('S', 'K')
    assert hand.getMax() == a

def test_delete1():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    hand.delete('S', 'K')
    assert hand.preOrder() == "D A | 1\n\
S K | 1\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"

def test_delete2():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    hand.delete('C', 'Q')
    assert hand.preOrder() == "D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C K | 1\n\
H 7 | 1\n"

def test_total():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    hand.delete('C', 'Q')
    assert hand.getTotalCards() == 6
    hand.delete('C', 'Q')
    assert hand.getTotalCards() == 6
    hand.delete('S', 'K')
    assert hand.getTotalCards() == 5
    hand.delete('H', '7')
    assert hand.getTotalCards() == 4
