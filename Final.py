# Problem 1

# Problem 1-1
# Consider deriving the probability of a coin flip coming up heads by running m trials of 100 flips each. 
# If the coin is fair, the mean probability of the m trials will go to 0.5 as m goes to infinity.
# True [X]

# Problem 1-2
# Consider two normal distributions, A and B. The standard deviation of A is 3 and the standard deviation of B is 5. 
# For each distribution, 1,000 observations are drawn and plotted in a histogram with 10 bins, 
# creating one histogram for each distribution.
# The rightmost bin of A will have fewer points than the rightmost bin of B.
# The rightmost bin of B will have fewer points than the rightmost bin of A.
# The rightmost bin of A will have the same number of points as the rightmost bin of B.
# Any of the above are possible.
# Answer: Any of the above are possible. (I answered: The rightmost bin of A will have fewer points than the rightmost bin of B.)
# Why is the answer "Any of the above are possible."?

# Problem 1-3
# You roll an unfair (weighted) die. The distribution of the numbers rolled is a uniform distribution.
# False, because the distribution of the numbers rolled is not a uniform distribution.

# Problem 1-4
# A simulation
#   is useful when describing a system that cannot easily be described mathematically.
#   is easy to successively refine.
#   can be used to extract intermediate results.
#   All of the above
#   None of the above
# Answer: All of the above

# Problem 1-5
# The following image plots the population of the US over time, along with a model fit to the data. 
# The graph is of points linearly from 1900 to 2000 and a red line fitted to the points 
# that dips to 0 from x=2000 to x=2050
# overfitting

# Problem 1-6
# If the R² of a model produced using linear regression is 0.7, 
# the model accounts for 70% of the variance in the observations.
# Answer: True

# Problem 1-7
# Given a finite set of data points there exists a polynomial fit such 
# that the polynomial curve goes through each point in the data.
# Answer: False, because the polynomial curve does not have to go through each point in the data.

# Problem 1-8
# You want to calculate confidence intervals by applying the empirical rule, 
# which requires that you have a normal distribution with a known mean and standard deviation. 
# Which approach can you use to estimate the mean and standard deviation that you need? Choose all that work.
    # Central Limit Theorem, which requires that you have many sufficiently large samples from the population
    # Standard Error, which requires that you have one sufficiently large sample
# Answer: Both, because both the Central Limit Theorem and Standard Error can be used to estimate the mean and standard deviation that you need.
# Explanation: ?

# Problem 1-9
# You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. 
# Assume that once you draw a ball out of the bucket, you don't replace it. 
# What is the probability of drawing 3 balls of the same color? 
# Answer the question in reduced fraction form - eg 1/5 instead of 2/10.
# Reasoning: 3/7*2/6 = 1/7

######################################################################################################################

# Problem 2:

# # Consider the following code:

# import random, pylab
# xVals = []
# yVals = []
# wVals = []
# for i in range(1000):
#     xVals.append(random.random())
#     yVals.append(random.random())
#     wVals.append(random.random())
# xVals = pylab.array(xVals)
# yVals = pylab.array(yVals)
# wVals = pylab.array(wVals)
# xVals = xVals + xVals
# zVals = xVals + yVals
# tVals = xVals + yVals + wVals
# # For each of the following questions, select the best answer from the set of choices.

# Problem 2-1
# The values in tVals are most closely:
    # Uniformly distributed
    # Distributed with a Gaussian distribution
    # Exponentially distributed
# Answer: Gaussian distribution, see viz below.

# # Plot histograms
# pylab.figure(figsize=(15, 5))

# # Histogram for xVals
# pylab.subplot(1, 3, 1)
# pylab.hist(xVals, bins=20, edgecolor='black')
# pylab.title('Distribution of xVals')
# pylab.xlabel('Value')
# pylab.ylabel('Frequency')

# # Histogram for zVals
# pylab.subplot(1, 3, 2)
# pylab.hist(zVals, bins=20, edgecolor='black')
# pylab.title('Distribution of zVals')
# pylab.xlabel('Value')
# pylab.ylabel('Frequency')

# # Histogram for tVals
# pylab.subplot(1, 3, 3)
# pylab.hist(tVals, bins=20, edgecolor='black')
# pylab.title('Distribution of tVals')
# pylab.xlabel('Value')
# pylab.ylabel('Frequency')

# # Show the plots
# pylab.tight_layout()
# pylab.show()

# Problem 2-2
# The values in xVals are most closely:
    # Uniformly distributed
    # Distributed with a Gaussian distribution
    # Exponentially distributed
# Answer: Uniformly distributed, see viz.


# For each of the following expressions using the code above, 
# match the following calls to pylab.plot with one of the graphs shown below.

# # Problem 2-3
# pylab.plot(xVals, zVals)
# pylab.title('xVals vs zVals')
# pylab.xlabel('xVals')
# pylab.ylabel('zVals')
# pylab.show()
# # Graph 5

# # Problem 2-4
# pylab.plot(xVals, yVals)
# pylab.title('xVals vs yVals')
# pylab.xlabel('xVals')
# pylab.ylabel('yVals')
# pylab.show()
# # Graph 4

# # Problem 2-5
# pylab.plot(xVals, sorted(yVals))
# pylab.title('xVals vs sorted(yVals)')
# pylab.xlabel('xVals')
# pylab.ylabel('sorted(yVals)')
# pylab.show()
# # Graph 3

# # Problem 2-6
# pylab.plot(sorted(xVals), yVals)
# pylab.title('sorted(xVals) vs yVals')
# pylab.xlabel('sorted(xVals)')
# pylab.ylabel('yVals')
# pylab.show()
# # Graph 2

# # Problem 2-7
# pylab.plot(sorted(xVals), sorted(yVals))
# pylab.title('sorted(xVals) vs sorted(yVals)')
# pylab.xlabel('sorted(xVals)')
# pylab.ylabel('sorted(yVals)')
# pylab.show()
# # Graph 1

######################################################################################################################

# Problem 3:

# You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. 
# Assume that once you draw a ball out of the bucket, you don't replace it. You draw 3 balls.

# Write a Monte Carlo simulation that meets the specifications below. 
# Feel free to write a helper function if you wish. Do not use pylab, numpy or matplotlib.

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    def draw():
        bucket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
        drawn = []
        for i in range(3):
            drawn.append(bucket.pop(bucket.index(random.choice(bucket))))
        return drawn

    same_color = 0
    for i in range(numTrials):
        drawn = draw()
        if drawn[0] == drawn[1] == drawn[2]:
            same_color += 1
    return same_color / numTrials

# # Test
# print(drawing_without_replacement_sim(10000)) # Expected output 1/7
# Grader test was just repeatedly testing this and checking to see if within range of 1/7. (presumably)

######################################################################################################################

# Problem 4:

# Problem 4-1

# You are given the following function and class and function specifications 
# for the two coding problems on this page (also available in this file, die.py):
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), 
# using only pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show from the pylab module 
# and with the following specification:

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins, edgecolor='black')
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    # pylab.show()

# # # Test
# makeHistogram([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 'Value', 'Frequency', 'Histogram of Values')

# Problem 4-2

# Write a function called getAverage(die, numRolls, numTrials), with the following specification.
# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
    # a dice roll of 1 4 3 has a longest run of 1
    # a dice roll of 1 3 3 2 has a longest run of 2
    # a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
# When this function is called with the test case given in the file, it will return 5.312. 
# Your simulation may give slightly different values.

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_runs = []
    for t in range(numTrials):
        rolls = [die.roll() for i in range(numRolls)]
        longest_run = 1
        current_run = 1
        for i in range(1, len(rolls)):
            if rolls[i] == rolls[i-1]:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 1
        longest_runs.append(longest_run)
    makeHistogram(longest_runs, 10, 'Longest Run', 'Frequency', 'Histogram of Longest Runs')
    return sum(longest_runs) / len(longest_runs)

    
# # One test case
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

# # # Grader test
# Test: 1

#         (Die([1]), 10, 1000)
        
# Output:
# test 1
# Successfully called makeHistogram
# Test successful
# Test: 2

#         (Die([1,1]), 10, 1000)
        
# Output:
# test 2
# Successfully called makeHistogram
# Test successful
# Test: 3

#         (Die([1,2,3,4,5,6]), 50, 1000)
        
# Output:
# test 3
# Successfully called makeHistogram
# Test successful
# Test: 4

#         (Die([1,2,3,4,5,6,6,6,7]), 50, 1000)
        
# Output:
# test 4
# Successfully called makeHistogram
# Test successful
# Test: 5

#         # (Die([1,2,3,4,5,6,6,6,7]), 1, 1000)
        
# Output:
# test 5
# Successfully called makeHistogram
# Test successful

######################################################################################################################

# Problem 5:

# K-means is a greedy algorithm, meaning it looks for local minimum when choosing points closest to the centroid. 
# For each dataset illustrated below, will k-means, as shown in lecture, 
# using Euclidean distance as the metric be able to find clusters that match the dataset patterns?
# See KmeansClusterProblem.png

######################################################################################################################

# Problem 6:

# Write a function that meets the specifications below. You do not have to use dynamic programming.

# Hint: You might want to use bin() on an int to get a string, 
# get rid of the first two characters, add leading 0's as needed, 
# and then convert it to a numpy array of ints. Type help(bin) in the console.
# In the console, help said:
# >>> help(bin)
# Help on built-in function bin in module builtins:

# bin(number, /)
#     Return the binary representation of an integer.

#     >>> bin(2796202)
#     '0b1010101010101010101010'

# For example, 
# If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
# If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
# If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
# More specifically, write a function that meets the specifications below:

import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    def to_binary(n, length):
        binary = bin(n)[2:]
        return np.array([0]*(length - len(binary)) + [int(i) for i in binary])

    length = len(choices)
    best_combination = np.zeros(length, dtype=int)
    best_sum = 0
    for i in range(2**length):
        binary = to_binary(i, length)
        current_sum = sum(binary * choices)
        if current_sum == total:
            return binary
        elif current_sum < total and current_sum > best_sum:
            best_sum = current_sum
            best_combination = binary
    return best_combination

# # Test
# print(find_combination([1,2,2,3], 4)) # Expected output [0 1 1 0] or [1 0 0 1]
# print(find_combination([1,1,3,5,3], 5)) # Expected output [0 0 0 1 0]
# print(find_combination([1,1,1,9], 4)) # Expected output [1 1 1 0]
# print(find_combination([4, 6, 3, 5, 2], 10)) # Expected output [1, 1, 0, 0, 0] Which is still not working: [0 0 1 1 1]
# print(find_combination([4, 10, 3, 5, 8], 1)) # Expected output [0, 0, 0, 0, 0]
# print(find_combination([1, 81, 3, 102, 450, 10], 9)) # Expected output [1, 0, 1, 0, 0, 0]
# print(find_combination([4, 10, 3, 5, 8], 1))

######################################################################################################################

# Problem 7:

# Problem 7-1

# Answer the next questions on machine learning, related to the following data. 
# Consider the following 6 people who are either happy or unhappy and the data we know on them:

# 	                                Person 1	Person 2	Person 3	Person 4	Person 5	Person 6
# Happy/Unhappy	                    happy	    happy	    happy	    unhappy	    unhappy	    unhappy
# Income (dollars)	                10k	        30k	        90k	        100k	    120k	    60k
# Distance from North Pole (miles)	4k	        10k	        5k	        1k	        1k	        6k
# Continents Visited	            Europe	    Europe	    Europe	    Europe	    Europe	    Europe
# Age	                            25	        19	        26	        57	        60	        40

# Using the Manhattan distance and looking only at "Income" and "Distance from North Pole", 
# which two people are closest and farthest?
# Let's start by making a function that calculates the Manhattan distance between two points, 
# using function for minkowski distance below as an example.
def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

def manhattanDist(v1, v2):
    return minkowskiDist(v1, v2, 1)

# # Test
print(manhattanDist([10, 4], [30, 10])) # Expected output 26

# For calculating this for every pair of people, we should construct a distance matrix,
#  using the function defined above to fill in each row of the matrix.

# In the case of the animal matrix, code was constructed in Lec12, now let's do something similar for the people matrix.
class Person(object):
    def __init__(self, name, income, distance):
        """Assumes name a string; income and distance are numbers"""
        self.name = name
        self.features = pylab.array([income, distance])
        
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other):
        """Assumes other a Person
           Returns the Manhattan distance between feature vectors
              of self and other"""
        return manhattanDist(self.getFeatures(), other.getFeatures())
                             
    def __str__(self):
        return self.name

def comparePersons(persons, precision):
    """Assumes persons is a list of Person, precision an int >= 0
       Builds a table of Manhattan distance between each person"""
    # Get labels for columns and rows
    columnLabels = []
    for p in persons:
        columnLabels.append(p.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    # Get distances between pairs of persons
    # For each row
    for p1 in persons:
        row = []
        # For each column
        for p2 in persons:
            if p1 == p2:
                row.append('--')
            else:
                distance = p1.distance(p2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    # Produce table
    table = pylab.table(rowLabels=rowLabels,
                        colLabels=columnLabels,
                        cellText=tableVals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.138]*len(persons))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distances')
    pylab.show()

# Create Person instances
person1 = Person('Person 1', 10, 4)
person2 = Person('Person 2', 30, 10)
person3 = Person('Person 3', 90, 5)
person4 = Person('Person 4', 100, 1)
person5 = Person('Person 5', 120, 1)
person6 = Person('Person 6', 60, 6)

persons = [person1, person2, person3, person4, person5, person6]

# Compare persons
# comparePersons(persons, 3)

# Conclusion: closest: Person 3 and Person 4 ||| farthest: Person 1 and Person 5

# Problem 7-2
# If we were to cluster the people, 
# the inclusion/exclusion of which feature would never impact the final clusters?
# Answer: Continents Visited

######################################################################################################################

# Problem 8 part A:

# For this problem you are going to simulate growth of fox and rabbit population in a forest!
# The following facts are true about the fox and rabbit population:
    # The maximum population of rabbits is determined by the amount of vegetation in the forest, 
    # which is relatively stable.
    # There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.
    # For each rabbit during each time step, a new rabbit will be born with a probability of pRabbitReproduction
    # pRabbitReproduction = 1.0 - currentPopulationOfRabbits/1000
    # In other words, when the current population is near the maximum, 
    # the probability of giving birth is very low, and when the current population is small, 
    # the probability of giving birth is very high.
    # The population of foxes is constrained by number of rabbits.
    # There are never fewer than 10 foxes.
    # At each time step, after the rabbits have finished reproducing, 
    # a fox will try to hunt a rabbit with success rate of pFoxEatRabbit
    # pFoxEatRabbit = currentPopulationOfRabbits/1000
    # In other words, the more rabbits, the more likely a fox will eat one.
    # If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. 
    # Remember that the population of rabbits is never lower than 10.
    # Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.
    # If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.
    # If the starting population is below 10 then you should do nothing. 
    # You should not increase the population nor set the population to 10. 
# Start with 500 rabbits and 30 foxes.
# At the end of each time step, record the number of foxes and rabbits.
# Run the simulation for 200 time steps, and then plot the population of rabbits 
# and the population of foxes as a function of time step. 
# (You do not need to paste your code for plotting for Part A of this problem).
# Use the following steps, and the template file rabbits.py 
# (click to download .py file), as guides in your implementation of this simulation.
# Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step
# Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time step
# Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and then the second part of the simulation. 
# Record the two populations in two different lists, and return those lists.
# Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
# CURRENTRABBITPOP = 50
# CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    def pRabbitReproduction():
        return 1.0 - CURRENTRABBITPOP / MAXRABBITPOP
    
    new_rabbits = 0
    for i in range(CURRENTRABBITPOP):
        if random.random() < pRabbitReproduction():
            new_rabbits += 1
    CURRENTRABBITPOP += new_rabbits
    if CURRENTRABBITPOP > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    def pFoxEatRabbit():
        return CURRENTRABBITPOP / MAXRABBITPOP
    
    new_foxes = 0
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10 and random.random() < pFoxEatRabbit():
            CURRENTRABBITPOP -= 1
            if random.random() < 1/3:
                new_foxes += 1
        else:
            if random.random() < 0.1:
                CURRENTFOXPOP -= 1
    CURRENTFOXPOP += new_foxes
    if CURRENTFOXPOP < 10:
        CURRENTFOXPOP = 10
    if CURRENTRABBITPOP < 10:
        CURRENTRABBITPOP = 10
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations


# Grader Tests:
# Test: 1 rabbitGrowth
# Calling rabbitGrowth with MAXRABBITPOP = 1000, CURRENTRABBITPOP = 500 should increase the population.
# Output:
# rabbitGrowth()
# Population has increased? True
# rabbitGrowth()
# Population has increased? True
# Test completed.
# 
# Test: 2 rabbitGrowth
# Calling rabbitGrowth with MAXRABBITPOP = 1000, CURRENTRABBITPOP = 1000 should not increase the population.
# Output:
# rabbitGrowth()
# Population has increased? False
# rabbitGrowth()
# Population has increased? False
# Test completed.
# 
# Test: 3 foxGrowth
# Calling foxGrowth with CURRENTRABBITPOP = 1000, MAXRABBITPOP = 1000, CURRENTFOXPOP = 50 should increase the population.
# Output:
# foxGrowth()
# Population has increased? True
# foxGrowth()
# Population has increased? True
# Test completed.
# 
# Test: 4 foxGrowth
# Calling foxGrowth with CURRENTRABBITPOP = 1, MAXRABBITPOP = 1000, CURRENTFOXPOP = 1 should not increase the population.
# Your output:
# Calling foxGrowth() 20 times. The fox population should not grow.
# 0 10
# Population has increased? False
# Test completed.
# Correct output:
# Calling foxGrowth() 20 times. The fox population should not grow.
# Population has increased? False
# Test completed.
# 
# Test: 5 runSimulation
# Test the simulation
# Output:
# results = runSimulation(20)
# Test completed.
# 
# Test: 6 runSimulation
# Test the simulation with CURRENTRABBITPOP = 10, CURRENTFOXPOP = 20, MAXRABBITPOP = 100
# Output:
# results = runSimulation(100)
# Testing that the number of rabbits never falls below 10 or goes above 100.
# Test completed.
# 
# Test: 7 runSimulation
# Test the simulation with CURRENTRABBITPOP = 10, CURRENTFOXPOP = 20, MAXRABBITPOP = 100
# Output:
# results = runSimulation(100)
# Testing that the number of foxes never falls below 10.
# Test completed.

# Test 4 did not work because I reset the fox population to something and I shouldn't do that, which is why
# the grader gave output 0 10. 
# 2 hints, first one is relevant here:
# "See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this particular test, 
# your code changes the CURRENTFOXPOP (increases it if the fox population has gone below the minimum fox population), 
# which is not the right behavior -- the code should not reset CURRENTFOXPOP.

# It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3 foxGrowth". 
# Pay special attention to the following statement in the docstring of foxGrowth(): 
# "Each fox, based on the probabilities in the problem statement, may eat one rabbit 
# (but only if there are more than 10 rabbits)."

# Problem 8 Part B:
# Follow the next steps of the simulation to answer the remaining questions.

# Step 4: Assume MAXRABBITPOP = 1000, CURRENTRABBITPOP = 500, CURRENTFOXPOP = 30, numSteps = 200. 
#         Plot two curves, one for the rabbit population and one for the fox population. 
#         You won't be submitting the plots. They are for your own understanding.

# Step 5: Use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve 
#         and the same for the fox curve. 
#         Then use polyval to evaluation the 2nd degree polynomial and plot it, e.g.
#         coeff = polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
#         plot(polyval(coeff, range(len(rabbitPopulationOverTime))))
# Of course your variables and plotting commands may not look identical to the above code; 
# the above code is shown just to give you an idea of what we mean.
# Once you have finished Steps 4 and 5, continue on to answer the following questions.

# Let's plot two curves, one for the rabbit population and one for the fox population.
rabbit_populations, fox_populations = runSimulation(200)
pylab.plot(rabbit_populations, label='Rabbit Population')
pylab.plot(fox_populations, label='Fox Population')
pylab.legend()
pylab.show()

# Problem 8 -2:
# At some point in time, there are more foxes than rabbits.
# Answer: True

#Now that we've got the plot, let's use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve
# and the same for the fox curve. Then use polyval to evaluate the 2nd degree polynomial and plot it.

rabbit_coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
fox_coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)

pylab.plot(pylab.polyval(rabbit_coeff, range(len(rabbit_populations))), label='Rabbit Population')
pylab.plot(pylab.polyval(fox_coeff, range(len(fox_populations))), label='Fox Population')
pylab.legend()
pylab.show()


# Problem 8 -3:
# The polyfit curve for the rabbit population is:
# A concave up curve (looks like a U shape)

# Problem 8 -4:
# The polyfit curve for the fox population is:
# A concave down curve (looks like an upside down U shape)

# Problem 8 -5:
# Changing the initial conditions from 500 rabbits and 30 foxes to 50 rabbits and 300 foxes 
# changes the general shapes of both the polyfit curves for the rabbit population and fox population.
# Answer: False

# Problem 8 -6:
# Let's say we make a change in the original simulation. 
# That is, we are going to change one detail in the original simulation, 
# but everything else will remain the same as it was explained in Problem 8 - Part A.
# Now, if a fox fails in hunting, it has a 90 percent chance of dying 
# (instead of a 10 percent chance, as in the original simulation).
# Changing the probability of an unsuccessful fox dying from 10% to 90% changes the general shapes of both 
# the polyfit curves for the rabbit population and fox population.
# Answer: True, they switch places, Rabit U shape and Fox upside down U shape, with Rabit above Fox.
# Grader disagrees, perhaps they meant just the shape. As in U and upside down U, not the order of them.