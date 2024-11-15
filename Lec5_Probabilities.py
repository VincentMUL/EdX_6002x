import random
random.seed(0)

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def testRoll(n=10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

def squareRoot(x, epsilon):
    """Assumes x and epsilon are positive floats & epsilon < 1
    Returns a float y such that y*y is within epsilon of x"""
    y = 0
    while abs(y*y - x) >= epsilon:
        y += epsilon

# This is indeed a stochastical process.
# The probability is about counting possible events.
# Count the number of events of interest and divide by the total number of events.
# Probability of 11111 is 1/6^5
# Probability of 12345 is 1/6^5

# Three basic facts about probability:
# 1. The probability p of an event occuring is between 0 and 1.
# 2. The probability of an event not occuring is 1-p.
# 3. Multiplication rule:
#   When events are independent, the probability of 
#   all of the events occuring is the product 
#   of the probabilities of the individual events.
# Two events are independent if the outcome of one event
# has no influence on the outcome of the other.

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability =', round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability =', round(estProbability, 8))

# runSim('11111', 1000)
# #Cheated! This wasn't stochastic. It was deterministic, because random.seed(0) was used..
# #They are pseudorandom, they work by reading some random value.
# #Seed generates a random number, but it is not truly random.
# #Since we are using the same seed everytime I run this program, I'll get the same answer.
# # Super convenient for debugging, but not for real world applications!
# #Why did we get the same wrong answer twice? Because the probability is <1/1000.
# #And we tried only 1000 times. We need to try more times to get a better estimate.
# runSim('11111', 1000000)
# # When only trying a small number of trials for a rare event,
# # we may get an estimate that is wrong.

# How many trials do we need?
# Example: How common are boxcars?
# Boxcars: 6 on both dice.
# Probability of boxcars is 1/36 (1/(6**2))
# Other way to calculate: 1/6 * 1/6 = 1/36 (given two dice rolls are independent)
# Simulation:

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests

print('Frequency of boxcars =', str(fracBoxCars(100000)*100) + 
      '%')

# Moral 1: The more trials, the more accurate the estimate.
#(Later we'll see how to calculate the number of trials we need.)
# Moral 2: Do not confuse sample probability with actual probability.
# Moral 3: These sims were silly. Many cases this is not the case.

# EXERCISE 5:
# In this problem, we're going to calculate some probabilities of dice rolls. 
# Imagine you have two fair four-sided dice (if you've never seen one, google). 
# The result, a number between 1 and 4, is displayed at the top of the die on each of the 3 visible sides. 
# 'Fair' here means that there is equal probability of rolling any of the four numbers.

# You can answer the following questions in one of two ways - 
# you can calculate the probability directly, or, if you're having trouble, 
# you can simply write out the entire sample space for the problem. 
# A sample space is defined as a listing of all possible outcomes of a problem,
# and it can be written in many ways - a tree or a grid are popular options. 
# For example, look up a diagram of the sample space for 3 coin tosses.

# Some vocabulary before we begin: 
# an event is a subset of the sample space,
# or, a collection of possible outcomes. 
# A probability function assigns an event, A, a probability P(A) 
# that represents the likelihood of event A occuring.

# As an example, let's say we flip a coin. 
# Define the event H as the event that the coin comes up heads. 
# We can assign the probability P(H) = 1/2; the likelihood that event H occurs.

# The following problems will ask for the probability that a given event occurs.

# What is the size of the sample space for one roll of a four sided die?
# 4
# What is the size of the sample space for two rolls of a four sided die?
# 16 (4**2)
# Assume we roll 2 four sided dice. What is P({sum of the rolls is even})? 
# Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 1/2
# Assume we roll 2 four sided dice. What is P({rolling a 2 followed by a 3})? 
# 1/16
# Assume we roll 2 four sided dice. What is P({rolling a 2 and a 3, in any order})?
# 1/8
# Assume we roll 2 four sided dice. What is P({sum of the rolls is odd})?
# 1/2
# 
# Assume we roll 2 four sided dice. What is P({first roll equal to second roll})?
# 1/4 (= 4 * 1/16)
# Note: Another way of thinking about this is 
# that it doesn't matter what the first roll is, 
# just that the second roll matches it. 
# So, the probability of that event is 
# (4/4) * (1/4) = 1/4: 4/4 for the first roll (we don't care what it is), 
# times 1/4 chance that the second roll matches the first roll.
# 
# Assume we roll 2 four sided dice. What is P({first roll larger than second roll})?
# 3/8 = 0/16 + 1/16 + 2/16 + 3/16
# Assume we roll 2 four sided dice. What is P({at least one roll is equal to 4})?
# 1/4 + 1/4 - 1/16 = 7/16
# Assume we roll 2 four sided dice. What is P({neither roll is equal to 4})?
# 9/16 =  1 - 7/16

# EXERCISE 6:
# In this problem, we're going to calculate some various probabilities.

# What is the size of the sample space for two rolls of a ten sided die?
# 10**2 = 100
# What is the size of the sample space for three rolls of an eight sided die?
# 8**3=512
# What is the size of the sample space for drawing one card from a deck of 52 cards?
# 52
# What is the size of the sample space for drawing one card from each of two decks of 52 cards? 
# That is, drawing one card from one deck of cards, 
# then a second card from a second deck of cards.
# 52**2 = 2704
# Assume we roll 2 ten sided dice. 
# What is P({rolling a 2 followed by a 3})?
# 1/100
# Assume we roll 2 ten sided dice. 
# What is P({first roll larger than second roll})?
# 45/100 = 0/100 + 1/100 + 2/100 + ... + 8/100 + 9/100
# Assume we roll 3 eight sided dice. 
# What is P({all three rolls are equal})?
# 8/512 = 1/64
# Another way to think of it: it doesn't matter what the first roll is, 
# but the second and third rolls must match the first roll. 
# So the probability can be expressed as (8/8) * (1/8) * (1/8) = 1/64.
#
# A standard deck of cards contains 52 cards, 
# 13 each of four suits - diamonds, clubs, hearts, and spades. 
# Each suit contains one of 13 cards: A (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king). 
# Given one deck of 52 playing cards, you flip one over. 
# Assuming a fair deck, what is P({ace of hearts})?
# 1/52
# Assuming a fair deck, what is P({drawing a card with suit spades})?
# 13/52 = 1/4
# Assuming a fair deck, what is P({ace of any suit})?
# 4/52 = 1/13
# Assuming a fair deck, what is P({any card except an ace})?
# 48/52 = 12/13 or 1-1/13
# 
# Given one deck of 52 playing cards, you draw two random cards. 
# (The cards are drawn at the same time, 
# so the selection is considered without replacement) 
# Assuming a fair deck, what is P({both cards are aces})?
# 4/52 * 3/51 = 1/221
#
# Given two decks of 52 playing cards, you flip one over from each deck. 
# Assuming fair decks, what is P({the two cards are the same suit})?
# 1/4
# This is an interesting problem. 
# There are a few ways of calculating this, 
# but a very simple way is to note that 
# it doesn't matter what suit the first card is; 
# what matters is that the second card's suit 
# matches the suit of the first card.

# EXERCISE 7:
# You pick three balls in succession 
# out of a bucket of 3 red balls and 3 green balls. 
# Assume replacement after picking out each ball. 
# What is the probability of each of the following events?
#
# Three red balls: A : {R,R,R}.
# 1/8
# The sequence red, green, red: A : {R,G,R}.
# 1/8
# Any sequence with 2 reds and 1 green.
# 3/8
# Any sequence where the number of reds is greater than or equal to the number of greens.
# 1/8 + 3/8 = 1/2
#
# You have a bucket with 3 red balls and 3 green balls. 
# This time, assume you don't replace the ball after taking it out. 
# What is the probability of drawing 3 balls of the same color?
# 2/5 * 1/4 = 1/10
# My Explanation: I assumed the first ball did not matter, 
# the rest just had to match it.
# Class explanation: In this problem, we don't assume the balls 
# are replaced after being drawn. This changes the probability 
# because with every draw, there is one less ball to pick from. 
# The probability of drawing three red balls is 3/6 * 2/5 * 1/4 
# -- for the first pick, there are three red balls available 
# and six balls total. For the second pick, if we picked a red ball 
# first, there are now two red balls available and five balls total. 
# For the third pick, if both the first and second picks were red balls,
# there is now one red ball available and four balls total. 
# Multiply together to get P({R, R, R}) = 1/20.
# However the problem asked to find the probability of drawing 
# 3 balls of the same color. Thus this probability is P({R, R, R})
#  + P({G, G, G}). The above analysis works for green balls as well,
# thus P({R, R, R}) + P({G, G, G}) = 1/20 + 1/20 = 2/20 = 1/10.