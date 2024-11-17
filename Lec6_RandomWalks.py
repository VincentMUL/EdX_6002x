# Simulations by hand won't be enough to understand the behavior of random walks.
# We need simulations to handle the big numbers.

import random

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
        xDist = self.x - other.ox
        yDist = self.y - other.oy
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

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0,
       dClass a subclass of Drunk
       Simulates numTrials walks of numSteps steps each.
       Returns a list of the final distances for each trial"""
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances