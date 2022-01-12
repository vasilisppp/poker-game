from util import cardValue
import random

def poker(hands):
    return [h for h in hands if h==max(hands,key = lambda h: h.getRank())]

class hand():
    def __init__(self, cardString: str):
        self.setHand(cardString)
    
    def setHand(self, cardString: str):
        self._cardString = cardString
        self._cards = cardString.split()
        self._cardRanks = [cardValue(c[0]) for c in self._cards]
        self._cardRanksSorted = sorted(self._cardRanks, reverse=True)

    def getCardString(self):
        return self._cardString
    
    def getCards(self):
        return self._cards

    def getRank(self):
        if self.straight() and self.flush():
            return (9,self.straight(),0)
        elif self.kind(4):
            return(8,self.kind(4),self.kind(1))
        elif self.kind(3) and self.kind(2):
            return (7,self.kind(3),self.kind(2))
        elif self.flush():
            return (6,self._cardRanksSorted,0)
        elif self.straight():
            return (5,self._cardRanksSorted[0],0)
        elif self.kind(3):
            return (4,self.kind(3),self._cardRanksSorted)
        elif self.twoPair():
            return (3,self.twoPair(),self._cardRanksSorted)
        elif self.kind(2):
            return (2,self.kind(2),self._cardRanksSorted)
        else:
            return (1,self._cardRanksSorted,0)

    def getCardRanks(self):
        return self._cardRanks

    def getCardRanksSorted(self):
        return self._cardRanksSorted

    def flush(self):
        colors = [c[1] for c in self._cards]
        return len(set(colors))==1

    def straight(self):
        if len(set(self._cardRanksSorted))==5:
            if self._cardRanksSorted[0]-self._cardRanksSorted[-1]==4:
                # Ace first straight
                return self._cardRanksSorted[0] 
            elif self._cardRanksSorted[0]==14 and self._cardRanksSorted[1]-self._cardRanksSorted[-1]==3:
                return self._cardRanksSorted[1]
            else:
                return 0
        else:
            return 0
    
    def kind(self,kindSize:int):
        # returns rank of kind
        return next((r for r in self._cardRanksSorted if self._cardRanksSorted.count(r)==kindSize),0)

    def twoPair(self):
        tp = tuple(sorted([r for r in set(self._cardRanksSorted) if self._cardRanksSorted.count(r)==2],
                reverse=True))
        return tp if len(tp)==2 else 0


class deck(list):
    def __init__(self,shuffle=True):
        super().__init__((r+s for r in '23456789TJQKA' for s in 'HDSC'))
        if shuffle:
            self.shuffleCards()

    def shuffleCards(self):
        random.shuffle(self)
    
    def dealHand(self,n=5):
        cardsToDeal=""
        for i in range(n):
            cardsToDeal += self.pop()
            if i!=n-1:
                cardsToDeal += ' '
        return hand(cardsToDeal)