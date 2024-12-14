# There are fifty-two cards in a deck, each of which belongs to one of four suits and one of thirteen ranks. 
# The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in bridge). 
# The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. 
# Depending on the game that you are playing, an Ace may be higher than King or lower than 2.

# If we want to define a new object to represent a playing card, 
# it is obvious what the attributes should be: rank and suit. 
# It is not as obvious what type the attributes should be. 
# One possibility is to use strings containing words like 'Spade' for suits and 'Queen' for ranks. 
# One problem with this implementation is that it would not be easy to compare cards to see which had a higher rank or suit.

# An alternative is to use integers to encode the ranks and suits. 
# In this context, “encode” means that we are going to define a mapping between numbers and suits, 
# or between numbers and ranks. This kind of encoding is not meant to be a secret (that would be “encryption”).
# Spades	↦	3
# Hearts	↦	2
# Diamonds	↦	1
# Clubs	    ↦	0
# Jack	↦	11
# Queen	↦	12
# King	↦	13

class Card:
    """Represents a standard playing card.
    Attributes; suit:integer 0-3 ; rank:integer 1-13 """
    def __init__(self, suit=0, rank=2):#default card is 2 of clubs
        self.suit = suit
        self.rank = rank
        #suit and rank are instance attributes, associated with a particular instance of the class
# #example to create a card:
# queen_of_diamonds = Card(1, 12)
    # Variables below are defined inside a class but outside of any method
    # class attributes because they are associated with the class object Card
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']#None is place holder for the zeroth element
# Both instance and class attributes are accessed using dot notation
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
# For example, in __str__, self is a Card object, and self.rank is its rank. 
# Similarly, Card is a class object, and Card.rank_names is a list of strings associated with the class.
# Every card has its own suit and rank, but there is only one copy of suit_names and rank_names.

