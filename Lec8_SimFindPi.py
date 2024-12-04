# Monte Carlo method
# Coined in 1949 by Stanislaw Ulam and Nicholas Metropolis
# Ulam together with Edward Teller, John von Neumann, and others worked on the Manhattan Project
# Ulam and Teller designed the hydrogen bomb
# Monte Carlo method of Ulam was invented in 1946, when he was sick in bed
# He was playing solitaire in bed, convalescing from an illness
# The Question: What are the chances that a Canfield solitaire 
# laid out with 52 cards will come out successfully?
# He saw a link with neutron diffusion and other questions of mathematical physics.
# He was able to transform processes described by differential equations into 
# an equivalent form interpretable as a succession of random operations.
# Later described to John Von Neumann. Talked about computers like ENIAC 
# (+/- 1000 additions per second), today's computers about 1000000000 additions per second.
# The Monte Carlo method was used during Manhattan project!

# Monte Carlo method:
# Our roulette simulation was a classic Monte Carlo simulation.
# Method of estimating the value of an unknown quantity using the principles of inferential statistics.
# Uses a Population (set of examples) and a Sample (subset of examples).
# Key fact is the random sample is representative of the population.
# Amazingly, Monte Calro simulation and randomized algorithms in general can be used
# to solve problems that are inherently not stochastic.
# Example: simuation of pi - ratio of circumference to diameter of a circle.
# Circa 1650 BC Rhind papryus 3.16, 250BC Archimedes
# Archimedes used inner and outer polygons to approximate pi.
# Concluded 273/71 < pi < 201/64 (upper and lower bounds) - > 3.1418 (error 0.0002)
# Buffon and Laplace in 18th century used a stochastic simulation.
# Circle in square of side 2, radius r is 1. Area of square is 4
# Area of circle is pi*r^2 = pi, if we knew area of circle, we could calculate pi.
# Dropping large number of needles, ratio of number of needletips lying inside the circle
# to the number of needletips in the square is same ratio as area of circle to area of square.
# So area of circle is area of square * (needles in circle)/(needles in square)
# Since area of circle is pi and area of square is 4, we can calculate pi.
# pi = 4 * (needles in circle)/(needles in square)
# Drop many needles and randomly!
# Example of arrows; trials need to be random and independent.

import random, math, numpy, pylab

# EXERCISE 2:
# If you wanted to run a simulation that estimates the value of sqrt(2),
# in a way similar to the Pi estimation shown in lecture, 
# what geometric shape would you throw needles at?
# 1.A square, with a smaller square drawn inside it. The smaller square is formed by connecting the larger square's midpoints.
# 2.A cube with a sphere inscribed inside it.
# 3.A flat line ranging from 0 to root 2 and with a subsection that spans from 0 to 1.
# Answer: Not 1!! It's 3!
def throwNeedlessqrt(numNeedles):
    success = 0
    for n in range(numNeedles):
        x = random.random()
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success)/numNeedles)
    return sqrt2   

# print(throwNeedlessqrt(500000)) #test -> 1.41468
#using math.sqrt(2) = 1.4142135623730951 

# What introduced the error for Archimedes' method of calculating Pi?
# 1. Incorrect conceptual model.
# 2. Calculation error.
# 3. Not enough samples.
# Answer: 3

# Simulating Buffon-Laplaces method
def throwNeedles(numNeedles):
    inCircle =0
    for Needles in range(1, numNeedles +1, 1):
        x = random.random()#carthesian coordinates
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0: #Pythagoras
            inCircle += 1
    return 4*(inCircle/float(numNeedles))#4 comes from area of square

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates) #averaging the results over numTrials trials
    print('Est. = ' + str(curEst) + ', Std. dev. = ' + str(round(sDev,6)) + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):#estPi calls getEst with increasing numNeedles
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/1.96: #with a confidence of 95%
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

random.seed(0)
estPi(0.005, 100)
#notice the estimates of python get closer to the real value of pi and then gets worse
# Important notion!Not sufficient to produce a good answer, 
# need to have reason to believe that it is close to right!
# In this case the small standard deviation implies we are close to 
# the true value of pi (=3.141592653589793)

#Is it correct to state 95% of the time we run this sim, we will estimate
#the value of pi is between 3.13743875875 and 3.14567467875?
#With a probability of 0.95 the actual value of pi is 
# between 3.13743875875 and 3.14567467875?
# Both are factually correct, but only 1 of them can be inferred from
# our simulation! Small stdev is a necessary but not sufficient condition
# Statistically valid is not the same as correct conclusion.
# Assumption is here that our simulation is accurate model of reality.
# For instance, change 4 to 2 in throwNeedles function,
# converged faster, final value is not close to pi.
# Do a sanity check!
# Validation could be done for instance with the polygon method.

#Method can also be used to estimate area of region r.
#Pick enclosing region e, property that area of e is easy to calculate.
#Region r lies completely within e. (a subset of e)
#Pick a random set of points and f fraction of them lie within r.
#Let f be fraction of points that fall within r.
#Multiply the area of e by f to get an estimate of the area of r.
#->Useful for estimating integrals!
def integrate(f, a, b, step):
    yVals, xVals = [], []
    xVal = a
    while xVal <= b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal += step
    pylab.plot(xVals, yVals)
    pylab.title('sin(x)')
    pylab.xlim(a, b)
    xUnders, yUnders, xOvers, yOvers = [],[],[],[]
    for i in range(500):
        xVal = random.uniform(a, b)
        yVal = random.uniform(0, 1)
        if yVal < f(xVal):
            xUnders.append(xVal)
            yUnders.append(yVal)
        else:
            xOvers.append(xVal)
            yOvers.append(yVal)
    pylab.plot(xUnders, yUnders, 'ro')
    pylab.plot(xOvers, yOvers, 'ko')
    pylab.xlim(a, b)
    ratio = len(xUnders)/(len(xUnders) + len(yUnders))
    print(ratio)
    print(ratio*b)
    
def one(x):
    return 0.9
    
#integrate(one, 0, math.pi, 0.001)

#EXERCISE 3:
# If you remember the Buffon Needle Problem, 
# the ratio of the areas of a circle and a square are used to estimate 
# the value of pi by dropping needles onto the shapes.
# We can imagine that using different area ratios 
# results in the estimation of different constants.
# In the following boxes, you will be asked to enter in mathematical expressions. 
# To enter in addition, multiplication, subtraction, or division, 
# use the operators: +, *, -, /. To enter in exponentiation, 
# use the caret (^) key. To enter in the constant pi, simply type pi.
# Too easy, half the circle in half the square -> pi/2 and 
# return 2*(inCircle/float(numNeedles)) instead of 4

#EXERCISE 4:
# You have a bucket with 3 red balls and 3 green balls. 
# Assume that once you draw a ball out of the bucket, you don't replace it. 
# What is the probability of drawing 3 balls of the same color?
# Write a Monte Carlo simulation to solve the above problem. 
# Feel free to write a helper function if you wish.

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    sameColor = 0
    for trial in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        drawn = []
        for draw in range(3):
            ball = random.choice(bucket)
            bucket.remove(ball)
            drawn.append(ball)
        if drawn[0] == drawn[1] and drawn[1] == drawn[2]:
            sameColor += 1
    return sameColor/numTrials

print(noReplacementSimulation(100000)) #test -> 0.298
#Grader test:
# In this test we call the simulation five times, with 5000 trials, and 
# compare the results. There should be variable changes.
