# Simulations by hand won't be enough to understand the behavior of random walks.
# We need simulations to handle the big numbers.

import random

# random.seed(0) #seed for reproducibility (to be able to repeat the experiment)

# Structure of Simulation:
    # Simulate one walk of k steps -> 1 function
    # Simulate n such walks -> 1 function (multiple trials and accumulate results)
    # Report average distance from origin -> 1 function (report or plots of results))
# Also some useful abstractions; location, field, drunks, etc.

class Location(object): #A 2D location, no flying drunks
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        """other is another Location object"""
        ox = other.x #or should this be other.getX()?
        oy = other.y #or should this be other.getY()?
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

#Notable aspects of class Field:
# - Field is a dictionary, not a list
# - A mapping of drunks to locations
# - Drunk is key, location is value
# - Unbounded size; Drunk can get arbitrarily far from origin
# - Location of drunk is attribute of field, not drunk
# - Allows multiple drunks with no constraints 
#   on how they relate to each other; 2 drunks can be in same location
# - Drunk is hashable, so can be key in dictionary

class Field(object): #A field with multiple drunks
    #key design decision: location of drunk is attribute of field, not drunk
    #because allows to think more easily about drunks in relation to each other
    # -> a field is a mapping of drunks to locations
    def __init__(self):
        self.drunks = {} #field is a dictionary, also restrains how to implement drunk;
        # drunk as key -> type of drunk will have to be hashable
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc #drunk is added to field with location loc
    
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field') #defensive programming, since field is dict
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

class Drunk(object): #A base class to be inherited by subclasses
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name
    def __str__(self):
        if self != None:
            return "This drunk is named " + self.name
        return 'Anonymous'
#Class Drunk is not to be instantiated on its own
#Class Drunk is not intended to be useful on its own
#Two subclasses of Drunk: UsualDrunk and ColdDrunk(moves south)

class UsualDrunk(Drunk):
    """A drunk who moves in a random direction"""
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):#a biased drunk
    """A drunk who moves southward"""
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times; returns the distance between the 
       final location and the location at the start of the walk"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass): #dClass type class, so to simulate walks of as many
    #different types of drunks as we want
    """Assumes numSteps an int >= 0, numTrials an int > 0,
       dClass a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    Homer = dClass() #create drunk by type of drunk
    origin = Location(0, 0) #origin of walk
    distances = [] #list of distances from origin
    for t in range(numTrials):#trial of doing every walk
        f = Field()
        f.addDrunk(Homer, origin)
        # print(walk(f, Homer, numSteps))
        distances.append(round(walk(f, Homer, numSteps), 1))#save the distance of every walk
        #this line of code above was wrong in the lecture, it called walk with numTrials
    return distances #return accumulated results/distances


#drunkTest is set up to do numTrials of trials of random walks of numSteps in length
#using drunks of type dClass
#walkLengths is a tuple of all the lengths of walks we want to simulate
def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a tuple of ints >= 0
       numTrials an int > 0, dClass a subclass of Drunk
       For each number of steps in walkLengths, runs simWalks with numTrials walks and
       prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print('Mean =', round(sum(distances)/len(distances), 4))
        print('Max =', max(distances), 'Min =', min(distances))


# drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
#interesting result; as number of steps increases, the mean distance from origin increases
# in the lecture the mean, max and min was pretty much independent of the number of steps
# Run a sanity check! Try on cases where we think we know the answer
# drunkTest((0,1,2), 100, UsualDrunk) #sanity check
# for us it works, but in lecture it didn't, gave 8 on average.
# Because of a mistake in for loop of simwalks; it called walk with numTrials,
# but it should have been called with numSteps (correct in line 119)

def SimAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

# SimAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)
# # cold drunk moves away farther with higher number of steps, because it moves southward

# EXERCISE 1:

# 1. Would placing the drunk's starting location not at the origin change the distances returned?
# Answer: No, walk uses the starting location and not the actual origin.
# Therefore, no change to the code.
#
# 2. If you were going to use random.seed in a real-life simulation instead of just 
# when you are debugging a simulation, would you want to seed it with 0?
# Answer: No, because that would be a deterministic simulation.

# EXERCISE 2:

# 1. Is the following code deterministic or stochastic?
# import random
# mylist = []

# for i in range(random.randint(1, 10)):
#     random.seed(0)
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         mylist.append(number)
# print(mylist)
# Answer: Stochastic, but only because of the random.randint(1, 10) in the for loop.
# If we remove that line, the code will be deterministic, because of the random.seed(0).

# 2. Which of the following alterations (Code Sample A or Code Sample B) 
#    would result in a deterministic process?
#
# import random
# Code Sample A
# mylist = []
# for i in range(random.randint(1, 10)):
#     random.seed(0)
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         if number not in mylist:
#             mylist.append(number)
# print(mylist) # always prints a list of 7; [7]
# # Code Sample B
# mylist = []
# random.seed(0)
# for i in range(random.randint(1, 10)):
#     if random.randint(1, 10) > 3:
#         number = random.randint(1, 10)
#         mylist.append(number)
#     print(mylist)
# Answer: Code Sample A and B are both deterministic, because of the random.seed(0).
# After seeding, random.randint(1, 10) will always produce the same sequence of numbers. 
# In this case, the first number generated after seeding with 0 is always 7.

