import random
from Lec7_InferentialStatistics import playRoulette, FairRoulette

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
        
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
        
    def __str__(self):
        return 'American Roulette'

def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns

# random.seed(0)
# numTrials = 20
# resultDict = {} #map game to list of results
# games = (FairRoulette, EuRoulette, AmRoulette)

# for G in games:
#     resultDict[G().__str__()] = [] #Initialize the list of results for each game
# #Why? Because we want to store the results of each game in a dictionary.
# for numSpins in (1000, 10000, 100000, 1000000):
#     print('\nSimulate', numTrials, 'trials of',
#             numSpins, 'spins each')
#     for G in games:
#         pocketReturns = findPocketReturn(G(), numTrials,
#                                          numSpins, False)
#         expReturn = 100*sum(pocketReturns)/float(len(pocketReturns))
#         print('Exp. return for', G(), '=',
#               str(expReturn) + '%')

#The results show the loss on American Roulette is bigger than European Roulette.
#
#Conclusions:
# Never possible to guarantee perfect accuracy through simulation or sampling.
# Never really sure the sample set is typical of the population.
# Not to say that an estimate is not precisely correct. Eg flip a coin twice;
# get 1 head and 1 tails. The estimate of 50% heads is correct, but the
# reasoning was not correct.
# Question is how much confidence we have in the estimate!
# Or how many samples are needed to get a good estimate.
# How many samples to get a justifiable confidence in the estimate.
#
# Variance is a measure of how much spread in the possible different outcomes.
# A sum of all the squared differences from the mean relative to the sample size.
# The standard deviation is the square root of the variance.
# Because of the square, the outliers can have a big effect on the variance.
# You should always consider the standard deviation relative to the mean.
# The standard deviation tells us if many values are relatively close to the mean.
# Large = many far, small = many close.

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return round(mean, 3), round(std, 3)

#The mean and standard deviation can help us talk about the confidence
#we should have in sample mean being close to the population mean.
#Confidence interval provides a range that is likely to contain the
#unknown value and a confidence that the unknown value lies within that range.
#(Preferable to estimating an unknown value with a single value.)
#
# Example: "The return on betting on 2 twenty times in European Roulette,
# is -3.3%. The margin of error is +/- 1 percentage point with 95% confidence."
# Meaning: In an infinite number of experiments of 20 spins, 95% of those
# experiments will have a return between -2.3% and -4.3%.
# -> The confidence interval and level indicate reliability of the estimate.

# Under certain conditions we can apply the empirical rule:
# 68% of the data lies within 1 standard deviation of the mean.
# 95% of the data lies within 2 standard deviations of the mean.
# 99.7% of the data lies within 3 standard deviations of the mean.

# We can look at a sample of data, calculate the mean and standard deviation,
# and then use the empirical rule to estimate the confidence interval.

# random.seed(0)
# numTrials = 20
# resultDict = {} #map game to list of results
# games = (FairRoulette, EuRoulette, AmRoulette)
# for G in games:
#     resultDict[G().__str__()] = [] #Initialize the list of results for each game
# #Why? Because we want to store the results of each game in a dictionary.
# for numSpins in (1000, 10000, 100000, 1000000):
#     print('\nSimulate betting a pocket for', numTrials, 'trials of',
#             numSpins, 'spins each')
#     for G in games:
#         pocketReturns = findPocketReturn(G(), numTrials,
#                                          numSpins, False)
#         mean, std = getMeanAndStd(pocketReturns)
#         resultDict[G().__str__()].append((numSpins, 100*mean, 100*std))
#         print('Exp. return for', G(), '=',
#               str(round(100*mean,3)) + '%', '+/-' + str(round(100*1.96*std, 3)) #1.96 is the z-value for 95% confidence, rather then 2.
#               + '% with 95% confidence')

# Notice the confidene interval shrinks for larger sample size.

# EXERCISE 2:
# For the questions below, please try to think about the solution in your head 
# before using an IDE or a calculator to compute it. 
# The goal of these questions is to give you some intuition about the topics we've been discussing.
#
# 1. Which of the following populations has the largest variance?
#    a. [0, 1, 2, 3, 4, 5, 6]
#    b. [3, 3, 3, 3, 3, 3, 3]
#    c. [0, 0, 0, 3, 6, 6, 6]
# Answer: C
#    a. [3, 3, 5, 7, 7]
#    b. [1, 5, 5, 5, 9]
# Answer: B
#
# 2. If a number is removed from a population, the standard deviation of that population will always decrease.
#    True or False?
# Answer: False
#
# 3. You are taking samples of the ages of two populations, A and B. 
# Population A is all the residents of San Francisco, 
# while Population B is all the residents of Los Angeles.
# The sample from Population A has a mean of 35 and a standard deviation of 1. 
# The sample from Population B has a mean of 45 and a standard deviation of 15. 
# Which of the following are certain?
#    a. You will not find an individual in Population A that is over the age of 37.
#    b. The average age of Population A is lower than the average age of Population B.
#    c. The average age of the sample of Population A is lower than the average age of the sample of Population B
#    d. If the sample size of each population is 10, then you can conclude that your sample accurately represents the population.
#    e. A sample size of 1 million is more appropriate than a sample size of 10 for these populations.
# Answer: C and E
#
# 4. The 95% confidence interval for a normal distribution of data with 
#   a mean of 5 and a standard deviation of 2 is 5 +/- ________

# EXERCISE 3:
# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
# and outputs the standard deviation of the lengths of the strings. 
# Return float('NaN') if L is empty.
# Recall that the standard deviation is computed by this equation:
# std = sqrt(sum((lengths - mean) ** 2) / n)
# where: µ is the mean of the elements in X and
# the numerator is the sum of the squared differences between the elements in X and the mean.
# (online this is each element t in in set X)
# The denominator is the number of elements in X -> n.
# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.
# Note: If you want to use functions from the math library, be sure to import math. 
# If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:
# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# Then, do import numpy as np and use np.METHOD_NAME in your code.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0 or type(L) != list:
        return float('NaN') #Not a Number
    else:
        mean = sum(len(s) for s in L)/len(L)
    
    if mean == 0:
        return float('NaN') #Not a Number
    # elif mean == 1:
    #     return 0
    else:
        stdev = (sum((len(s) - mean)**2 for s in L)/len(L))**0.5
    return stdev

#Test cases
L = ['a', 'z', 'p']
print(stdDevOfLengths(L))
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
L = []
print(stdDevOfLengths(L))
L = ['a']
print(stdDevOfLengths(L))
L = ['aa']
print(stdDevOfLengths(L))
L = ['aaa', 'bbb', 'ccc']

#GRADER ANSWERS:
def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L) == 0):
        return float('NaN')   
    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / len(L)
    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals)**2
    variance = sumDevSquared / len(L)
    # standard deviation is the square root of the variance
    stdDev = variance**(.5)
    return stdDev

# using listcomps
def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    lengths    = [len(s) for s in L]
    mean       = sum(lengths) / n
    squaredDev = [(l-mean)**2 for l in lengths]
    variance   = sum(squaredDev) / n    
    return variance**(.5)

# using a separate function for std dev
def stdDev(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    X = []
    for s in L:
        X.append(len(s))
    return stdDev(X)

# EXERCISE 4:
# The coefficient of variation is the standard deviation divided by the mean. 
# Loosely, it's a measure of how variable the population is in relation to the mean.
# 1. Figure 1 shows the skyline of Pythonland, and Figure 2 shows the skyline of Montyland.
#    Figure shows Pythonland with higher mean than Montyland, same stdev as Montyland.
#    Answer: Montyland
# 2. Which of the following populations has the highest coefficient of variation?
#    a. [1, 2, 3] X
#    b. [11, 12, 13]
#    c. [0.1, 0.1, 0.1]
# 3. Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.

def getMeanAndStdAndCov(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    cov = std/mean
    return round(mean, 3), round(std, 3), round(cov, 3)

X = [10, 4, 12, 15, 20, 5]
print(getMeanAndStdAndCov(X))
