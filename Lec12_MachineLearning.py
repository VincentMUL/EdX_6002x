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

