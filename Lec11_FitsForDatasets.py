#Getting the tighter fit. But why?
#Building the model helps us understand the data better and the process that generated it.
#Building the model helps us make predictions about out-of-sample data. (eg spring)
# A model is GOOD if it helps us do these things!!!
#
# So let's review the process that generated the mystery data from Lec10!
import random , pylab
from Lec10_ExperimentalData import getData, genFits, testFits, rSquared

def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a*x**2 + b*x + c
        yVals.append(theoreticalVal + random.gauss(0, 35)) #add noise to theoretical value
        #from the normal distribution with mean 0 and std dev 35
    f = open(fName, 'w')
    f.write('x      y\n')
    for i in range(len(yVals)):
        f.write(str(yVals[i]) + ' ' + str(xVals[i]) + '\n')
    f.close()

#parameters for generating data
xVals = range(-10, 11, 1)
a, b, c = 3, 0, 0
degrees = (2, 4, 8, 16)
# genNoisyParabolicData(a, b, c, xVals, 'MysteryData.txt')

# If it just generates a parabola with some noise, why wasn't the quadratic model the best?
random.seed(0)
genNoisyParabolicData(a, b, c, xVals, 'DataSet1.txt')
genNoisyParabolicData(a, b, c, xVals, 'DataSet2.txt')
#Only difference is the random seed

xVals1, yVals1 = getData('DataSet1.txt')
models1 = genFits(xVals1, yVals1, degrees) # get ds1 and build models1
testFits(models1, degrees, xVals1, yVals1, 'DataSet1.txt')

pylab.figure()
xVals2, yVals2 = getData('DataSet2.txt')
models2 = genFits(xVals2, yVals2, degrees)
testFits(models2, degrees, xVals2, yVals2, 'DataSet2.txt')
pylab.show()

# Why is the degree 16 better for both datasets and not degree 2?
# Because we're looking at R² on the data on which the model was trained.
# It's training error what we're looking at. Small training error
# is necessary for a good model, but not sufficient.
# We want the model to work on out-of-sample data. Other data,
# generated by the same process. It needs to generalize.
# The degree 16 model is better because it's more flexible. 
# It can fit the noise in the data. But it's not a good model.
# It's overfitting the data. It's fitting the noise, not the signal.
# It's not going to work well on out-of-sample data. It's not going to generalize.
# 
# How can we check if our model is well at generalizing?
# We can use cross-validation. We can split the data into two parts.
# Generate the model using one dataset and test it on the other.
# Use models for DataSet1 to predict DataSet2 and vice versa.
# We expect the testing error to be higher than the training error.

pylab.figure
testFits(models1, degrees, xVals2, yVals2, 'DataSet2/Model1')
pylab.show()
pylab.figure
testFits(models2, degrees, xVals1, yVals1, 'DataSet1/Model2')
pylab.show()
#degree 16 fit does not look so good! Why? Noise!

# Exercise 1:

# To model data effectively, it is important to understand the underlying model that describes the data. 
# This means that knowing the physical phenomenon or event that is being modeled is extremely important. 
# For each of the following data/phenomena/events, 
# describe what type of model (linear, quadratic, other) you would use to describe the underlying phenomena.
# Hourly temperature from 7am to 7pm
# Answer: quadratic
# Gravitational force on an object as mass increases
# Answer: linear
# Displacement of a mass on a hanging spring from the ceiling
# Answer: The answer is 'other' because a spring doesn't follow a linear model once the spring goes near or past the elastic limit.
# It is also important to understand physical phenomena and their limitations when modeling data. 
# Which of the following are true?

# Even though hourly temperature fluctuations throughout the day may oscillate 
# for a variety of reasons (wind, cloud cover, etc), the underlying trend is quadratic 
# and using a quadratic model is most appropriate
# Answer: True
# You can eliminate a small number of non-outlier data points in order to construct a model that has a better fit.
# Answer: False
# At some point, some physical phenomena have limitations that do not fit their mathematical models 
# (i.e. springs have an elastic limit).
# Answer: True
# When modeling, the model that has the biggest R^2 value is always the best model.
# Answer: False

# What happens when we increase the order of the polynomial model?
# Is it every possible to get a worse fit by increasing the order of the polynomial model?
# If extra term is useless, it will have a small coefficient. So in theory no.
# But suppose the data is noisy. Then the noise can be fit by the extra terms.
# The higher the order of the polynomial, the more likely it is to fit the noise.
# Example in code:
xVals = (0, 1, 2, 3)
yVals = xVals
pylab.plot(xVals, yVals, label = 'Actual values')
a, b, c = pylab.polyfit(xVals, yVals, 2)
print("a = ", round(a, 4), "b = ", round(b, 4), "c = ", round(c, 4))
estYVals = pylab.polyval((a, b, c), xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()
# The R² is 1.0. The model fits the data perfectly.
# Now let's check the predictive power of the model.
xVals = xVals + (20,)#concatenating tuple 20
yVals = xVals#also 20
pylab.plot(xVals, yVals, label = 'Actual values')
estYVals = pylab.polyval((a, b, c), xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()
#Did very well again.
#Now let's simulate a small error in the data.
xVals = (0, 1, 2, 3)
yVals = (0, 1, 2, 3.1)
pylab.plot(xVals, yVals, label = 'Actual values')
model = pylab.polyfit(xVals, yVals, 2)
print(model)
estYVals = pylab.polyval(model, xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()
# [0.025 0.955 0.005]
# R² =  0.9999057936881771
# Still pretty good. Now let's check the predictive power of the model.
xVals = xVals + (20,)
yVals = xVals
pylab.plot(xVals, yVals, label = 'Actual values')
estYVals = pylab.polyval(model, xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()
# R² =  0.7026164813486407
# Very bad predictor, especially when looking at the plot.
# What would have happened if we used a first degree fit?
xVals = (0, 1, 2, 3)
yVals = (0, 1, 2, 3.1)
pylab.plot(xVals, yVals, label = 'Actual values')
model = pylab.polyfit(xVals, yVals, 1) #just changed from 2 to 1
print(model)
estYVals = pylab.polyval(model, xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()

xVals = xVals + (20,)
yVals = xVals
pylab.plot(xVals, yVals, label = 'Actual values')
estYVals = pylab.polyval(model, xVals)
pylab.plot(xVals, estYVals, 'r--', label = 'Predicted values')
print('R² = ', rSquared(yVals, estYVals))
pylab.legend()
pylab.show()
# [ 1.03 -0.02]
# R² =  0.9994347621290627
# R² =  0.9987682926829268
# The first degree fit is a better predictor than the second degree fit.
# R² training data very similar to R² testing data.

# Conclusion: choosing an over-complex model can lead to overfitting.
#             This in turn risks producing a model that works poorly on out-of-sample data.
#             On the other hand, choosing an insufficiently complex model has other problems.
#             As we saw when fitting a linear on a quadratic model.
# Albert Einstein: "Everything should be made as simple as possible, but not simpler."

# Exercise 2:

# Suppose you are given the following data and are asked to fit a curve to this data.
A = [1,2,3,4,5,6,7,8,9,10]
L = [0.59,18.38, 33.01, 54.14, 72.48, 89.8, 97.07, 112.6, 142.87, 199.84]
# Questions were too easy, comparing linear, quadratic and polynomial fit of order 5 to these data points.
