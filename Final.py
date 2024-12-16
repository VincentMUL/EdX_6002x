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

# Consider the following code:

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
# For each of the following questions, select the best answer from the set of choices.