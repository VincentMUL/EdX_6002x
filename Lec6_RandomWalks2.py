# Now we'll go to visualizing the random walks. We'll use the turtle module for this.
#The style will have 3 aspects. The color of the line and the marker, the shape of the marker,
# and the kind of line (blotted or solid).

import random
import pylab
from Lec6_RandomWalks import simWalks, Field, Location, Drunk, UsualDrunk, ColdDrunk

class styleIterator(object):#will rotate through the sequence of styles,
    #defined by the arguments to init
    def __init__(self, styles):
        self.index = 0  #initialize index to 0, keep track of current position in styles list
        self.styles = styles #stores list of styles

    def nextStyle(self):
        result = self.styles[self.index] #retrieve style at current index
        if self.index == len(self.styles) - 1:#check if current index is at end of list
            self.index = 0#reset index to 0
        else:#if not at end of list; increment index
            self.index += 1
        return result#returns current style
#advantage of this 'ring structur' is you do not need to know the number of required styles in advance

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps') #just to vizualize progress
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))#initialize style iterator
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()#using the style iterator
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.show()

# numsSteps = (10, 100, 1000, 10000)
# simAll((UsualDrunk, ColdDrunk), numsSteps, 100)

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    pylab.figure('drunk locs')#create a new figure
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)#lists transformed into arrays, because absolute values
        yVals = pylab.array(yVals)#due to upcasting?
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, 
                   label = dClass.__name__ + 
                   ' mean loc. = <' + str(meanX) + 
                   ', ' + str(meanY) + '>')
    pylab.title('Location at End of Walks (' + str(numSteps) + ' steps)')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'upper left')
    pylab.show()#!REMEMBER! the show() method determines 'when' the plot is shown
    #if it were under the for loop, it would show after every plot and the title 
    #determined before the for loop would be overwritten
#plots the ending locations and the average x and y distance
#at the end from the origin

random.seed(0)
plotLocs((UsualDrunk, ColdDrunk), 10000, 1000)
#plot shows final location after a trial of 10000 steps
#and there are 1000 trials for each type of drunk
#radius UsualDrunk vs ColdDrunk is similar,
#but the center has moved considerably,
#because on average colddrunk moves 0.2 steps down for every 4 steps
#ie moves down 0.05 for every step
#which explains the linear trend in the distance trend plot

# Adding Wormholes to the field
# Einstein-Rosen bridges

def Oddfield(Field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}#dictionary of wormholes; maps locations to locations
        #random locations as keys and random locations as values for those keys
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc#add wormhole to dictionary

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.getLoc(drunk).getX()
        y = self.getLoc(drunk).getY()
        if (x, y) in self.wormholes:
            self.getLoc(drunk) = self.wormholes[(x, y)]