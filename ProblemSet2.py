# Simulation Overview
# iRobot is a company (started by MIT alumni and faculty) that sells the 
# Roomba vacuuming robot (watch one of the product videos to see these robots in action). 
# Roomba robots move around the floor, cleaning the area they pass over.
#
# In this problem set, you will code a simulation to compare 
# how much time a group of Roomba-like robots will take to clean the floor 
# of a room using two different strategies.
#
# The following simplified model of a single robot moving in a square 5x5 room
#  should give you some intuition about the system we are simulating.
#
# The robot starts out at some random position in the room, 
# and with a random direction of motion. The illustrations below show the robot's position 
# (indicated by a black dot) as well as its direction (indicated by the direction of the red arrowhead).
#
# t = 0
# The robot starts at the position (2.1, 2.2) 
# with an angle of 205 degrees (measured clockwise from "north"). 
# The tile that it is on is now clean.
#
# t = 1
# The robot has moved 1 unit in the direction it was facing, 
# to the position (1.7, 1.3), cleaning another tile.
# 
# t = 2
# The robot has moved 1 unit in the same direction (205 degrees from north), 
# to the position (1.2, 0.4), cleaning another tile.
#
# t = 3
# The robot could not have moved another unit in the same direction 
# without hitting the wall, so instead it turns to face in a new, 
# random direction, 287 degrees.
# t = 4
# The robot moves along its new direction to the position (0.3, 0.7), 
# cleaning another tile.
#
# Simulation DETAILS:
# Multiple robots:
# In general, there are N > 0 robots in the room, where N is given. 
# For simplicity, assume that robots are points and can pass through 
# each other or occupy the same point without interfering.
# 
# The room:
# The room is rectangular with some integer width w and 
# height h, which are given. Initially the entire floor is dirty. 
# A robot cannot pass through the walls of the room. 
# A robot may not move to a point outside the room.
#
# Tiles:
# You will need to keep track of which parts of the floor 
# have been cleaned by the robot(s). We will divide the area 
# of the room into 1x1 tiles (there will be w * h such tiles). 
# When a robot's location is anywhere in a tile, 
# we will consider the entire tile to be cleaned (as in the pictures). 
# By convention, we will refer to the tiles using ordered pairs of integers:
# (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), ..., (w-1, h-1).
#
# Robot motion rules:
# Each robot has a position inside the room. 
# We'll represent the position using coordinates (x, y) which are floats 
# satisfying 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances 
# of the Position class to store these coordinates.
# A robot has a direction of motion. 
# We'll represent the direction using an integer d satisfying 0 ≤ d < 360, 
# which gives an angle in degrees.
# All robots move at the same speed s, a float, which is given 
# and is constant throughout the simulation. Every time-step, 
# a robot moves in its direction of motion by s units.
# If a robot detects that it will hit the wall within the time-step, 
# that time step is instead spent picking a new direction at random. 
# The robot will attempt to move in that direction on the next time step, 
# until it reaches another wall.
#
# Termination:
# The simulation ends when a specified fraction of the tiles in the room have been cleaned

# Introduction
# In this problem set you will practice designing a simulation 
# and implementing a program that uses classes.
# As with previous problem sets, p
# lease don't be discouraged by the apparent length of this assignment. 
# There is quite a bit to read and understand, but most of the problems do not involve writing much code.
#
# Getting Started
# Download and save pset2.zip: A zip file of all the files you need, including:
# ps2.py, a skeleton of the solution.
# ps2_visualize.py, code to help you visualize the robot's movement 
#                   (an optional - but cool! - part of this problem set).
# ps2_verify_movement3X.pyc, precompiled module for Python 3.X 
#                           that assists with the visualization code. 
#                           In ps2.py you will import the line where X matches your Python version.  
#                           For example, from ps2_verify_movement39 import testRobotMovement
#
# REVIEW OBJECT ORIENTED PROGRAMMING AND CLASSES
# This and future problem sets will require you to know OOP. If you need a refresher, 
# please visit this link and make sure you are familiar with these topics.
# Implementing new classes and their attributes.
# Understanding class methods.
# Understanding inheritance.
# Telling the difference between a class and an instance of that class - 
# recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.
# Utilizing libraries as black boxes.
# Note: If you want to use numpy arrays, 
#       you should add the following lines at the beginning of your code for the grader:
            # import os
            # os.environ["OPENBLAS_NUM_THREADS"] = "1"
# Then, do import numpy as np and use np.METHOD_NAME in your code.

#Problem 1: RectangularRoom Class
# You will need to design two classes to keep track of which parts of the room have been cleaned as well
# as the position and direction of each robot.
# In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:
    # RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
    # Position: We've also provided a complete implementation of this class. 
    #           It stores the x- and y-coordinates of a robot in a room.
# Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.
# 
# In this problem you will implement the RectangularRoom class. 
# For this class, decide what fields you will use and decide how the following operations are to be performed:
# Initializing the object
# Marking an appropriate tile as cleaned when a robot moves to a given position 
#   (casting floats to ints - and/or the function math.floor - may be useful to you here)
# Determining if a given tile has been cleaned
# Determining how many tiles there are in the room
# Determining how many cleaned tiles there are in the room
# Getting a random position in the room
# Determining if a given position is in the room
# Complete the RectangularRoom class by implementing its methods in ps2.py.
# Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. 
# For reasonable representations, a majority of the methods will require only a couple of lines of code.

#Problem 2: Robot Class

# In ps2.py we provided you with the Robot class, which stores the position 
# and direction of a robot. For this class, decide what fields you will use 
# and decide how the following operations are to be performed:
#
# Initializing the object
# Accessing the robot's position
# Accessing the robot's direction
# Setting the robot's position
# Setting the robot's direction
# Complete the Robot class by implementing its methods in ps2.py.
#
# Note: When a Robot is initialized, it should clean the first tile 
# it is initialized on. Generally the model these Robots will follow is 
# that after a robot lands on a given tile, we will mark the entire tile as clean. 
# This might not make sense if you're thinking about really large tiles, 
# but as we make the size of the tiles smaller and smaller, 
# this does actually become a pretty good approximation.

# Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. 
# For reasonable representations, a majority of the methods will require only a couple of lines of code.

# Note: The Robot class is an abstract class, which means that we will never 
# make an instance of it. Read up on the Python docs on abstract classes 
# at this link and if you want more examples on abstract classes, follow this link.

# In the final implementation of Robot, not all methods will be implemented. 
# Not to worry -- its subclass(es) will implement the method updatePositionAndClean()

# Enter your code for classes RectangularRoom (from the previous problem) 
# and Robot below.

# Problem 3: StandardRobot Class
# Each robot must also have some code that tells it how to move about a room, 
# which will go in a method called updatePositionAndClean.

# Ordinarily we would consider putting all the robot's methods in a single class. 
# However, later in this problem set we'll consider robots with alternate movement strategies, 
# to be implemented as different classes with the same interface. 
# These classes will have a different implementation of updatePositionAndClean 
# but are for the most part the same as the original robots. 
# Therefore, we'd like to use inheritance to reduce the amount of duplicated code.

# We have already refactored the robot code for you into two classes: 
# the Robot class you completed in Problem 2 (which contains general robot code), 
# and a StandardRobot class that inherits from it (which contains its own movement strategy).

# Complete the updatePositionAndClean method of StandardRobot to simulate the motion of 
# the robot after a single time-step (as described on the Simulation Overview page).

class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

# We have provided the getNewPosition method of Position, which you may find helpful:

class Position(object):

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
# Note: You can pass in an integer or a float for the angle parameter.

# Before moving on to Problem 4, check that your implementation of StandardRobot works 
# by uncommenting the following line under your implementation of StandardRobot. 
# Make sure that as your robot moves around the room, the tiles it traverses switch colors from gray to white. 
# It should take about a minute for it to clean all the tiles.

# testRobotMovement(StandardRobot, RectangularRoom)

# Problem 4: Running the Simulation
# 
# In this problem you will write code that runs a complete robot simulation.
# Recall that in each trial, the objective is to determine how many time-steps 
# are on average needed before a specified fraction of the room has been cleaned. 
# Implement the following function:
# def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
#                   robot_type):
#     """
#     Runs NUM_TRIALS trials of the simulation and returns the mean number of
#     time-steps needed to clean the fraction MIN_COVERAGE of the room.

#     The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
#     speed SPEED, in a room of dimensions WIDTH x HEIGHT.
#     """
# The first six parameters should be self-explanatory. 
# For the time being, you should pass in StandardRobot for the robot_type parameter, like so:
avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
# Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) 
# whenever you wish to instantiate a robot. 
# (This will allow us to easily adapt the simulation to run with different robot implementations, 
# which you'll encounter in Problem 6.)
# Feel free to write whatever helper functions you wish.
# We have provided the getNewPosition method of Position, which you may find helpful:
class Position(object):

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
# For your reference, here are some approximate room cleaning times. 
# These times are with a robot speed of 1.0.

# One robot takes around 150 clock ticks to completely clean a 5x5 room.

# One robot takes around 190 clock ticks to clean 75% of a 10x10 room.

# One robot takes around 310 clock ticks to clean 90% of a 10x10 room.

# One robot takes around 3322 clock ticks to completely clean a 20x20 room.

# Three robots take around 1105 clock ticks to completely clean a 20x20 room.

# (These are only intended as guidelines. 
# Depending on the exact details of your implementation, 
# you may get times slightly different from ours.)

# You should also check your simulation's output for speeds other than 1.0. 
# One way to do this is to take the above test cases, change the speeds, and make sure the results are sensible.
# For further testing, see the next page in this problem set about the optional way to use visualization methods. 
# Visualization will help you see what's going on in the simulation and may assist you in debugging your code.

# Enter your code for the definition of runSimulation below.

# Problem 5: RandomWalkRobot Class

# iRobot is testing out a new robot design. 
# The proposed new robots differ in that they change direction randomly after every time step, 
# rather than just when they run into walls. You have been asked to design a simulation to determine what effect, 
# if any, this change has on room cleaning times.
#
# Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) 
# but implements the new movement strategy. RandomWalkRobot should have the same interface as StandardRobot.
#
# Test out your new class. 
# Perform a single trial with the StandardRobot implementation and watch the visualization 
# to make sure it is doing the right thing. Once you are satisfied, 
# you can call runSimulation again, passing RandomWalkRobot instead of StandardRobot.
#
# Enter your code for classes Robot and RandomWalkRobot below.

# Problem 6: Data Plotting
# Now, you'll use your simulation to answer some questions about the robots' performance.

# In order to do this problem, you will be using a Python tool called PyLab. 

# Below is an example of a plot. 
# This plot does not use the same axes that your plots will use; 
# it merely serves as an example of the types of images that the PyLab package produces.
# Note to those who did the optional visualization: 
# For problem 6, we make calls to runSimulation() to get simulation data and plot it. 
# However, you don't want the visualization getting in the way. 
# If you chose to do the visualization exercise, before you get started on problem 6 
# (and before you submit your code in submission boxes), 
# make sure to comment the visualization code out of runSimulation(). 
# There should be 3 lines to comment out. If you do not comment these lines, 
# your code will take a REALLY long time to run!

# For the questions below, call the given function with the proper arguments to generate a plot using PyLab.

# Examine showPlot1 in ps2.py, which takes in the parameters title, x_label, and y_label. 
# Your job is to examine the code and figure out what the plot produced by the function tells you. 
# Try calling showPlot1 with appropriate arguments to produce a few plots. 
# Then, answer the following 3 questions.