import random

#EXERCISE 3:

# The output of random.randint(1, 10) after a specific seed is shown below.

# >>> import random
# >>> random.seed(9001)
# >>> random.randint(1, 10)
# 1
# >>> random.randint(1, 10)
# 3
# >>> random.randint(1, 10)
# 6
# >>> random.randint(1, 10)
# 6
# >>> random.randint(1, 10)
# 7
# We would like you to solve this problem using just the above output, 
# without using the interpreter. 
# (Note that the actual output you get when you run the above commands is actually going to be 1, 5, 5, 2, 10) 
# What is printed in the following programs? Separate new lines with commas - so the above output would be 1, 3, 6, 6, 7.

# random.seed(9001)
# for i in range(random.randint(1, 10)):
#     print(random.randint(1, 10))
# Answer: 3

# random.seed(9001)
# d = random.randint(1, 10)
# for i in range(random.randint(1, 10)):
#     print(d)
# Answer: 1, 1, 1

# random.seed(9001)
# d = random.randint(1, 10)
# for i in range(random.randint(1, 10)):
#     if random.randint(1, 10) < 7:
#         print(d)
#     else:
#         random.seed(9001)
#         d = random.randint(1, 10)
#         print(random.randint(1, 10))
# Answer: 1, 1, 3

#EXERCISE 4:
# Suppose we wanted to create a class PolarBearDrunk, 
# a drunk polar bear who moves randomly along the x and y axes 
# taking large steps when moving South, and small steps when moving North.
#
# class PolarBearDrunk(Drunk):
#     def takeStep(self):
#         # code for takeStep()
# Which of the following would be an appropriate implementation of takeStep()?
#
# #Option A)
# directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]
# myDirection = random.choice(directionList)
# if myDirection[0] == 0.0:
#     return myDirection + (0.0, -0.5)# is this supported for tuples? Answer: No, produces
# # tuples of lenght 4
# return myDirection
# # ALTERNATIVE to A would be this:
# directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0)]
# myDirection = random.choice(directionList)
# if myDirection[0] == 0.0:
#     return (myDirection[0], myDirection[1] - 0.5) 
# return myDirection
# 
# #Option B)
# directionList = [(0.0, 0.5), (1.0, -0.5), (-1.0, -0.5), (0.0, -1.5)]
# return random.choice(directionList)
# Always moves a bit more southward
#
# #Option C)
# directionList = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.5)]
# return random.choice(directionList)
# 
# #Option D)
# directionList = [(0.0, 1.0), (1.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, -1.0)]
# return random.choice(directionList)
# Just moves south twice as likely, but the same distance as north.
# Answer: Option C

# We will be visualizing a random walk in this lab.
# A random walk can be used to model real-life phenomena that are not necessarily random. Particle behavior is one of these applications. 
# Using a random walk, we can simulate the path of one or more molecules in a variable-density medium and gain insight into certain processes like diffusion.
# The particles are initially set to move ΔX and ΔY in the range of [-0.5, 0.5] at each step. By increasing the "density" (of arbitrary units)
#  below the plot you can reduce this range, effectively constraining the particle movement.
# Feel free to play with all of the parameters (although be warned that simulating too many particles may slow down and/or crash your browser). 
# Try and guess the simulated particle behavior under certain edge conditions. 
# For instance, what would you expect to happen if one of the sides is much denser than the other?