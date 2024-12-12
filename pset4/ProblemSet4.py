# In this problem set, you will use regression analysis to model the climate of different areas 
# and try to find evidence of global warming. 
# You will create models to analyze and visualize climate change in terms of temperature. 
# Download ps4.zip.
# Please do not rename the files we provide you with, change any of the provided helper functions, 
# change function/method names, or delete provided docstrings. You will need to keep data.csv in the same folder as ps4.py.
# To model the change in climate of an area, you will need some data. For this problem set, 
# we will use temperature data obtained from the National Centers for Environmental Information (NCEI). 
# The data, stored in data.csv , contains the average temperatures observed in 21 U.S. cities from 1961 to 2015. 
# Open the file, and take a look at the raw data.
# In order to parse the raw data, in ps4.py w e have implemented a helper class Climate. 
# You can initialize an instance of the Climate class by providing the filename of the raw data. 
# Look over this class and read its docstrings to figure out how to get data for the following problems.

# Problem 1: Curve Fitting
# Implement the generate_models function.
#
#x and y are two lists corresponding to the x-coordinates and y-coordinates of the data samples (or data points); 
# for example, if you have N data points, x = [x1 , x2 , ..., xN ] and y = [y1 , y2 , ..., yN ], 
# where x_i and y_i are the x and y coordinate of the i-th data points. 
# In this problem set, each x coordinate is an integer and corresponds to the year of a sample (e.g., 1997); 
# each corresponding y coordinate is a float and represents the temperature observation (will be computed in multiple ways) of that year in Celsius. 
# This representation will be used throughout the entire problem set.
# 
# degs is a list of integers indicating the degree of each regression model that we want to create. 
# For each model, this function should fit the data (x,y) to a polynomial curve of that degree.
# 
# This function should return a list of models. A model is the numpy 1d array of the coefficients 
# of the fitting polynomial curve. Each returned model should be in the same order as their corresponding integer in degs.
#
# Example: print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2])) should print something close to:
# [array([ 1.10000000e+00, -2.15270000e+03]), array([ -8.86320195e-14, 1.10000000e+00, -2.15270000e+03])]
#
# The above example was generating a linear and a quadratic curve on data samples (xi, yi ) = (1961, 4.4), (1962, 5.5), and (1963, 6.6). 
# The resulting models are in the same order as specified in degs. Note that it is fine you did not get the exact number because of numerical errors.

import numpy as np
import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')]) # date is in the format YYYYMMDD
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]



"""
End helper code
"""

# Example: print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2])) should print something close to:
# [array([ 1.10000000e+00, -2.15270000e+03]), array([ -8.86320195e-14, 1.10000000e+00, -2.15270000e+03])]

# Problem 1
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    for deg in degs:
        model = np.polyfit(x, y, deg)
        models.append(model)
    return models

# Test generate_models:
# print(generate_models([1961, 1962, 1963],[4.4,5.5,6.6],[1, 2]))

#GRADER TEsts:
# Test: generate_models([1900, 1901, 1902, 1904, 2000], [32.0, 42.0, 31.3, 22.0, 33.0], [2])
# Output:
# [array([  3.51667102e-02,  -1.37199002e+02,   1.33764160e+05])]
# Test: generate_models([1961, 1962, 1963], [4.4, 5.5, 6.6], [1, 2])
# Output:
# [array([  1.10000000e+00,  -2.15270000e+03]), array([ -8.86320608e-14,   1.10000000e+00,  -2.15270000e+03])]
# Test: generate_models([1960, 1997, 1999, 2001], [-3.1, -4.1, -9.2, 10.1], [1, 2, 3])
# Output:
# [array([  7.64961915e-02,  -1.53745049e+02]), array([  9.24663056e-02,  -3.66029000e+02,   3.62195201e+05]), array([  7.59680860e-02,  -4.52530612e+02,   8.98514989e+05,
#         -5.94652222e+08])]
# Test: generate_models([1960, 1997, 1999, 2001, 1998, 1995], [-3.1, -4.1, -9.2, 10.1, 9.1, 4.5], [1, 2, 3, 4])
# Output:
# [array([  1.43651226e-01,  -2.84888692e+02]), array([  1.45050481e-02,  -5.72778422e+01,   5.65389304e+04]), array([  2.41178585e-02,  -1.43636842e+02,   2.85137445e+05,
#         -1.88670385e+08]), array([  1.14194270e-02,  -9.08068327e+01,   2.70778566e+05,
#         -3.58853930e+08,   1.78337425e+11])]

# Problem 2: R²
# 
# After we create some regression models, we also want to be able to evaluate our models to figure out how well each model represents our data, 
# and tell good models from poorly fitting ones. One way to evaluate how well the model describes the data is computing the model's R^2 value. 
# R^2 provides a measure of how well the total variation of samples is explained by the model.
#
# Implement the function r_squared. This function will take in:
#   a list, y, that represents the y-coordinates of the original data samples
#   estimated, which is a corresponding list of y-coordinates estimated from the regression model
#
# This function should return the computed R² value. You can compute R² as follows, 
# where e[i] is the estimated y value for the i-th data point (i.e. predicted by the regression), 
# y[i] is the y value for the ith data point, and mean is the mean of the original data samples.
#
# If you are still confused about R², its wikipedia page has a good explanation about its use/how to calculate it:
# https://en.wikipedia.org/wiki/Coefficient_of_determination 

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    mean = np.mean(y)
    numerator = 0
    denominator = 0
    for i in range(len(y)):
        numerator += (y[i] - estimated[i])**2
        denominator += (y[i] - mean)**2
    return 1 - (numerator/denominator)

# Test r_squared:
# print(r_squared([1,2,3], [1,2,3])) # 1.0

#GRADER TESTS:
# Test: r_squared([32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0])
# Output:
# 0.9944
# Test: r_squared([4.4, 5.5, 6.6], [4.4, 5.5, 6.6])
# Output:
# 1.0000
# Test: r_squared([-3.1, -4.1, -9.2, 10.1], [-2.1, -6.1, 9.2, 20.1])
# Output:
# -1.1834
# Test: r_squared([-3.1, -4.1, -9.2, 10.1, 9.1, 4.5], [-1.1, -2.1, -7.2, 11.1, 11.1, 5.5])
# Output:
# 0.9414

# Problem 3:
# 
# We have learned how to obtain a numerical metric for evaluation. 
# Visualizing our data samples along with fitting curves can also help us figure out the goodness of obtained models. 
# In this problem, we will integrate the numerical metrics and visualization for a comprehensive evaluation.
# 
# Implement function evaluate_models_on_training. This function takes as input your data samples (x and y) 
# and the list of models (which are lists of coefficients obtained from generate_models) that you want to apply to your data.
# This function should generate a figure for each model. In this figure, you are to plot your data along with your best fit curve, 
# and report on the goodness of the fit with the R^2 value. When you are writing this function try to make your graph match the following format:
#   + Plot the data points as individual blue dots
#   + Plot your model as a red solid line
#   + Include a title and label your axes
#   + Your title should include the value of your model and the R^2 degree of this model. Your title could be longer than your graph. 
#     To fix that you can add "\n", which adds a newline to your string, in your title when you concatenate several pieces of information 
#     (e.g., title = string_a + "\n" + string_b ).
# 
# After you finish writing the function, you have all the components needed to start generating data samples from the raw temperature records and investigate the trend. 
# Run the following code at the bottom ps4.py.
# # Problem 3
# y = []
# x = INTERVAL_1
# for year in INTERVAL_1:
#     y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
# models = generate_models(x, y, [1])
# evaluate_models_on_training(x, y, models)
#
# This code just randomly picks a day from a year (i.e., Jan 10th in this case), and sees whether we can find any trend in the temperature changing over the years. 
# We surmise, due to global warming, that the temperature of this specific date should increase over time. 
# This code generates your data samples; each sample represents a year from 1961 to 2005 
# (i.e., the years in INTERVAL_1) and the temperature of Jan 10th for Boston in that year (provided helper class is helpful for this). 
# The code fits your data to a linear line with generate_models and plots the regression results with evaluate_models_on_training.
#
# Problem 3
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    for model in models:
        pylab.plot(x, y, 'bo', label='Data')
        estYVals = np.polyval(model, x)
        pylab.plot(x, estYVals, 'r', label='Fit')
        pylab.title('Degree of model: ' + str(len(model)-1) + '\n' + 'R²: ' + str(r_squared(y, estYVals)))
        pylab.xlabel('Year')
        pylab.ylabel('Temperature')
        pylab.show()


### Begining of program
raw_data = Climate('data.csv')

# Problem 3
y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)

#
# What is the R² value? (use 3 decimal places)
# 0.005

#Problem 4:
#
# Let's try another way to get data points and see whether we can find some evidence for global warming. 
# We surmise, due to global warming, the average temperature should increase over time. 
# Thus, we are going to plot the results of a linear regression on the average annual temperature of Boston.
#
# In a similar manner to Problem 3, fill in the missing piece to the following code. The code should generate your data samples. 
# Each sample represents a year from 1961 to 2005 and the average annual temperature in Boston in that year (again, the provided helper class is helpful). 
# Fit your data to a linear line with generate_models and plot the regression results with evaluate_models_on_training.
# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
for year in x1:
    y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))
models = generate_models(x, y, [1])    
evaluate_models_on_training(x, y, models)
# What is the R² value? (use 3 decimal places)
# 0.085

#Problem 5:
# Which graph, choosing a specific day (Jan 10) or calculating the yearly average, 
# indicates that almost none of the data variation is learned by our model?
# Choosing a specific day
# Which graph, choosing a specific day (Jan 10) or calculating the yearly average, 
# supports more the claim that global warming is leading to an increase in temperature?
# Calculating the yearly average

