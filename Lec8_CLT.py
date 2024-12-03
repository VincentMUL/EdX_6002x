# Why does the emperical rule work for normal distributions?
# Because we are reasoning not about a single 'spin',
# but about the average of many spins.
# And the central limit theorem applies.

# The Central Limit Theorem (CLT) is a fundamental theorem 
# in probability theory. Given a sufficiently large sample:
# 1. The means of the samples in a set of samples,
#    will be approximately normally distributed.
# 2. This normal distribution will have a mean close to the mean
#    of the population.
# 3. This variance of the sample means will be close to the variance
#    of the population divided by the sample size.
# Used code below to demonstrate the CLT.
# Using a die that can role a random real number between 0 and 5.
# A miraculous continuous die.
import random
import pylab 
from Lec7_VariationInData import getMeanAndStd, FairRoulette, findPocketReturn


def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
                weights = pylab.array(len(means)*[1])/len(means),
                hatch = style) #plot histogram of ranges of numbers being rolled
                #weigths to make sure each bin does not only show amount, 
                #only probability, displayed on y axis.
    return getMeanAndStd(means)
#hatch is used to display the histogram in a different way.

# # to illustrate working of function below:
# L= [1,1,1,1,2]
# pylab.hist(L)
# factor = pylab.array(len(L)*[1])/len(L)
# print(factor)
# pylab.figure()
# pylab.hist(L, weights = factor)
# pylab.show()
# #just to illustrate difference of probs vs amounts in bins.

# mean, std = plotMeans(1, 100000, 19, '1 die', 'b', '*')
# print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
# mean, std = plotMeans(50, 100000, 19, 'Mean of 50 dice', 'r', '//')
# print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)
# pylab.title('Rolling Continuous Dice')
# pylab.xlabel('Value')
# pylab.ylabel('Probability')
# pylab.legend()
# pylab.show()
# # The roll of 1 die is a uniform distribution.
# # The more dice you roll, the more the distribution looks like a normal distribution.
# # Standard deviation decreases as you roll more dice, but the mean stays the same.
# # The variance of 50 dice is close to 50 times smaller than the variance of 1 die.
# # This is the Central Limit Theorem in action.

# Betting for a pocket in fair roulette wheel example:
numTrials = 50000
numSpins = 200
game = FairRoulette()

means = []
for i in range(numTrials):
    means.append(findPocketReturn(game, 1, numSpins, False)[0]/numSpins)#if True, too much prints
#findPocketReturn returns a tuple, we only need the mean.
pylab.hist(means, bins = 19, weights = pylab.array(len(means)*[1])/len(means))
pylab.xlabel('Mean Return')
pylab.ylabel('Probability')
pylab.title('Expected Return Betting a Pocket')
pylab.show()
#Why is there a gap in this histogram?
#Because the mean return is a discrete variable,
#it can only take on certain values.

#Very close to normal distribution, but not quite.
# mEan peaks around zero, but shows a slight skew.

#Moral?
# It doesn't matter what the shape of the values happens to be.
# If we are trying to estimate the mean of a population using sufficiently large samples.
# The CLT allows us to use the empirical rule when computing CIs.

#EXERCISE 1:
# Suppose we have an experiment. We toss a coin m times. 
# Each time we collect results from a sample of size n and compute 
# this sample's mean µ(i) and standard deviation sigma(i). 
# This experiment has an underlying distribution with mean µ and standard deviation sigma.
# Which of the following does the Central Limit Theorem (CLT) 
# guarantee (for large enough n and m):
# 1. The sample means will be approximately normally distributed.
# 2. The sample means will have a mean close to the mean of the original distribution µ.
# 3. The sample means will have a variance close to the variance of the original 
#    distribution divided by the sample size sigma²/n .
# Answer: 1, 2, 3
