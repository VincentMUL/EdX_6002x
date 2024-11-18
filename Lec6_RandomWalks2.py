# Now we'll go to visualizing the random walks. We'll use the turtle module for this.
#The style will have 3 aspects. The color of the line and the marker, the shape of the marker,
# and the kind of line (blotted or solid).

import random
import pylab
from Lec6_RandomWalks import simWalks, Field, Location, Drunk, UsualDrunk, ColdDrunk

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles #self.styles is treated as a ring

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')

numsSteps = (10, 100, 1000, 10000)
simAll((UsualDrunk, ColdDrunk), numsSteps, 100)