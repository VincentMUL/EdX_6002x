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

import random #module to shuffle the deck
class Card:
    """Represents a standard playing card.
    Attributes; suit:integer 0-3 ; rank:integer 1-13 
    With suits defined as
    0:Clubs, 1:Diamonds, 2:Hearts, 3:Spades
    """
    def __init__(self, suit=0, rank=2):#default card is 2 of clubs
        self.suit = suit
        self.rank = rank
        #suit and rank are instance attributes, associated with a particular instance of the class
# #example to create a (an instance) card:
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
#
# For programmer-defined types, you can control object comparison.
# By default, user-defined types are compared by object identity, 
# but you can override this behavior by providing an __lt__ method. (less than)
# Takes in two parameters, self and other, and returns True if self is strictly less than other.
# In order to compare cards, you might need to write a __lt__ method that compares ranks and suits.
    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        # suits are the same... check ranks
        return self.rank < other.rank
# More concisely written using tuple comparison:
#     def __lt__(self, other):
#         t1 = self.suit, self.rank
#         t2 = other.suit, other.rank
#         return t1 < t2
# This works because tuples are compared element by element: 
# the first item of t1 is compared to the first item of t2, and so on.

# # Now we can create a Card object and compare them using <:
# card1 = Card(1, 11)
# card2 = Card(3, 11)
# print(card1 < card2)
# # True, because 1 < 3

# Now that we have Cards, the next step is to define a Deck class.
# Since a deck is made up of cards, it is natural for each Deck to contain a list of cards as an attribute.

class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
# Efficient way to accumulate a large string is to use a list 
# and join the elements with the newline character. Cards are therefore seperated by newlines.
# Even though the result appears on 52 lines, it is one long string that contains newlines.
#
# To deal cards, we would like a method that removes a card from the deck and returns it.
# Deck is a list, so pop is an appropriate method to remove a card from the deck.
    def pop_card(self):
        return self.cards.pop() #dealing from the bottom of the deck!
# Adding a card is done with the append method. (no return)
    def add_card(self, card):
        self.cards.append(card)
# Method using another method without much work is called a veneer.
# In this case add_card is a thin method that expresses a list operation
# in terms appropriate for decks; improving appearance.
# Shuffling the deck is done with random.
    def shuffle(self):
        random.shuffle(self.cards)
# To sort the cards, we use the sort method from the list class.
    def sort(self):
        self.cards.sort()
# By default, list's sort uses the __lt__ method we defined to determine the order.
# The default behavior of sort is to sort by suit, then rank.
#
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
# Now that we have Deck and Card classes, the next step is to define a Hand class.
# Hand is similar to a deck. It holds cards and has methods for adding and removing cards.
# Hand is also different to a deck. For instance we may want to compare hands to other hands.
# Or compute a score for a hand in order to make a bid. 
# Similar, but different -> inheritance.
# Hand class inherits from Deck class, put the parent class in parentheses.
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
# This allows us to use methods from parent Deck on child Hand.
# Instead of populating the hand with a deck, we need an empty list of cards.
# So we can populate the Hand with cards from a Deck.
# Now when creating a Hand, the init method of Hand is called, not Deck.
# hand = Hand('new hand')
# print(hand.cards)
# # []
# print(hand.label)
# # new hand
# # Other methods are inherited from Deck, so we can deal a card like this:
# hand = Hand('new hand')
# deck = Deck()
# card = deck.pop_card()
# hand.add_card(card)
# print(hand)
# # King of Spades
# 
# Next step is to encapsulate in a method called move_cards.
# This method takes two arguments, a Hand object and the number of cards to deal.
# It modifies both self and hand, and returns None.
    # def move_cards(self, hand, num): #self can be either deck or hand and hand can also be a deck
    #     for i in range(num):
    #         hand.add_card(self.pop_card())
# This method is called polymorphic because it works with any Deck or Hand object.
# Inheritance is a way to define a new class that is modified from an existing class.
# Sometimes easy to facilitate code reuse, sometimes reflect natural structure of the problem.
# Making the design easier to understand, but sometimes making the code difficult to read.
# Relevant code may be spread across several modules.

# Class diagrams
# Class diagram shows abstract representation of the structure of a program.
# Each rectangle refrencing a point and each Deck containing references to many Cards.
# A HAS-A relationship, a rectangle has a point. (A Deck has a Card) Standard arrow.
# An IS-A relationship, a Hand is a kind of Deck. (Hand inherits from Deck) Arrow with hollow head.
# One class might depend on another, objects in 1 class take objects in another class as parameters.
# This is a dependency, shown with a dashed arrow.
# A star over the HAS-A arrow, indicating multiplicity. (A Deck has many Cards) 52 indicating 52 cards.
# No dependencies in this case.

# Debugging is sometimes tricky, because might be hard to figure out which method will be invoked.
# Especially with inheritance, because it depends on the type of the object.
# Simplest solution: add print statements to the beginning of methods.
# Or a function providing the definition of the method:
def find_defining_class(obj, method_name):
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
# mro stands for method resolution order, a list of classes that will be searched for methods.
# It's the sequence of classes Python checks when looking to resolve a method invocation.
# hand = Hand()
# print(find_defining_class(hand, 'shuffle'))
# # <class '__main__.Deck'>

# !!!!!!!!!!!!!!!!!!
# Design suggestion:
# When you override a method, the interface of the new method should be the same as the old.
# Same parameters, return same type and obey same preconditions and postconditions. 
# If you follow this rule, any function designed to work with an instance of a parent class 
# will also work with an instance of a child class.
# !!!!!!!!!!!!!!!!!!
# Violating this rule is called the Liskov substitution principle,
# named after Barbara Liskov, who proposed it. 
# Formally, the Liskov substitution principle is stated as:
# If S is a subtype of T, then objects of type T may be replaced with objects of type S
# without altering any of the desirable properties of that program.
# In this case, Deck is a subtype of Hand, so any method that works with a Deck should also work with a Hand.

# Above was an example of Object Oriented Design where there is a connection to the real world.
#   Wrapping a piece of code up in a function is called encapsulation. 
#   Serving as documentation and easier reuse of code.
#   Adding a parameter to a function is called generalization, because it makes the function more general.
#   Replacing specific values with variables is called parameterization.
#   Rearranging a program to improve interfaces and facilitate code reuse is called refactoring.
#   (Changing design without changing behavior)
# In the same way, data encapsulation is the process of wrapping up data in a single unit.
# Data encapsulation is identifying data that naturally belong together and grouping them 
# into a coherent unit —usually a class— before deciding on or refining the methods that operate on them.
# This suggests the following development plan:
    # 1. Start by writing functions that read and write global variables (when necessary).
    # 2. Once you get the program working, look for associations between global variables 
    #    and the functions that use them.
    # 3. Encapsulate related variables as attributes of an object.
    # 4. Transform the associated functions into methods of the new class.
