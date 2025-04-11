class Card():
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'    
    
    
c = Card("Ace","Spade")
print(c)
print(str(c))
print(repr(c))