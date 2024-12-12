#Understanding data is ever present.
#How to get a sense of whether to believe the answers achieved from the data statistics.
#
# Here we will look at the statistics on data from experiments.
# First do experiment to gather data, which can be physical, social or scraped from the internet.
# Second use some theory to generate some questions about the data.
# Third use computation to help answer the questions.
#
# Example of a spring (metal or rubber) experiment.
# Linear springs (stretch or contract linearly with force).
# Linear because the force applied is linear with the distance stretched or compressed.
# Linear springs have a spring constant k, which determines how much force is needed
# to stretch or compress the spring a given distance. A slinky has k of 1 N/m,
# the spring for motorcycle suspension has k of 10^5 N/m.
# A Newton is the amount of force needed to accelerate a 1 kg mass by 1 m per second per second.
# Robert Hooke in 1676 discovered the relationship between force and distance for springs.
# F = -kx, where F is the force, k is the spring constant and x is the distance stretched or compressed.
# Law of Elasticity. The negative sign indicates that the force is in the opposite direction of the stretch or compression.
# The spring constant k is always positive.
# This law holds for a lot of systems, but not all. For instance, all springs have an elastic limit.
# Not all springs behave linearly. For instance, rubber bands and the limbs of a recurve bow.
# How much does a rider need to weigh to compress the spring by 1 cm?
# F = -kx = -35000 N/m * 0.01 m = -350 N. The rider needs to weigh 35 kg. (F = m*g with g = 9.8 m/s^2)
# Here we already knew the k value, but we can also determine it experimentally.
#
# You need to know k for calibrating a spring scale, using atomic force microscopy, etc.
# Also for the double helix of DNA.
# Classic experiment with distance of bottom of string to the stand keeping the string aloft.
# The weight on the spring stretches the spring and the distance between the end of the spring and
# the stand, which is now shorter, is measured. And the difference between the two distances is the stretch.
# If we did this perfectly, and we knew the weight, we could determine the spring constant.
# We can do a little better with repeating with different weights and plotting this.
# Plot shows a linear incline, followed by a plateau. The incline is the linear part of the spring.
# Now we should do a curve fit.
# This is finding a fit that relates an independent variable (in this case the mass of the weight) 
# to an estimated value of a dependent variable (in this case the stretch of the spring).
# 
# Now we need some measure to determine how good the fit is. We require an objective function.
# This function needs to provide a quantitative assessment of how well the fit is.
# Once we have this function, we can formulate the best fitted curve as the curve 
# that minimizes the value of the objective function. Optimization problem!
# Looking for the line that minimizes the distance between the line and the data points.
# You can measure this in X, Y and Perpendicular directions(shortest distance).
# 
# We should use the Y direction, because the point is to predict the dependent variable (Y) 
# from the independent variable (X).
# 
# The most common objective function is the least squares method.
# If observed and predicted are arrays of equal length, then the sum of the squares of the residuals is:
# sum((observed[i] - predicted[i])**2)
# The difference between observed and predicted is often called the residual. 
# Other name is sum of the squares of the residuals. Square and sum, because we want to penalize large errors
# more than small errors. If we didn't square, the sum would be zero. 
# We don't care about the direction of the error. Why not absolute value? Because it is not differentiable.
# Notice how the formula is the variance times the number of the observations. Minimizing this also minimizes the variance.
#
# EXERCISE 1:
# 
# Using the formula derived in this segment, compute k from the second experimental observation: m = 0.15 kg, x = 0.1015 m.
# Use 9.81 m/s^2 as the gravitational constant (g). Enter your answer to at least 1 decimal place of accuracy.
# k = m*g/x = 0.15 kg * 9.81 m/s^2 / 0.1015 m = 14.5 N/m
#
#
# Using linear regression to find the coefficients of a polynomial.
# Polynomial is the sum of a finite number of terms, where each term is of the form c*x^p.
# c is the coefficient and p is the degree of the term. The degree of the polynomial is the highest p.
# For our challenge we're going to use a degree 1 polynomial, which is linear, because Hooke's Law.
# Goal is to find the coefficients of the polynomial that best fits the data.
# Best fit being the fit with the lowest square of residuals. 
# There are many algorithms to solve this, eg the Newton-Raphson method.
# The squared in this function makes it differentiable, which is the convenient analytical property.
#
# Lucky for us, we don't need to implement this ourselves. We can use the pylab library:
# polyfit(obervedx, observedy, degree) returns the coefficients of the polynomial 
# of the given degree that best fits the data (= least squares fit).
# When n is 1 this function returns a tuple with two elements, the slope and the intercept.
# When n is 2 this function returns a tuple with three elements, the coefficients of the quadratic polynomial.

import pylab, numpy

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() #discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def labelPlot():
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    labelPlot()

def fitData(fileName):
    xVals, yVals = getData(fileName) #gives two lists
    xVals = pylab.array(xVals)#turn lists into arrays
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points') #plot points as blue circles
    labelPlot()
    a,b = pylab.polyfit(xVals, yVals, 1) # two coefficients of the linear fit
    # estYVals = a*pylab.array(xVals) + b #using the two coefficients to get the estimated y values
    # might have been obsolete, as we already turned it into an array
    estYVals = a*xVals + b
    print('a =', a, 'b =', b)
    pylab.plot(xVals, estYVals, 'r', label = 'Linear fit, k = '
               + str(round(1/a, 5)))
    pylab.legend(loc = 'best')
    pylab.show()

# fitData('springData.txt')
# a = 0.04643203319205249 b = 0.06562859649122815
# we got the k by looking at 1/a, which is 21.5 N/m
# Why 1/a? Because slope is delta distance over delta force, so 1/slope is delta force over delta distance.
# Notice most points do not lie in the least squares fit, but the fit is still good.
# We're trying the minimize the sum of the squares of the residuals, not the residuals themselves.
#
# Alternatively we could use the function polyval to get the estimated y values.

def fitData1(fileName):
    xVals, yVals = getData(fileName) #gives two lists
    xVals = pylab.array(xVals)#turn lists into arrays
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points') #plot points as blue circles
    labelPlot()
    model = pylab.polyfit(xVals, yVals, 1) # both coefficients assigned to model
    estYVals = pylab.polyval(model, xVals) # easier to write and read for higher degree polynomials
    # More importantly, this line is independent of the degree of the polynomial.
    pylab.plot(xVals, estYVals, 'r', label = 'Linear fit, k = '
               + str(round(1/model[0], 5)))
    pylab.legend(loc = 'best')
    pylab.show()



# Another example using mystery data, looks like a parabola.
# Let's use a higher degree model. 
# model2 = pylab.polyfit(xVals, yVals, 2) # quadratic fit
# pylab.plot(xVals, pylab.polyval(model2, xVals), 'r--', label = 'Quadratic Model')

# xVals, yVals = getData('mysteryData.txt')
# pylab.plot(xVals, yVals, 'o', label = 'Data Points')
# pylab.title('Mystery Data')

# #Try linear model
# model1 = pylab.polyfit(xVals, yVals, 1)
# pylab.plot(xVals, pylab.polyval(model1, xVals),
#           label = 'Linear Model')

# #Try a quadratic model
# model2 = pylab.polyfit(xVals, yVals, 2)
# pylab.plot(xVals, pylab.polyval(model2, xVals),
#           'r--', label = 'Quadratic Model')
# pylab.legend()
# pylab.show()

# By the way, quadratic is also example of linear regression,
# because we are still adding a sum of terms. The linear part is the coefficients.
# Clearly, this is a way better fit than the linear fit for the mystery data.
# Next segment we'll learn a quantitative way to determine how good the fit is.

# EXERCISE 2:
# Which of the following lines will fit a parabola to the spring data given in the lecture file, 
# springData.txt? Check all that work.
# Answer:
# model = pylab.polyfit(xVals, yVals, 2)
# a,b,c = pylab.polyfit(xVals, yVals, 2)
# Suppose the coefficients returned by polyval are in the tuple (c1, c2, c3).
#  Which of the following lines calculate the estimated y values?
# Answer: estYVals = c1*xVals**2 + c2*xVals + c3

# Goodness of Fit:
# How much better is the quadratic fit than the linear fit for the mystery data?
# Evaluate them relatively and absolutely.
# Relative:
# We're finding a function that maps an independent variable to an estimated
# value of a dependent variable. Goodness of fit is equivalent to accuracy of the estimation.
# Since minimizing mean squared error was used, perhaps we should look at this.
# Let's use some code for this
def aveMeanSquareError(data, predicted):
    error = 0.0
    for i in range(len(data)):
        error += (data[i] - predicted[i])**2 #accumulating the squared residuals
    return error/len(data)

def fitData2(fileName):
    xVals, yVals = getData(fileName) #gives two lists
    xVals = pylab.array(xVals)#turn lists into arrays
    yVals = pylab.array(yVals)
    xVals = xVals*9.81 #acc. due to gravity
    pylab.plot(xVals, yVals, 'bo', label = 'Measured points') #plot points as blue circles
    labelPlot()
    model = pylab.polyfit(xVals, yVals, 1) # both coefficients assigned to model
    estYVals = pylab.polyval(model, xVals) # easier to write and read for higher degree polynomials
    # More importantly, this line is independent of the degree of the polynomial.
    pylab.plot(xVals, estYVals, 'r', label = 'Linear fit, k = '
               + str(round(1/model[0], 5)))
    pylab.legend(loc = 'best')
    pylab.show()

# estYVals = pylab.polyval(model1, xVals)
# print('Ave. mean square error for linear model =',
#       aveMeanSquareError(yVals, estYVals))
# estYVals = pylab.polyval(model2, xVals)
# print('Ave. mean square error for quadratic model =',
#         aveMeanSquareError(yVals, estYVals))

# Ave. mean square error for linear model = 9372.730789652878
# Ave. mean square error for quadratic model = 1524.0204471835434
# So it seems to give some indication of the goodness of fit. Six times better in this case.

# What about in absolute terms?
# Mean square error for two different models of the SAME data, but not for different data.
# Or in itself to know if '1524' is good or bad.
#
# For linear regression we can use the coefficient of determination, R².
# equation: R² = 1 - (Σ(yi - estYi)²) / (Σ(yi - meanY)²)
# with y being the observed values, estY being the estimated values (sometimes p for predicted) 
# and meanY (µ) being the mean of the observed values.
# Numerator is amount of error in the estimates and denominator is the variability of the original values.

def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum() #sum of the squared residuals?
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))

# R² is intended to capture the proportion of variability in a data set
#   that is accounted for by the statistical model provided by the fit.
#   If dataset is highly variable, it's harder to fit.
#   Always between 0 and 1 when fit generated by linear regression
#   and tested on training data (= data used for the regression). 
#   Does not hold on out of sample data.
#   if R² 1 is perfect fit the model explains all of the variability of the data, 
#   0.5 is model explains half of all of the variability and 0 is no fit.

def genFits(xVals, yVals, degrees): #takes in list or tuple of degrees
    models = []
    for d in degrees:
        model = pylab.polyfit(xVals, yVals, d)
        models.append(model)
    return models #returns list of models (one for each degree)

def testFits(models, degrees, xVals, yVals, title):
    pylab.plot(xVals, yVals, 'o', label = 'Data')
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i], xVals)#allows us to test models of varying degrees
        error = rSquared(yVals, estYVals)
        pylab.plot(xVals, estYVals,
                  label = 'Fit of degree '\
                  + str(degrees[i])\
                  + ', R² = ' + str(round(error, 5)))
    pylab.legend(loc = 'best')
    pylab.title(title)
    pylab.show()

# xVals, yVals = getData('mysteryData.txt')
# degrees = (1, 2)
# models = genFits(xVals, yVals, degrees)
# testFits(models, degrees, xVals, yVals, 'Mystery Data')
# # linear fit R² = .00049, quadratic fit R² = .83748
# # Still some room, let's try more degrees.

# #Compare higher order fits
# degrees = (2, 4, 8, 16)
# models = genFits(xVals, yVals, degrees)
# testFits(models, degrees, xVals, yVals, 'Mystery Data')
# # Yes, degree 16 gives R² = 0.96553
# # But is this a good fit? No, because it's overfitting. It's fitting the noise in the data
# # See next lecture.

# EXERCISE 4:
# Recall from the previous video the concept of the coefficient of determination, 
# also known as the R² value. 
# This is computed by 1 - (Σ(yi - estYi)²) / (Σ(yi - meanY)²) . 
# The variability of the errors is computed by taking the sum of the squares of 
# (observed - predicted) errors. We normalize this variablity by dividing it by 
# the variability of the data, which is sum of the squares of 
# (observation - average_observation) for each observation.
#
# In this file, this R² value is computed by the function rSquare.
# In that file, revise fitData and fitData3 to report the coefficient of determination 
# for the fitted line in each case. Did this measure of the "goodness of fit" improve 
# when we eliminated the measurements after the spring reached its elastic limit 
# and Hooke's Law no longer applied? See lecture10_Ex4.py for the original code.
# The answer is yes, see adjusted code, just added error variable and some extra print in pylab.plot.
# Also had to move the rSquare function to before the fitData functions.