# Machine learning is a very hot topic. Made lot of money and modern tech.
# This is just exposure to the concept.

# Many useful programs learn from data.
# For example implementation of Newton's method, learns the root of a polynomial.
# Arthur Samuel: "Field of study that gives computers the ability to learn 
# without being explicitly programmed." (He's known for the checkers program)
# It's where statistics meets optimization.
# Traditional programming: Data and program in Computer -> output
# Machine learning: Data and output in Computer -> program
#                   We can then feed new data in that program and get output.
#                   Exactly what we did in curve fitting.
#                   We put in indep and dep values (I/O), got a program/model
#                   which we can use to predict new values.
#
# Humans learn by memorization:
#   1. Accumulation of individual facts
#   Limited by time to observe and memory to store.
#   2. Generalization from examples
#   Deduce new facts from old facts, essentially predictive activity.
#   Limited by accuracy of deduction and assumes world doesn't change.
# Machine learning is the same.

# Basic Paradigm:
#   1. Training Data: Observe set of examples
#   2. Learning Algorithm: Infer a function from the examples
#      Infer something about process that generated the data.
#   3. Prediction: Use the function to predict new examples
#      Use inference to make prediction of unseen data: test data.

# Machine Learning Methods Require:
#   Representation of features (feature vectors)
#   Distance metric for feature vectors (measure similarity)
#   Objective function (eg mean squared error) and constraints (eg degree of poly) to optimize
#   Optimization method (eg gradient descent) to learn the model, 
#   which will minimize or maximize the objective function.
#   Evaluation method (eg cross validation) to test the model,
#   and decide if the model is good enough. Not only to determine if we believe
#   the model is correct, but also to tweak and tune the parameters.
#  
# Broadly either Supervised or Unsupervised Learning: 
#  Supervised: Start with set of feature vector-value pairs, with
#              the goal of finding a model that predicts a value for an unseen feature vector.
#              Given input and output data, learn a function that maps input to output.
#              Regression model predicts real number, infinite number of outcomes (as with linear regression)
#              Classification model predicts a label from a finite set of labels. (eg malignant or benign)
#  Unsupervised: Start with feature vectors without labels, 
#                with the goal of finding (latent) structure in the set of feature vectors (data).
#                Clustering: Grouping similar data points together.
#                Define some metric that captures how similar one feature vector is to another.
#                And group them together based on this metric. Depending on choice of features, different structurs emerge.
#                Suppose there are labels for the data and learn the model, the choice of features matters.               
# Choice of features is critical in both supervised and unsupervised learning.
# Ideally, we want to choose features that fully describe the data, but not realistic.
# Features never fully describe the situation -> Feature engineering:
#   1. Represent examples by feature vectors to facilitate generalization.
#   2. Choose features that are relevant to the task. Some are helpful, some will cause to overfit.
# Maximize the signal, minimize the noise. SNR!!

# EXERCISE 1:
# For the following problems, decide whether it would be better to perform supervised 
# or unsupervised learning given the data.

# 1. 100,000 emails are read and marked as spam or not spam, depending on some metrics 
#    measured on their content(keywords, length, etc). We want to determine what a new email will be marked as.
#    Supervised learning. We have the labels for the data. 
#    We can learn a model that predicts the label of a new email.
# 2. A junkyard has 500 objects with 2 and 4 wheels. 
#    We want to separate the objects into 4 different groups.
#    Unsupervised learning. We don't have labels for the data.
# 3. A group of 1000 students are asked for a sample of their handwriting. 
#    Researchers make pairs of (handwritten text, typed text). 
#    Given a new handwriting sample from a new student, 
#    we want to determine what the typed version of the handwriting sample would be.
#    Supervised learning. We have the labels for the data.
# 4. Given a set of t-shirts, we want to organize them in 3 different piles.
#    Unsupervised learning. We don't have labels for the data.
# 5. Given a greenhouse full of plants, we want to organize them so that they can be given away to 
#    novice, intermediate, and expert plant handlers.
#    Unsupervised learning. We don't have labels for the data.
# 6. Given a set of colored points on an x-y axis, we want to place a new point on the plot, knowing its color.
#    Supervised learning. We have the labels for the data.
# 7. A school documents the age, grade, score on a math standardized test, 
#    and score on a writing standardized test for every student. 
#    A new student comes to the school and we want to decide what grade they should be placed in.
#    Supervised learning. We have the labels for the data.

# All ML methods require:
# 1. Representation of features
# 2. Distance metric for feature vectors
# 3. Objective function and constraints
# 4. Optimization method
# 5. Evaluation method
# 
# SUPERVISED LEARNING
#
# Talked about SNR maximization, now distance metric for feature vectors.
# There's Euclidian distance: sqrt((x1-x2)^2 + (y1-y2)^2), based on right triangle.
# Manhattan distance forces you to use the base and height of the triangle.
# Based on Euclidian or Mahattan metric, closest point can be different.
# Minkowski distance is a generalization of Euclidian and Manhattan distance.
# It's a weighted sum of the absolute differences of the features.
#
# Example of animals and their features and label for each (reptile or not in this case).
# Now, what is the Euclidian distance between each animal?
# Wrote some code creating a Distance matrix.
# (eg distance cobra and rattlesnake is 0, but cobra and chicken is 2.236)


import pylab, math, numpy

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

class Animal(object):
    def __init__(self, name, features):
        """Assumes name a string; features a list of numbers"""
        self.name = name
        self.features = pylab.array(features)
        
    def getName(self):
        return self.name
    
    def getFeatures(self):
        return self.features
    
    def distance(self, other):
        """Assumes other an Animal
           Returns the Euclidean distance between feature vectors
              of self and other"""
        return minkowskiDist(self.getFeatures(),
                             other.getFeatures(), 2)
                             
    def __str__(self):
        return self.name

def compareAnimals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of Euclidean distance between each animal"""
    #Get labels for columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #Get distances between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            if a1 == a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #Produce table
    table = pylab.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.138]*len(animals))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    help(table.scale)
    table.scale(1, 2.5)
    pylab.axis('off')
    pylab.savefig('distances')

cobra = Animal('cobra', [1,1,1,1,0])
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa\nconstrictor', [0,1,0,1,0])
chicken = Animal('chicken', [1,1,0,1,2])
alligator = Animal('alligator', [1,1,0,1,4])
dartFrog = Animal('dart frog', [1,0,1,0,4])
zebra = Animal('zebra', [0,0,0,0,4])
python = Animal('python', [1,1,0,1,0])
guppy = Animal('guppy', [0,1,0,0,0])
animals = [cobra, rattlesnake, boa, chicken, guppy,
           dartFrog, zebra, python, alligator]

columnLabels = []
precision = 3 # number of digits in table
for a in animals:
    columnLabels.append(a.getName())
rowLabels = columnLabels[:] # labels happen to be the same in this case
tableVals = []
#Compute the value for each cell: Get distances between pairs of animals
for a1 in animals:#For each row
    row = []
    for a2 in animals:#for each column
        if a1 == a2: #for comparing animal to itself, just put '--'
            row.append('--')
        else:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))#append to the row
    tableVals.append(row)#append to the table, essentially a list of the rows

#producing a table using pylab
table = pylab.table(rowLabels = rowLabels, colLabels = columnLabels,
                    cellText = tableVals,
                    cellLoc = 'center', loc = 'center',
                    colWidths = [0.2]*len(animals))
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1)
pylab.axis('off')
pylab.savefig('distances')
pylab.show()
# Hard to find the right scale. So, we can scale the table.
# We can use the scale method of the table object.

# How to use the distance matrix (values existing in code).
# Use nearest neighbor algorithm to classify a new animal. (simple classification)
# Training is simply 'remembering' the training data.
# When predicting label of a new example, find the closest training example.
# And predict the label of the new example to be the same as the closest training example.
# What if the closes training example is more like an outlier in the group of its label?
# Use K-nearest neighbor algorithm. Instead of just one closest training example, use K closest.
# Choose some value for K, usually odd, like 3, and instead of using single nearest neighbor, use 3.
# In other words, use K nearest neighbors to choose the label of the new example, based on majority of K.
# Has advantages and disadvantages.
# Advantage: Learning really fast, no theory required, easy to explain. 
# Disadvantage: Slow to predict (not really brute force, but still intensitve) 
#               and memory intensive (have to store all the training data).
#               Also, there is no real model to shed light on process that generated the data.
# Logistic regression is most used, covered in text book,
#...
# To fill in someday...
#...

#Use KNN to classify animals.
# Use it to classify zebra, python and alligator. Zebra and python correctly classified.
# All are pretty clear, but alligator is a bit tricky. (2 out of 3 not reptiles)
# Look at feature vector of alligator, differs from cobra in 2 places and from dart frog in 3 places.
# Yet, distance alligator to snakes is 4.123 and from dart frog is 1.732. Why?
# All about scaling. All of features except number of legs are binary. Number of legs has a more
# dynamic range and therefore larger weight (4 is bigger number than 1). Change feature vector to
# normalize the features. (eg divide by 4) Or use binary, has legs, 1 or 0. Suddenly chicken closer.
# Other 2 closest are reptiles. Sometimes reducing numerical features to binary may cause information loss.
# While wanting to maintain relative distance within a feature across animals, we want each feature to
# also be comparable to other features. So, we can normalize the features.
# Two most common ways of scaling: Z-scaling and Interpolation.
# In each case start by accumulating all values for a specific feature.
# Both convert the value of the features.
# Z-scaling: Subtract the mean and divide by the standard deviation.
#            Resulting in each feature having a mean of 0 and a stdev of 1.
# Interpolation: Map minimal value to 0 and maximal value to 1 and linearly interpolate in between.
#                Subtract the min and divide by the range.
#                Resulting in each feature having a min of 0 and max of 1.
def zScaleFeatures(vals):
    """Assumes vals is a sequence of floats"""
    result = pylab.array(vals)
    mean = float(sum(result))/len(result)
    result = result - mean
    # return result/stdDev(result)
    return result/(numpy.std(result)) #numpy.std is the standard deviation function in numpy

def iScaleFeatures(vals):
    """Assumes vals is a sequence of floats"""
    minVal, maxVal = min(vals), max(vals)
    fit = pylab.polyfit([minVal, maxVal], [0, 1], 1) #fit a line to the data
    return pylab.polyval(fit, vals)

# EXERCISE 2:

# For the following question, check the boxes that correspond to the rules that we may be able to learn. 
# Consider the following set of 6 emails, which classify the email as spam or not. 
# Which of the following rules might we learn? Check all that apply.

# Spam or Not Spam?	Spam	Spam	Spam	Not spam	Not spam	Not spam
# Words in Email	   4	4	      30	      35	      50	      10
# Flagged Words	CASH, BUY, password	cash, free, rolex	cash free, call	only, cancel, sign	free, check, weight	quote, cheap, website
# Rules identified: 
# Emails containing both flagged words "cash" and "free" are marked "spam".
# Emails containing at least one flagged word in all capital letters are marked "spam".

# EXERCISE 3:
# For each of the following situations state whether it would be a good idea to scale the features.
# 1. One feature set is height (in meters) and the other is weight (in kilograms).
#   Yes, because the range of values is different.
# 2. One feature set is the number of detected earthquakes in a city and the other is the population in that city.
#   Yes, because the range of values is different.
# 3. The percent concentration of a virus in a random sampling of healthy and unhealthy people.
#   No, because the range of values is the same.
# 4. The angle of refraction of light (degree that light bends) observed when entering water vs. glass vs a diamond.
#   No, because the range of values is the same.
# We would not scale the latter two becasue the values we are measuring are of the same physical quantity 
# and of the same magnitude.

# UNSUPERVISED LEARNING:
# Clustering: Grouping similar data points together.
# Uncovering latent structure in the data, by partition the set of examples into clusters.
# Important to realize in unsupervised learning there is no single correct answer.
# Answer we get is dictated by the features we choose to use and the distance metric used.
# So not by some set of labels that gives us ground truth.
# Clustering is best posed as an optimization problem. 
# Define the objective function as dissimilarity(C), where C is a set of clusters.
# and variability(c) where c is 1 cluster. 
# Variability of a c is the sum of the distances between each points(e) in the c and the mean of the c.
# Looks like variance, but it's not, because the size of the cluster is not used (no division by size), 
# To penalize bigger incoherent clusters over smaller incoherent clusters. A mistake for a lot
# of examples is worse than a mistake for a few examples.
# So optimization is minimizing dissimilarity(C) = sum of variability(c) for all c in C?
# Not quite, because we could just put each example in its own cluster (each cluster size 1) 
# and minimize dissimilarity. There would be no variability and dissimilarities would be 0.
# So, we need to add a constraint to the optimization problem. Either minimum between clusters,
# if too close use 1 bigger cluster and maximum number of clusters. Prevents trivial solutions.
#
# When using a max number of clusters we can use K-means clustering. Constraint: exactly K non-emtpy clusters.
# Using a greedy algorithm finding an approximation to minimizing the objective function.
# PSEUDOCODE ALGORITHM:
# Randomly choose K examples as the initial centroids.
#   While true:
#       Create K clusters by assigning each example to the closest centroid
# centroid is kind of geographical center of cluster
#       Compute K new centroids by averaging the examples in each cluster
#       If the centroids are the same as the previous iteration, stop ('break')
# We don't have any clusters first, so random k exmples as centroids and then create k clusters, 
# by assigning each example to the closest centroid. Then compute new centroids by averaging the examples 
# in each cluster. If the centroids are the same as the previous iteration, stop.
# See example in lecture, notice how after first average, the centroids move and none of them correspond to
# the original examples. Only in the 0th iteration, the centroids are the same as some of the data points.
# As long as 1 datapoint moves, the centroids of the involved clusters move.
# At some point the centroids move, but the data points don't. Then we have converged.
# K-means does not always works well. It's sensitive to the initial choice of centroids.
# Suppose random choice of centroids starts with 2 centroids in the same cluster, might get stuck in local
# minimum or maximum. (Also, K-means doesn't work well with non-spherical clusters?)
# Mitigating this issue? Run it many times.
# best = kMeans(points)
# for t in range(numTrials):
#     C = kMeans(points)
#     if dissimilarity(C) < dissimilarity(best):
#         best = C
# return best
# 
# Example of picture:
# Use k-means to cluster groups of pixels in an image by color.
# Get the color associated with the centroid of each cluster, ie average color.
# For each pixel in the original image, find the centroid that is its nearest neighbor
# and replace the pixel by that centroid.

# Conclusion:
# Use data to build statistical models that can be used to shed light on system that produce data
# and make predictions about new data.
# Supervised learning, Unsupervised learning and Feature engineering.
# Goal was to wet appetite for ML, not to teach it.

# EXERCISE 4:

# The company Internet Movies, Inc. has found wide success in their streaming movie business. 
# After many long and successful years of delivering content, they have decided to use machine learning 
# to make their business even more successful. Luckily, they already possess a huge dataset 
# that has grown over years and years of user activity – but they need your help to make sense of it! 
# Answer the following questions:
# 1. Let’s start with a simple case. 
#    Assume user Alice is a particularly good member and she makes sure to rate every movie she ever watches 
#    on the website. What machine learning approach would be better for the company to use for determining whether 
#    she would be interested in a new specific movie?
#    Supervised learning. We have the labels for the data.
# 2. Bob, on the other hand, is not that much into ratings. He does watch a lot of movies, 
#    but never takes the time to rate them. For users like Bob, which of the following data can the company use 
#    to determine potential interest in a specific movie? 
#    Check all that apply.
#    A. Metadata of movies: actors, director, genre, etc.
#    B. Length of the movie
#    C. Popularity of the movie amongst other users
#    D. User login patterns
#    Answer: A and C
# Explanation : Length of the movie may or may not be considered. We are more likely to consider 
#               it if we consider very long movies or very short movies as well.
# 3. What machine learning approach should the company use for cases like Bob?
#    Unsupervised learning. We don't have labels for the data.
# 4. Assume all the users of the company have a very simple rule in their movie taste: 
#    they like it if Tom Cruise has the lead role. Any other data is mostly irrelevant. 
#    However, no one in the company knows about this fact. 
#    Which of the following clustering models might be able to detect this rule? Check all that apply.
    # A. Supervised (label: rating), with data: Director, language, genre
    # B. Supervised (label: rating), with data: Movie length, lead role, director
    # C. Unsupervised, with data: Lead role, movie length, rating
    # D. Unsupervised, with data: Lead role, genre, director
    # E. Unsupervised, with data: Number of ratings, lead role
    # Answer: B and C
# Explanation: For supervised learning, we already have ratings for each label. 
#              So for the data to differentate between those with Tom Cruise or not, 
#              we must have the leading role as one of our features. 
#              For unsupervised learning, we must have the lead role as part of our data. 
#              In addition, we must have a way to know whether users like the movie or not, 
#              so we must also know the rating.
# 5. Looking at the options they’re given, the board members choose to go with a supervised model 
#    with lead role as data. You become outraged. "How can you not include movie length? It’s incredibly important!
#    Who watches a 3 hour long movie --" Your fellow data scientist interrupts you. "Yeah, I agree, 
#    but look at these initial results. You see, if we remove movie length, ..." What can your colleague (correctly) 
#    say to convince you? Check all that apply.
    # A. "we can reduce inter-cluster dissimilarity."
    # B. "we can reduce intra-cluster dissimilarity."
    # C. "the model starts to work. It doesn’t work otherwise."
    # D. "we can consume less memory, and the results look almost the same."
    # Answer: B and D
# Explanation: Movie lengths are not sufficiently different between most movies in order to help us 
#              in making the clusters. Reducing intra-cluster dissimilarity is correct because having less 
#              features allows us to differentiate elements within a cluster from each other. 
#              Consuming less memory with similar results is correct because we do not need as much storage 
#              and will save money. The supervised learning model will work and has no limits on the number 
#              of features allowed.

# EXERCISE 5:
# As Professor Guttag said, there are two types of people in this world: 
# those who know programming and those who don’t. To prove this once and for all, you take a random sampling 
# of edX students and put them through a programming test. Assume that the test is entirely fair and 
# that it reflects the exact level of skill each student has. 
# You also ask them to fill out a small questionnaire about their experience with 6.00.2x.
# You receive the results for each student as [Exam grade, Hour spent on 6.00.2x]. 
# That is, if Alice has spent 90 hours on 6.00.2x and received a score of 74 on the exam, 
# you will have [74, 90] as a data point.
# 1. Based on your initial purposes, what should you choose as k?
# k=2, because there are two types of people in this world.
# 2. Should you apply scaling to this data?
# Yes, because the range of values is different.
# You run your clustering algorithm and get two clusters:

# CLUSTER 1	Exam grade	Hours spent on 6.00.2x
# Mean	46.2	4.3
# Variance	15.0	0.91
# CLUSTER 2	Exam grade	Hours spent on 6.00.2x
# Mean	84.5	60.2
# Variance	5.1	6.04
# Results look good – there are indeed two kinds of people, and curiously one kind seems to absolutely love 6.00.2x. However, when you rerun the code, you get the following clusters:

# CLUSTER 1	Exam grade	Hours spent on 6.00.2x
# Mean	12.5	2.34
# Variance	0.29	0.36
# CLUSTER 2	Exam grade	Hours spent on 6.00.2x
# Mean	70.23	35.4
# Variance	8.65	10.84
# 3. You don’t know what to believe (and, indeed, there’s no reason for you to choose one over another). What can you do to fix this and get a stable result?
# Let k = 3 and run the algorithm multiple times. Choose the result with the lowest dissimilarity.

