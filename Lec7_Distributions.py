#Emperical rule only holds under some assumptions
# Two key assumptions:
# 1. The mean estimation error is zero (nothing about their size, just avg 0)
#    example: most students asked to predict their grade, will overstimate
#    which results in a positive error; ie avg =/= 0
# 2. The distribution of the errors in the estimate is normal (bell curve);
#    -> Gaussian curve (in honor of mathematician and astronomer Carl Friedrich Gauss)

# Define distributions:
# Using a probability distribution.
#     Different: Already used histograms to depict frequency of distribution.
#     How often a random variable has taken on a value in some range.
#Probability distribution captures relative frequency by giving the
#probability of a random variable taking on a value within a range.
#There are 2 groups of Probability Distributions:
#1. Discrete: Random variables drawn from a finite set of values. (roll of a die)
#             Easy, just list probablity of each value (sum = 1)
#2. Continuous: Random variables drawn from an infinite set of values between 2
#               real numbers. (speed of car)
#               More complex, can't list probability of each value.
#               In fact individual values have probability of around 0.
#               Instead, define a probability density function (pdf).
#               PDF defines probability of a random variable falling within a range.
#               (area under the curve = 
#               probability of random variable falling within that range)
#               Definese a curve where the values on the x-axis lie between
#               minimum and maximum values of the  variable.
#               The probability of the variable having a value between x1 and x2
#               is the area under the curve between x1 and x2.
#               Example: Uniform Distribution (pdf for random.random()) being flat
#                        VS random.random() + random.random() being a triangle.
#               The area under the curve is 1.0 for both, but the triangular
#               distribution has a higher probability of being in the middle.
#
# Normal Distributions
# Most common continuous distribution.
# Bell shaped curve.
# Defined by 2 parameters:
# 1. Mean (mu): Center of the peak.
# 2. Standard Deviation (sigma): Spread of the curve.
# Normal distributions peak at the mean and fall off symmetrically.
# They asymptotically approach the x-axis, but never touch it.
# The area under the curve is 1.0.
# Why? Because of nice mathematical properties and because it's a good model.
# The normal distribution is a good model for many things.
# Example: Heights of people, errors in measurements, etc.
# Easily generated in pylab.

import random, pylab

# dist = []
# for i in range(100000):
#     dist.append(random.gauss(0, 30))
# pylab.hist(dist, bins = 30)
# pylab.show()
# #The histogram is a good approximation of the normal distribution.
# #Peak at mean and falls off symmetrically or cose to.
# #This is a discrete approximation of the continuous normal distribution.

#Other Importance of Normal Distributions:
#Confidence Intervals: Empirical rule for normal distributions holds.
#We'll write code on this, it involves integration, so side note.

#SciPy contains many useful mathematical functions used in science and engineering.
# scipy.integrate.quad(f, a, b, args=()) 
# f is function, a is lower limit, b is upper limit.
# optional tuple of arguments supplying all but the first argument (extra arg for f).
#This will return an approximation, because it's a numerical estimate.
#Also gives an estimate of the absolute error in the result.

import scipy.integrate

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2
#This is the formula for the normal distribution. Note: ternary function
#meaning it takes 3 arguments. x is the value of the random variable.

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian,
                                        mu-numStd*sigma,
                                        mu+numStd*sigma,
                                        (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))

# checkEmpirical(3)
#3 times the same, not an accident, imperical rule holds.

# Warning! Only works for normal distributions.
# Example; does it hold for spins of a roulette wheel?
# No, because the distribution is not normal.
# For roulette, the pockets are uniformly distributed;
# each pocket has the same probability of being selected.

#EXERCISE 5:
# In the lecture, you saw a uniform and a normal distribution. 
# There is another type of distribution, called an exponential distribution. 
# For the following real-life situations, fill in the blank with the 
# appropriate distribution model (normal, uniform, or exponential) 
# that would best simulate the situation.
# Rolling a fair 6-sided die
# Uniform
# Sum of rolling 2 fair 6-sided dice
# Normal
# Women's shoe sizes
# Normal
# Human intelligence (IQ) scores
# Normal
# Amount of mold on bread, assuming an infinite supply of bread
# Exponential
# The winning lottery numbers
# Uniform
# Skilled person throwing darts at a dart board
# Normal
# Radioactive decay (time between successive atom decays)
# Exponential

#EXERCISE 6:
# Samples were taken from a distribution, and the histogram of those samples is shown here:
dist = []
for i in range(100000):
    dist.append(random.gauss(2, 1))
pylab.hist(dist, bins = 300)
pylab.xlim(-6, 6)
pylab.show()
#This is similar to the image shown, except the X-axis went from -6 to 6
#Most questions too basic. Except:
# 
# Mary's Clothes Shoppe is a moderatly busy store. 
# Which of the following histograms best matches observations of 
# how much time (in minutes) there is between customer arrivals? 
# That is, which histogram helps best predict how much time until 
# the next customer comes into the Clothes Shoppe.
# For each histogram, 1000 observations were made. 
# The x-axis is measured in minutes, and the height of each bar 
# at minute m corresponds to how many times there was an m minute 
# wait until the next customer arrived.
# Answer is the exponential distribution.
# Explanation:
# The best match is Figure 1. It is common for a busy store to have 
# frequent customers and it is most common that the next customer 
# arrives shortly after the previous customer. It is rare - but not impossible - 
# for there to be a 15+ minute gap between one customer and the next; 
# but typically we see 1-5 minute gaps.
# Generally, inter-arrival time problems are modeled well by exponential distributions.