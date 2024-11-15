# Stochastic Processes
# Old: every effect has a cause and all future states can be derived
# from knowledge and current state
# NEW: Copenhagen doctrine of causal nondeterminism:
# At its fundamental level, the physical world cannot be predicted
# "x is highly likely to happen" is the best we can do
# Einstein and Shrödinger disagreed with this

# Discussion does not matter; 
# lack of knowledge does not always allow for accurate predictions
# Might as well treat the world as stochastic
# -> Predictive nondeterminism
# The inability to make accurate measurements, 
# makes it impossible to make precise predictions about future states.
# Note: Contrast to "causal nondeterminism", 
# where the world is fundamentally unpredictable;
# notion that not every event is caused by a previous event.
# However whether events are truly unpredictable or 
# we simply don't have enough information to predict them,
# is of no practical importance.

# Stochastic Process is an ongoing process where the next state might 
# depend on both the previous states and some random element.

import random

def rollDie(): #Deterministic
    """returns an int between 1 and 6"""
    pass

def rollDie2(): #Stochastic
    """returns a randomly chosen int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

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
#Note in the squareRoot function, the specification actually allows 
# many possible return values, but will alway return the same value.
# The specification does not require a deterministic implementation,
# but it ALLOWS deterministic implementations.

# NOTE: Non-deterministic programs may be difficult to debug.

# EXERCISE 1:

# Ex 1-1 For the following explanations of different types of programmatic models,
# fill in the blanks with the appropriate model the definition describes.

# 1. A ______ model is one whose behavior is entirely predictable. 
# Every set of variable states is uniquely determined by parameters
#  in the model and by sets of previous states of these variables. 
# Therefore, these models perform the same way for a given set of 
# initial conditions, and it is possible to predict precisely what 
# will happen.
# deterministic

# 2. A ________ model is one in which randomness is present, 
# and variable states are not described by unique values, 
# but rather by probability distributions. 
# The behavior of this model cannot be entirely predicted.
# stochastic

# 3. A _______ model does not account for the element of time. 
# In this type of model, 
# a simulation will give us a snapshot at a single point in time.
# static

# 4. A _______ model does account for the element of time. 
# This type of model often contains state variables that change over time.
# dynamic

# 5. A _______ model does not take into account the function of time. 
# The state variables change only at a countable number of points in time, 
# abruptly from one state to another.
# discrete

# 6. A ______ model does take into account the function of time, 
# typically by modelling a function f(t) and 
# the changes reflected over time intervals. The state variables change 
# in an unbroken way through an infinite number of states.
# continuous

# Ex 1-2 
# If you are using differential equations to model a simulation, 
# are you more likely to be doing a discrete or continuous model?
# continuous
#
# Let's say you run a stochastic simulation 100 times. How many times 
# do you need to run the simulation again to get the same result?
# None will necessarily give you the same result.
#
# Which modelling system would be best to model a bank account?
# Discrete or Continuous or "Either discrete or continuous would work,
# depending on the specifics of the model you wish to use."

# EXERCISE 2:
# This problem asks you to write a short function that 
# uses the the random module. Visit the docs.python.org to find docs 
# on the random module, where you can see all sorts of cool functions the module provides.

# The random module has many useful functions - 
# play around with them in your interpreter to see how much you can do! 
# To test this code yourself, put the line 'import random' 
# at the top of your code file, to import all of the functions in 
# the random module. To call random module methods, 
# preface them with 'random.' , as in this sample interpreter session:

# >>> import random
# >>> random.randint(1, 5)
# 4
# >>> random.choice(['apple', 'banana', 'cat'])
# 'cat'

# How would you randomly generate an even number x,
# 0 <= x < 100? Fill out the definition for the function genEven(). 
# Please generate a uniform distribution over the even numbers 
# between 0 and 100 (not including 100).

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)

# #Testing if this would work:
# for i in range(100):
#     # print(random.randint(0, 50)*2)
#     print(random.randrange(0,100,2))

# EXERCISE 3:
# Ex 3-1
# Write a deterministic program, 'deterministicNumber', 
# that returns an even number between 9 and 21.
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

# Ex 3-2
# Write a uniformly distributed stochastic program, 'stochasticNumber', 
# that returns an even number between 9 and 21.
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10,22,2)

# # Alternative solutions:
# def stochasticNumber():
#     return 2 * random.randint(5, 10)

# EXERCISE 4:

# 1. Are the following two distributions equivalent?
def dist1():
    return random.random() * 2 - 1
def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
    
# Let's build a plot with 50 points for each distribution:
import matplotlib.pyplot as plt
import numpy as np

# plt.figure('dist1')
# plt.hist([dist1() for _ in range(5000)], bins=1000)
# plt.figure('dist2')
# plt.hist([dist2() for _ in range(5000)], bins=1000)
# plt.show()
# # For dist1, the distribution is uniform between -1 and 1.
# # For dist2, half the time it's a uniform destribution between 0 and 1,
# # and the other half of the time it's a uniform distribution between -1 and 0.
# # The two distributions ARE equivalent.

# 2. Are the following two distributions equivalent?
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

# #visualizing the distributions
# plt.figure('dist3')
# plt.hist([dist3() for _ in range(5000)], bins=10)
# plt.figure('dist4')
# plt.hist([dist4() for _ in range(5000)], bins=10)
# plt.show()
# # For dist3, the distribution is uniform between 0 and 9.
# # For dist4, the distribution is uniform between 0 and 9.
# # The two distributions are equivalent.

# 3. Are the following two distributions equivalent?
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)

#visualizing the distributions
plt.figure('dist5')
plt.hist([dist5() for _ in range(5000)], bins=10)
plt.figure('dist6')
plt.hist([dist6() for _ in range(5000)], bins=10)
plt.show()
# For dist5, the distribution is uniform between 0 and 9.
# For dist6, the distribution is uniform between 0 and 10.
# The two distributions are not equivalent.