import unittest
from poker import *

class HandTest(unittest.TestCase):
    def testConstructor(self):
        stString = "AS JC QH KH TH"
        st = hand(stString)
        self.assertEquals(st.getCardString(),stString)
        self.assertEquals(st.getCards(),stString.split())
        self.assertEquals(st.getCardRanks(),[14,11,12,13,10])
        self.assertEquals(st.getCardRanksSorted(),[14,13,12,11,10])
        fhString = "5H 5S 5C 3S 3H"
        fh = hand(fhString)
        self.assertEquals(fh.getCardRanks(),[5,5,5,3,3])
        
    def testStraight(self):
        self.assertEquals(hand("AS JC QH KH TH").straight(),14)
        self.assertEquals(hand("9S JC QH KH TH").straight(),13)
        self.assertEquals(hand("AS 2S 3S 4S 5C").straight(),5)
        self.assertEquals(hand("2S JC QH KH TH").straight(),0)

    def testFlush(self):
        self.assertEquals(hand("AH JH QH KH TH").flush(),1)
        self.assertEquals(hand("AH JH QH KS TH").flush(),0)

    def testKind(self):
        # 1 of a kind
        self.assertEquals(hand("AH JH 2S KH TH").kind(1),14)
        # 2 of a kind
        self.assertEquals(hand("AH AS 3H 3S 5H").kind(2),14)
        self.assertEquals(hand("AH AS 3H 3S 5H").kind(2),14)
        # 3 of a kind
        self.assertEquals(hand("5H 5S 5C 3S 3H").kind(3),5)        
        self.assertEquals(hand("3S 3H 5H 5S 5C").kind(3),5)
        self.assertEquals(hand("3S 5D 5H 5S 5C").kind(3),0)
        # 4 of a kind
        self.assertEquals(hand("3S 3H 5H 5S 5C").kind(4),0)
        self.assertEquals(hand("3S 5D 5H 5S 5C").kind(4),5)
        
    def testTwoPair(self):
        self.assertEquals(hand("AH AS 3H 3S 5H").twoPair(),(14,3))
        self.assertEquals(hand("3S 5D 5H 5S 5C").twoPair(),0)

    def testGetRank(self):
        # Straight Flush
        self.assertEquals(hand("AS JS QS TS KS").getRank(),(9,14,0))
        self.assertEquals(hand("9S JS QS TS KS").getRank(),(9,13,0))
        # Four of a kind
        self.assertEquals(hand("3S AH AS AD AC").getRank(),(8,14,3))
        # Full house
        self.assertEquals(hand("3S 3H AS AD AC").getRank(),(7,14,3))
        # Flush
        self.assertEquals(hand("8S JS QS TS KS").getRank(),(6,[13,12,11,10,8],0))
        # Straight
        self.assertEquals(hand("9S JS QS TS KD").getRank(),(5,13,0))
        # Three of a kind
        self.assertEquals(hand("5S 5S 5S TS KD").getRank(),(4,5,[13,10,5,5,5]))
        # Two pair
        self.assertEquals(hand("3H AS AH 3S 5H").getRank(),(3,(14,3),[14,14,5,3,3]))
        # One pair
        self.assertEquals(hand("3H AS JH 3S 5H").getRank(),(2,3,[14,11,5,3,3]))
        # Nothing
        self.assertEquals(hand("3H AS JH QS 5H").getRank(),(1,[14,12,11,5,3],0))


class DeckTest(unittest.TestCase):
    def testConstructor(self):
        d1 = deck(False)
        self.assertEquals(len(d1),52)
        self.assertEquals(d1[0],'2H')
        self.assertEquals(d1[-1],'AC')
        d1 = deck(True)
        self.assertNotEquals(d1[0],'2H')
    
    def testDeal(self):
        d1 = deck(False)
        h1 = d1.dealHand()
        self.assertEquals(h1.getCards(),['AC', 'AS', 'AD', 'AH', 'KC'])
