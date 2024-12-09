# Was the nice match in mean and stdev of sample vs population a happy accident?
# Try and answer this with computation of 1000 samples of size 100.

import pylab, random, numpy
from Lec9_DataSampling import getHighs, getMeansAndSDs, makeHist, loadFile

# random.seed(0)
# population = getHighs()
# sampleSize = 100
# numSamples = 1000
# maxMeanDiff = 0
# maxSDDiff = 0
# sampleMeans = []
# for i in range(numSamples):
#     sample = random.sample(population, sampleSize) #take a sample of size 100
#     popMean, sampleMean, popSD, sampleSD =\
#         getMeansAndSDs(population, sample, verbose =False)
#     sampleMeans.append(sampleMean)
#     #find maximum difference between population and sample mean
#     if abs(popMean - sampleMean) > maxMeanDiff: 
#         maxMeanDiff = abs(popMean - sampleMean)
#     #find maximum difference between population and sample stdev
#     if abs(popSD - sampleSD) > maxSDDiff:
#         maxSDDiff = abs(popSD - sampleSD)
# print('Mean of sample means =', 
#     round(sum(sampleMeans)/len(sampleMeans), 3))
# print('Standard deviation of sample means =',
#     round(numpy.std(sampleMeans), 3))
# print('Maximum difference in means =', round(maxMeanDiff, 3))
# print('Maximum difference in standard deviations =', round(maxSDDiff, 3))
# makeHist(sampleMeans, 'Means of Samples', 'Mean', 'Frequency', show = False)
# pylab.axvline(x=popMean, color = 'r') #draw a red line at the population mean
# #v for vertical line, h for horizontal line
# #added it to the histogram
# #
# pylab.show()
#takes a while, 1000 samples of 100, so 100,000 data points
#shape is pretty close to N
# What is the CI? 
# Mean of sample means = 16.294
# Standard deviation of sample means = 0.943
# Maximum difference in means = 3.633
# Maximum difference in standard deviations = 2.457
# So CI is 16.3 +/- 1.96*0.943 = 16.3 +/- 1.85
# So CI is 14.45 to 18.15
# We can be 95% sure that the population mean is in this range.
# This seems correct, see red line.
# 
# Suppose we need a tighter bound? More samples?
# Didn't help much, go to 2000 samples of 100.
# NO, it doesn't change much.
# How about sample size increase? 200 samples?
# Yes, this helps! stdev drops from .9 to .6
#
# Let's check this by using error bars associated with various sample sizes.
# Error bars represent uncertainty. 
# When CI don't overlap, we say they are significantly different statistically.
# When they do overlap, we can't say they are *not* different.
# code:
# pylab.errorbar(xVals, sizeMeans, #x and y values
#                yerr = 1.96*pylab.array(sizeSDs), #y error bars (vertical)
#                fmt = 'o', # format points as circles
#                label = '95% Confidence Interval')
# see how size of error bars get smaller as sample size increases
# Bigger sample size is better: sample size from 100 to 400,
# CI goes from 1.8 CI to about 1.1 CI
# but this is when looking at 400 000 examples, 
# might as well have looked at the whole population!
# So, we need to find a balance between sample size and computational cost.
# What may we conclude from 1 sample? See next segment.

def showErrorBars(population, sizes, numTrials):
    xVals, sizeMeans, sizeSDs = [], [], []
    for sampleSize in sizes:
        xVals.append(sampleSize)
        trialMeans = []
        for t in range(numTrials):
            sample = random.sample(population, sampleSize)
            popMean, sampleMean, popSD, sampleSD =\
                getMeansAndSDs(population, sample, verbose = False)
            trialMeans.append(sampleMean)
        sizeMeans.append(sum(trialMeans)/len(trialMeans))
        sizeSDs.append(numpy.std(trialMeans))
    pylab.errorbar(xVals, sizeMeans,
                   yerr = 1.96*pylab.array(sizeSDs),
                   fmt = 'o', label = '95% Confidence Interval')
    pylab.title('Mean Temperature ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Mean')
    pylab.axhline(y = popMean, color = 'r')
    pylab.show()

# if __name__ == '__main__':
#     random.seed(0)
#     population = getHighs()
#     showErrorBars(population, (50, 100, 200, 300, 400, 500, 600), 100)
# random.seed(0)
# population = getHighs()
# showErrorBars(population, (50, 100, 200, 300, 400, 500, 600), 100)
# Error bars get smaller as sample size increases

# EXERCISE 3:
# The following image shows the average low and average high temperature 
# in from the data in julytemps.txt.
# The errorbars represent the 95% confidence interval. 
# The 95% confidence interval for the average high 
# is 83.5 +/- 12.9 and the 95% confidence interval for the average low is 67.2 +/- 7.3. 
# Are these two means statistically significant at the 95% confidence interval?
# No, plot shows they overlap. 
# Are these two means statistically significant at the 99.7% confidence interval?
# No
# Are these two means statistically significant at the 68% confidence interval?
# Yes
# From the first question, you can tell that the standard deviation is about 6.5 (for high temp) and 3.6 (for low temp). 
# The 68% confidence interval says that 68% of the data falls within one standard deviation of the mean. 
# Calculating mean+/-sigma for the high and low temps does not give an overlap in the error bars.

# #Vizualize data:
# lows=loadFile()[0]
# highs=loadFile()[1]
# # print('Highs:',highs)
# # print('Lows:',lows)
# categories = ['High', 'Low']
# pylab.errorbar(categories, [sum(highs)/len(highs), sum(lows)/len(lows)], 
#                yerr = [1.96*numpy.std(highs), 1.96*numpy.std(lows)], fmt = 'o', label = '95% Confidence Interval')
# pylab.show()
# pylab.errorbar(categories, [sum(highs)/len(highs), sum(lows)/len(lows)],
#                 yerr = [3.0*numpy.std(highs), 3.0*numpy.std(lows)], fmt = 'o', label = '99.7% Confidence Interval')
# pylab.show()
# pylab.errorbar(categories, [sum(highs)/len(highs), sum(lows)/len(lows)],
#                 yerr = [0.68*numpy.std(highs), 0.68*numpy.std(lows)], fmt = 'o', label = '68% Confidence Interval')
# pylab.show()

# What can we conclude form 1 sample?
# More than you might think, thanks to the Central Limit Theorem.
# CLT: 
# 1. The means of the samples in a sample set will be normally distributed.
# 2. This N dist mean of the sample means will be close to the population mean.
# 3. The variance of the sample means will be close to the variance of the population divided by the sample size.
# stdev = sqrt(variance), so stdev of sample means close to stdev of population mean
# We can use this to derive the Standard Error of the Mean (SEM). (estimate of stdev of sample)
# SEM is stdev of sample divided by sqrt(sample size)
# vizualize this:
def sem(popSD, sampleSize):
    return popSD/(sampleSize**0.5)

# sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
# numTrials = 50 #based on 50 trials of each sample size, we can generate a true stdev
# #then we're going to compare the stdev to the sem
# population = getHighs()
# popSD = numpy.std(population)
# sems = []
# sampleSDs = []
# for size in sampleSizes:
#     sems.append(sem(popSD, size))
#     means = []
#     for t in range(numTrials):
#         sample = random.sample(population, size)
#         means.append(sum(sample)/len(sample))
#     sampleSDs.append(numpy.std(means))
# pylab.plot(sampleSizes, sampleSDs, label = 'Std of 50 means')
# pylab.plot(sampleSizes, sems, 'r--', label = 'SEM')
# pylab.title('SEM vs. SD for ' + str(numTrials) + ' Trials')
# pylab.legend()
# pylab.xlabel('Sample Size')
# pylab.ylabel('Standard Deviation')
# pylab.show()
#This seems to show SEM follows stdev remarkably well.
# But to compute the SEM we actually need to know the population stdev!
# We can't know that, so given a single sample,
# how can we estimate the standard deviation of the population?
# Like estimating the mean using the sample mean, 
# we can estimate the stdev using the sample stdev (stdev of mean)
# As shown in graph, not very nice for small samples (error of 14%),
# but for larger samples, the error is only 2%.
# THEREFORE: Once sample is of reasonable size, the sample stdev is 
#            a good approximation of the population stdev.
# Is this only true for our example?
# For instance does the distribution matter (N, uniform, etc)?
# Or does the size of the population matter?
# First: Three distributions: N, uniform, exponential.
# using random.gauss(0,1), random.uniform(), random.expovariate(0.5)
# Gaussian and uniform are symmetrical, exponential is skewed.

def getDiffs(population, sampleSizes):
    popSD = numpy.std(population)
    diffsFract = []
    for sampleSize in sampleSizes:
        diffs = []
        for t in range(100):
            sample = random.sample(population, sampleSize)
            diffs.append(abs(popSD - numpy.std(sample)))
        diffMean = sum(diffs)/len(diffs)
        diffsFract.append(diffMean/popSD)
    return pylab.array(diffsFract)*100

def plotDiffs(sampleSizes, diffs, title, label):
    pylab.plot(sampleSizes, diffs, label = label)
    pylab.xlabel('Sample Size')
    pylab.ylabel('% Difference in SD')
    pylab.title(title)
    pylab.legend()
    

def plotDistributions():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    makeHist(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.figure()
    makeHist(normal, 'Normal', 'Value', 'Frequency')
    pylab.figure()
    makeHist(exp, 'Exponential', 'Value', 'Frequency')
    pylab.show()


def compareDists():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    sampleSizes = range(20, 600, 1)
    udiffs = getDiffs(uniform, sampleSizes)
    ndiffs = getDiffs(normal, sampleSizes)
    ediffs = getDiffs(exp, sampleSizes)
    plotDiffs(sampleSizes, udiffs, 'Sample SD vs. Population SD', 'Uniform population')
    plotDiffs(sampleSizes, ndiffs, 'Sample SD vs. Population SD', 'Normal population')
    plotDiffs(sampleSizes, ediffs, 'Sample SD vs. Population SD', 'Exponential population')
    pylab.show()

compareDists()
# We can see the distribution does matter, less difference in SD sample - pop
# for non-skewed distributions.
# For population size, it doesn't matter, good news!

# How do we estimate mean from a single sample out of a large population?
# 1. Choose sample size based on estimate of skew in population.
# 2. Choose random sample of that size from population.
# 3. Compute mean and stdev of sample.
# 4. Use sample stdev to estimate SEM
# 5. Use SEM to generate CI around the sample mean.
# This works great for independent random samples!
# Next what happens when we get that wrong.
# Try it out on temperature example.