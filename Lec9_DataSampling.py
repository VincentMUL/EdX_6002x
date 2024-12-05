# Monte carlo simulations allow you to make valid statistical inferences
# about both stochastic situations (eg random walk) and deterministic situations (eg pi)
# by generate many random samples, representative of the population, and use them to compute
# confidence intervals for the estimates.
# But there's a catch! Suppose we can't create samples by simulation?
# 
# Example of Clinton - Trump election.
# "According to the most recent poll Clinton leads Trump by 3.7 percentage points 
# in swing states. The registered voter sample is 835 with with a margin of error 
# of plus or minus 4 percentage points." 
# It's clear they did not conduct repeated polls of 835 people and use the 
# stdev to compute the confidence intervals. Instead they conducted 1 poll.

# Probability Sampling: Simple Random Sampling
#  each member of the pop has a nonzero prob of being selected
#   eg the needle needs to have equal chance of landing anywhere in the square
#   when violating this (bow example) we get biased samples
#  each member has an equal prob of being selected
# However, simple random sampling is not always appropriate!
# For instance in a skewed population; eg 2500 majors in Engineering, 100 in
# Humanities, 100 in Social Sciences, 100 in Natural Sciences. So easy to over-
# represent or under-represent a group.
# Solution: Stratified Sampling
#   Divide the population into strata (subgroups) and then draw simple random samples
#   from each stratum. The size of the sample from each stratum is proportional to the
#   size of the stratum in the population. Can be tricky! When done wrong, can be worse!
# 3 obvious approaches for predicting election:
#  1. Ask every voter. (Census)
#  2. Draw multiple random samples and compute mean and confidence interval.
#  3. Draw a single sample and compute mean and confidence interval.
# 1 is most accurate, but impractical. Though gets ground truth.
# Example of getting ground truth: Temperature in US. Data used from NCEI.
# It's daily high and low for 21 cities in US. excluding Alaska and Hawaii.
# from 1961-2015 (55 years). 421848 data points or "examples".

#Use some code to show distribution. Always good to visualize data.

import pylab, random, numpy

def makeHist(data, title, xlabel, ylabel, bins = 20):
    pylab.hist(data, bins = bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.show()

def getHighs(): #read in data from file
    inFile = open('temperatures.csv')
    population = []
    for l in inFile:
        try:
            tempC = float(l.split(',')[1])#split lines on comma, take 2nd element
            population.append(tempC)#get slist
        except:
            continue
    return population
#made because we'll be making a lot of histograms!

def getMeansAndSDs(population, sample, verbose = False):# takes population and sample of population
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    if verbose:#verbose is used to indicate if we want to see the histograms
        makeHist(population,
                 'Daily High 1961-2015, Population\n' +\
                    '(mean = ' + str(round(popMean, 2)) + ')',
                    'Degrees C', 'Number Days')
        pylab.figure()
        makeHist(sample, 'Daily High 1961-2015, Sample\n' +\
                    '(mean = ' + str(round(sampleMean, 2)) + ')',
                    'Degrees C', 'Number Days')
        print('Population mean =', popMean)
        print('Standard deviation of population =', numpy.std(population))
        print('Sample mean =', sampleMean)
        print('Standard deviation of sample =', numpy.std(sample))
    return popMean, sampleMean, numpy.std(population), numpy.std(sample)
#numpy.std is the standard deviation function in numpy
#random.sample(population, sampleSize) returns a list containing sampleSize 
#randomly chosen distinct elements of population -> sampling without replacement!

random.seed(0)
population = getHighs()
sample = random.sample(population, 100)
getMeansAndSDs(population, sample, True)
# stdev is about 58% of the mean. This is a large stdev!
# Why? Because of the difference in place, but also month.
# We're going to think about how to get a good approximation without looking at all
# the data: the sample is even further from the normal distribution than the population.
# Also clear we got lucky and got a few of the very hot and very cold, 
# these are outliers, we get these by accident.
# Population mean = 16.3
# Sample mean = 17.1
# Standard deviation of population = 9.4
# Standard deviation of sample = 10.4
# Both means and stdevs are close to each other, happy accident?

#EXERCISE 1
# For this situation, decide whether you should do randomized sampling or 
# stratified sampling: 
# You are traveling across the United States 
# and recording the heights of 1000 people to find out the average height in the US.
# Randomized sampling.
# You live in a state that has 20,000 people in one big city and 
# 100 people in a rural area. You and want to sample households in this state 
# to determine how many electronic devices the average household has across all states.
# Stratified sampling.

# EXERCISE 2
# You are given the following partially completed function and a file 
# julytemps.txt containing the daily maximum and minimum temperatures 
# for each day in Boston for the 31 days of July 2012. 
# In the loop, we need to make sure we ignore all lines that 
# don't contain the relevant data.
def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
        # FILL THIS IN
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)
# Be sure that you have looked through the raw data file 
# and that you understand which lines do and do not contain relevant data. 
# Which set of conditions would capture all non-data lines 
# (ie, provide a filter that would catch anything that wasn't relevant data)? 
# fields is the variable that contains a list of elements in a line.
# test
# print(loadFile())
# Also valid:
# if len(fields) < 3 or not fields[0].isdigit():
# if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
# if not fields[0].isdigit() or len(fields) < 3: IS NOT VALID, because first check
# will throw an error. First assure the first element is a digit, then check the length.
# Suppose you defined diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps)) 
# to be a list which is the element-by-element difference between 
# highTemps and lowTemps. Which is a valid plotting statement for a graph 
# with days on the horizontal axis and the temperature difference on the vertical axis?
# pylab.plot(range(1, 32), diffTemps)