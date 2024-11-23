# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement312 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
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
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # raise NotImplementedError
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")
        self.width = math.floor(width)
        self.height = math.floor(height)
        self.cleanedTiles = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        loc=(math.floor(pos.getX()), math.floor(pos.getY()))
        if loc not in self.cleanedTiles:
            self.cleanedTiles.append(loc)
        # raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # raise NotImplementedError
        return (m, n) in self.cleanedTiles
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # raise NotImplementedError
        return len(self.cleanedTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # raise NotImplementedError
        return Position(random.randint(0, self.width-1), random.randint(0, self.height-1))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        # raise NotImplementedError
        x = pos.getX()
        y = pos.getY()
        return 0 <= x < self.width and 0 <= y < self.height

# # Test 1 Class creation
# room = RectangularRoom(5, 5)
# room.getNumTiles() 
# # Successfully created a room of size 25
#
# # Test 2 test getNumTiles
# room = RectangularRoom(14, 5)
# room = RectangularRoom(3, 1)
# room = RectangularRoom(5, 4)
# room = RectangularRoom(6, 3)
# room = RectangularRoom(13, 6)
# Successfully created a room of size 78
#
# # Test 3 unclean tiles
#         room = RectangularRoom(4, 6)
#         This tests that all squares are properly marked as unclean
#         by calling the isTileCleaned() and getNumCleanedTiles() methods.
# Successfully created a room of size 24
# Number of cleaned tiles:
#
# Test 4 test cleaningTiles
# room = RectangularRoom(3, 3)
# Successfully created a room of size 9
# Number of clean tiles: 0
# After cleaning, number of clean tiles: 9


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # raise NotImplementedError
        if speed <= 0:
            raise ValueError("Speed must be greater than 0")

        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 360)
        room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # raise NotImplementedError
        if not self.room.isPositionInRoom(self.position):
            raise ValueError("Robot not in room")
        return self.position

    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # raise NotImplementedError
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # raise NotImplementedError
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!

# # Test 1 Class creation
        # Although Robot is an abstract class, we create instances of it for 
        # the purposes of testing your code's correctness.
        # robot = Robot(RectangularRoom(1,2), 1.0)

# Test 2 test getRobotPosition
#         robot = Robot(RectangularRoom(5,8), 1.0)
#         robot.getRobotPosition()

# Test 3 test getRobotDirection
#         robot = Robot(RectangularRoom(5,8), 1.0)
#         robot.getRobotDirection()

# Test 4 test setRobotPosition
#         robot = Robot(RectangularRoom(5,8), 1.0)
#         robot.getRobotPosition()
#         loop 5 times: 
#             * Generate random x, y values
#             * Check if Position(x,y) is in the room
#                 * If so, robot.setRobotPosition(Position(x, y))
#                 * robot.getRobotPosition()
# Output:
# Random position 0: (4.00, 4.00)
# (4.00, 4.00)
# Random position 1: (2.00, 8.00)
# Random position 2: (5.00, 4.00)
# Random position 3: (1.00, 2.00)
# (1.00, 2.00)
# Random position 4: (3.00, 3.00)
# (3.00, 3.00)

# Test 5 test setRobotDirection
#         robot = Robot(RectangularRoom(5,8), 1.0)
#         robot.getRobotDirection()
#         loop 10 times: 
#             * Generate random direction value
#             * robot.setRobotDirection(randDirection)
#             * robot.getRobotDirection()
# Output:
# Test passed
# Random direction: 20
# 20
# Random direction: 81
# 81
# Random direction: 266
# 266
# Random direction: 24
# 24
# Random direction: 109
# 109
# Random direction: 145
# 145
# Random direction: 138
# 138
# Random direction: 25
# 25
# Random direction: 332
# 332
# Random direction: 65
# 65

# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        newPosition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newPosition):
            self.position = newPosition
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction = random.randint(0, 360)
    
# Test: 1 class creation
        # robot = StandardRobot(RectangularRoom(1,2), 1.0)

# Test: 2 test setRobotPosition
#         robot = StandardRobot(RectangularRoom(5,8), 1.0)
#         robot.getRobotPosition()
#         loop 5 times: 
#             * Generate random x, y values
#             * Check if Position(x,y) is in the room
#                 * If so, robot.setRobotPosition(Position(x, y))
#                 * robot.getRobotPosition()
# Output:
# Random position 0: (4.00, 1.00)
#    In room; setting position. Position is now: (4.00, 1.00)
# Random position 1: (1.00, 3.00)
#    In room; setting position. Position is now: (1.00, 3.00)
# Random position 2: (4.00, 2.00)
#    In room; setting position. Position is now: (4.00, 2.00)
# Random position 3: (2.00, 7.00)
#    In room; setting position. Position is now: (2.00, 7.00)
# Random position 4: (5.00, 8.00)

# Test: 3 test setRobotDirection
#         robot = StandardRobot(RectangularRoom(5,8), 1.0)
#         robot.getRobotDirection()
#         loop 10 times: 
#             * Generate random direction value
#             * robot.setRobotDirection(randDirection)
#             * robot.getRobotDirection()
# Output:
# Random direction: 293
#   Setting direction. Direction is now: 293
# Random direction: 283
#   Setting direction. Direction is now: 283
# Random direction: 40
#   Setting direction. Direction is now: 40
# Random direction: 10
#   Setting direction. Direction is now: 10
# Random direction: 227
#   Setting direction. Direction is now: 227
# Random direction: 23
#   Setting direction. Direction is now: 23
# Random direction: 26
#   Setting direction. Direction is now: 26
# Random direction: 314
#   Setting direction. Direction is now: 314
# Random direction: 284
#   Setting direction. Direction is now: 284
# Random direction: 14
#   Setting direction. Direction is now: 14

# Test: 4 test updatePositionAndClean
#         Test StandardRobot.updatePositionAndClean() 

# Output:
# Creating room and robot...
# Setting position and direction to Position(1.5, 2.5) and 90...
# Calling updatePositionAndClean(); robot speed is 1.0
# Passed; now calling updatePositionAndClean() 20 times
# Passed test.

# #Test: 5 test updatePositionAndClean
#         Test StandardRobot.updatePositionAndClean() 

# Output:
# Creating randomly sized room: 7x7 - and robot at speed 0.61...
# Robot initalized at random position
# Was initial position cleaned? True
# Robot initalized at random direction:
# Number of cleaned tiles: 1

# Calling updatePositionAndClean() 30 times...
# Cleaned the minimum number of tiles; test passed.


# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # raise NotImplementedError
    r=robot_type
    timeSteps = []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [r(room, speed) for i in range(num_robots)]
        steps = 0
        anim = ps2_visualize.RobotVisualization(num_robots, width, height) # Initialize the visualization
        # anim = ps2_visualize.RobotVisualization(num_robots, width, height, 0.01) #faster visualization
        while room.getNumCleanedTiles() / room.getNumTiles() < min_coverage:
            for robot in robots:
                anim.update(room, robots)# Update the visualization
                robot.updatePositionAndClean()
            steps += 1
        timeSteps.append(steps)
    anim.done()# Close the visualization
    return sum(timeSteps) / len(timeSteps)

# Uncomment this line to see how much your simulation takes on average
print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))
# print(runSimulation(1, 1.0, 5, 5, 0.78, 30, StandardRobot))



# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # raise NotImplementedError
        newPosition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newPosition):
            self.position = newPosition
            self.room.cleanTileAtPosition(self.position)
            self.direction = random.randint(0, 360)
        else:
            self.direction = random.randint(0, 360)
        

# Test: 1 setRobotPosition
#         robot = RandomWalkRobot(RectangularRoom(4, 9), 1.0)
#         robot.getRobotPosition()
#         loop 5 times: 
#             * Generate random x, y values
#             * Check if Position(x,y) is in the room
#                 * If so, robot.setRobotPosition(Position(x, y))
#                 * robot.getRobotPosition()
# Output:
# Random position 0: (4.00, 9.00)
# Random position 1: (4.00, 7.00)
# Random position 2: (2.00, 9.00)
# Random position 3: (3.00, 1.00)
#   In room; setting position. Position is now: (3.00, 1.00)
# Random position 4: (2.00, 5.00)
#   In room; setting position. Position is now: (2.00, 5.00)

# Test: 2 test setRobotDirection
#         robot = RandomWalkRobot(RectangularRoom(5,8), 1.0)
#         robot.getRobotDirection()
#         loop 10 times: 
#             * Generate random direction value
#             * robot.setRobotDirection(randDirection)
#             * robot.getRobotDirection()
# Output:
# Random direction: 39
#    Setting direction: 39
# Random direction: 267
#    Setting direction: 267
# Random direction: 265
#    Setting direction: 265
# Random direction: 103
#    Setting direction: 103
# Random direction: 61
#    Setting direction: 61
# Random direction: 144
#    Setting direction: 144
# Random direction: 17
#    Setting direction: 17
# Random direction: 163
#    Setting direction: 163
# Random direction: 34
#    Setting direction: 34
# Random direction: 59
#    Setting direction: 59

# Test: 3 test updatePositionAndClean
#         Test RandomWalkRobot.updatePositionAndClean() 
# Output:
# Creating room and robot...
# Setting position and direction to Position(1.5, 2.5) and 90...
# Calling updatePositionAndClean(); robot speed is 1.0
# Passed; now calling updatePositionAndClean() 20 times
# Passed test.

# Test: 4 test updatePositionAndClean
#         Test RandomWalkRobot.updatePositionAndClean() 

# Output:
# Creating randomly sized room: 9x10 - and robot at speed 0.92...
# Robot initalized at random position
# Was initial position cleaned? True
# Robot initalized at random direction
# Number of cleaned tiles: 1

# Calling updatePositionAndClean() 30 times...
# Cleaned the minimum number of tiles; test passed.

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# Best title?
#Time It Takes 1 - 10 Robots To Clean 80% Of A Room
# Best x axis label?
#Number of Robots
# Best y axis label?
#Time-steps
    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# Best title?
#Not sure...
# Best x axis label?
#Aspect ratio
# Best y axis label?
#Time-steps

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
