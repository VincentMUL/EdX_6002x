# Part A: probabilities
# This part of the problem set involves some pencil-and-paper exercises. 
# It will help you practice and understand simple probability and statistics.

# Let's say Alvin will catch the flu with probability of 1/10 during any given month. 
# Let's also assume that Alvin can catch the flu only once per month, 
# and that if he has caught the flu, the flu virus will die by the end of the month. 
# What is the probability of the following events?
# Answer each question in reduced fraction form - eg 1/5 instead of 2/10.

# 1. He catches the flu in September, October and November.
# Answer: 1/10 * 1/10 * 1/10 = 1/1000
# 2. He catches the flu in September and then again in November, but not in October.
# Answer: 1/10 * 1/10 * 9/10 = 9/1000
# 3. He catches the flu exactly once in the three months from September through November.
# Answer: 1/10 * 9/10 * 9/10 + 9/10 * 1/10 * 9/10 + 9/10 * 9/10 * 1/10 = 3*81/1000 = 243/1000
# 4. He catches the flu in two or more of the three months from September through November.
# Answer= 1/1000 + 9/1000 + 9/1000 + 9/1000 = 28/1000 = 7/250

# Part B: 
# Introduction
# In this problem set, using Python and Pylab, you will design 
# and implement a stochastic simulation of patient and virus population dynamics, 
# and reach conclusions about treatment regimens based on the simulation results.

# Background: Viruses, Drug Treatments, and Computational Models
# Viruses such as HIV and H1N1 represent a significant challenge to modern medicine. 
# One of the reasons that they are so difficult to treat is their ability to evolve.
#
# As you may know from introductory biology classes, 
# the traits of an organism are determined by its genetic code. 
# When organisms reproduce, their offspring will inherit genetic information from their parent. 
# This genetic information will be modified, either because of mixing of the two parents' genetic information, 
# or through mutations in the genome replication process, thus introducing diversity into a population.
# Viruses are no exception. Two characteristics of viruses make them particularly difficult to treat. 
# The first is that their replication mechanism often lacks the error checking mechanisms that are present in more complex organisms. 
# This speeds up the rate of mutation. Secondly, viruses replicate extremely quickly (orders of magnitude faster than humans) 
# -- thus, while we may be used to thinking of evolution as a process which occurs over long time scales, 
# populations of viruses can undergo substantial evolutionary changes within a single patient over the course of treatment.
# These two characteristics allow a virus population to acquire genetic resistance to therapy quickly. In this problem set, 
# we will make use of simulations to explore the effect of introducing drugs on the virus population 
# and determine how best to address these treatment challenges within a simplified model.
# Computational modeling has played an important role in the study of viruses such as HIV 
# (for example, see this paper, by MIT graduate David Ho). In this problem, 
# we will implement a highly simplified stochastic model of virus population dynamics. 
# Many details have been swept under the rug (host cells are not explicitly modeled and 
# the size of the population is several orders of magnitude less than the size of actual virus populations). 
# Nevertheless, our model exhibits biologically relevant characteristics 
# and will give you a chance to analyze and interpret interesting simulation data.
# Spread of a Virus in a Person
# In reality, diseases are caused by viruses and have to be treated with medicine, 
# so in the remainder of this problem set, we'll be looking at a detailed simulation of the spread of a virus within a person. 
# We've provided you with skeleton code in ps3b.py.
#
#Part B: Problem 1: Implementing a Simple Simulation (No Drug Treatment)
# We start with a trivial model of the virus population - the patient does not take any drugs 
# and the viruses do not acquire resistance to drugs. 
# We simply model the virus population inside a patient as if it were left untreated.
# 
# SimpleVirus class
# 
# To implement this model, you will need to fill in the SimpleVirus class, 
# which maintains the state of a single virus particle.
# You will implement the methods __init__, getMaxBirthProb, getClearProb,doesClear, and reproduce according to the specifications. 
# Use random.random() for generating random numbers to ensure that your results are consistent with ours.
# Hint: During debugging, you might want to use random.seed(0) so that your results are reproducible.
# 
# The reproduce method in SimpleVirus should produce an offspring by returning a new instance of SimpleVirus with probability: 
# self.maxBirthProb * (1 - popDensity). This method raises a NoChildException if the virus particle does not reproduce. 
# For a reminder on raising execptions, review the Python docs: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
# 
# self.maxBirthProb is the birth rate under optimal conditions 
# (the virus population is negligible relative to the available host cells so there is ample nourishment available). 
# popDensity is defined as the ratio of the current virus population to the maximum virus population 
# for a patient and should be calculated in the update method of the Patient class.
#
# Patient class
# 
# You will also need to implement the Patient class, which maintains the state of a virus population associated with a patient.
# 
# The update method in the Patient class is the inner loop of the simulation. 
# It modifies the state of the virus population for a single time step and returns the total virus population at the end of the time step. 
# At every time step of the simulation, each virus particle has a fixed probability of being cleared (eliminated from the patient's body). 
# If the virus particle is not cleared, it is considered for reproduction. If you utilize the population density correctly, 
# you shouldn't need to provide an explicit check that the virus population exceeds maxPop when you are calculating how many offspring are added to the population
# -- you just calculate the new population density and use that for the next call to update.
#
# Unlike the clearance probability, which is constant, the probability of a virus particle reproducing is a function of the virus population. 
# With a larger virus population, there are fewer resources in the patient's body to facilitate reproduction, 
# and the probability of reproduction will be lower. One way to think of this limitation is to consider that virus particles 
# need to make use of a patient's cells to reproduce; they cannot reproduce on their own. As the virus population increases, 
# there will be fewer available host cells for viruses to utilize for reproduction.
#
# To summarize, update should first decide which virus particles are cleared and which survive by making use of the doesClear method of each SimpleVirus instance, 
# then update the collection of SimpleVirus instances accordingly. With the surviving SimpleVirus instances, update should then call the reproduce method for each virus particle. 
# Based on the population density of the surviving SimpleVirus instances, reproduce should either return a new instance of SimpleVirus representing the offspring of the virus particle, 
# or raise a NoChildException indicating that the virus particle does not reproduce during the current time step. 
# The update method should update the attributes of the patient appropriately under either of these conditions. After iterating through all the virus particles, 
# the update method returns the number of virus particles in the patient at the end of the time step.
#
# HINT: Be very wary about mutating an object while iterating over its elements. 
# It is best to avoid this entirely (consider introducing additional "helper" variables). See the 6.00.2x Style Guide for more information.
# eg iterate over a copy of a list, not a list you are modifying.
#
# Note that the mapping between time steps and actual time will vary depending on the type of virus being considered, 
# but for this problem set, think of a time step as a simulated hour of time.
#
# About the grader: When defining a Patient class member variable to store the viruses list representing the virus population, 
# please use the name self.viruses in order for your code to be compatible with the grader and to pass one of the tests.

import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        return random.random() < self.getClearProb()
        
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        if random.random() < self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        surviving_viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                surviving_viruses.append(virus)
        
        self.viruses = surviving_viruses # update the list of viruses
        popDensity = len(self.viruses) / self.maxPop # population density
        
        new_viruses = []
        for virus in self.viruses:
            try:
                new_viruses.append(virus.reproduce(popDensity))
            except NoChildException:
                pass
        self.viruses += new_viruses # add offspring to the list of viruses
        return len(self.viruses)

# Testing the SimpleVirus class
# virus = SimpleVirus(0.1, 0.05)
# print(virus.getMaxBirthProb())
# print(virus.getClearProb())
# print(virus.doesClear())
# print(virus.reproduce(0.5))
# GRADER TESTS:
# Test: Initialization 1
# Initialize a SimpleVirus

# Output:
# Passed test
# Test: Initialization 2
# Initialize a Patient

# Output:
# Passed test
# Test: SimpleVirus 1
# Initialize a SimpleVirus that is never cleared and always reproduces

# Output:
# v1 = SimpleVirus(1.0, 0.0)
# Testing 'doesClear' and 'reproduce' methods
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# Test completed.
# Test: SimpleVirus 2
# Initialize a SimpleVirus that is never cleared and never reproduces

# Output:
# v1 = SimpleVirus(0.0, 0.0)
# Testing 'doesClear' and 'reproduce' methods
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# v1.doesClear(): False
# Test completed.
# Test: SimpleVirus 3
# Initialize a SimpleVirus that is always cleared and always reproduces

# Output:
# v1 = SimpleVirus(1.0, 1.0)
# Testing 'doesClear' and 'reproduce' methods
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# Test completed.
# Test: SimpleVirus 4
# Initialize a SimpleVirus that is always cleared and never reproduces

# Output:
# v1 = SimpleVirus(0.0, 1.0)
# Testing 'doesClear' and 'reproduce' methods
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# v1.doesClear(): True
# Test completed.
# Test: SimpleVirus 5
# Initialize a SimpleVirus with randomized probabilities

# Output:
# v1 = SimpleVirus(0.97, 0.6)
# Testing reproduce. Be sure your implementation is making EXACTLY ONE call to random.random(), and no other random module calls.
# popDensity = 0.05
# Reproduced successfully
# Reproduced successfully
# Reproduced successfully
# Reproduced successfully
# Reproduced successfully
# Raised 'NoChildException'
# Test completed.
# Test: class Patient 1
# Initialize a Patient with randomized viruses

# Output:
# viruses = [
# SimpleVirus(0.59, 0.95)
# SimpleVirus(0.76, 0.66)
# SimpleVirus(0.94, 0.18)
# ]
# P1 = Patient(viruses, 6)
# P1.getTotalPop() = 3
# Test: class Patient 2
# Create a Patient with virus that is never cleared and always reproduces

# Output:
# virus = SimpleVirus(1.0, 0.0)
# patient = Patient([virus], 100)
# Updating the patient for 100 trials...
# patient.getTotalPop() expected to be >= 100
# Test successfully completed
# Test: class Patient 3
# Create a Patient with virus that is always cleared and always reproduces

# Output:
# virus = SimpleVirus(1.0, 1.0)
# patient = Patient([virus], 100)
# Updating the patient for 100 trials...
# patient.getTotalPop() expected to = 0
# Test successfully completed
# Test: class Patient 4
# Initialize a Patient with randomized viruses

# Output:
# viruses = [
# SimpleVirus(0.88, 0.75)
# SimpleVirus(0.79, 0.81)
# ]
# P1 = Patient(viruses, 9)
# P1.getTotalPop() = 2
# Updating patient 10 times... all exceptions should be handled...
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# len(P1.viruses) < maxPop? True
# Test Completed
# Test: class Patient 5
# Check exception handling by raising different types of exceptions in SimpleVirus.reproduce

# Output:
# Successfully ignored raised exception of type: NameError
# Successfully ignored raised exception of type: ValueError
# Successfully ignored raised exception of type: ZeroDivisionError
# Successfully ignored raised exception of type: AttributeError
# Successfully ignored raised exception of type: TypeError
# Successfully caught raised 'NoChildException'
# Test Completed

# Part B: Problem 2-1: Running and Analyzing a Simple Simulation (No Drug Treatment)
# 
# You should start by understanding the population dynamics before introducing any drug.
#
# Fill in the function simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials) that instantiates a Patient, 
# simulates changes to the virus population for 300 time steps (i.e., 300 calls to update), 
# and plots the average size of the virus population as a function of time; that is, 
# the x-axis should correspond to the number of elapsed time steps, 
# and the y-axis should correspond to the average size of the virus population in the patient. 
# The population at time=0 is the population after the first call to update.
#
# Run the simulation for numTrials trials, where numTrials in this case can be up to 100 trials. 
# Use pylab to produce a plot (with a single curve) that displays the average result of running the simulation for many trials. 
# Make sure you run enough trials so that the resulting plot does not change much in terms of shape and time steps 
# taken for the average size of the virus population to become stable. 
# Don't forget to include axes labels, a legend for the curve, and a title on your plot.
#
# You should call simulationWithoutDrug with the following parameters:
    # numViruses = 100
    # maxPop (maximum sustainable virus population) = 1000
    # maxBirthProb (maximum reproduction probability for a virus particle) = 0.1
    # clearProb (maximum clearance probability for a virus particle) = 0.05
#
# Thus, your simulation should be instantiatating one Patient with a list of 100 SimpleVirus instances. 
# Each SimpleVirus instance in the viruses list should be initialized with the proper values for maxBirthProb and clearProb.
#
# HINT: Your graph should contain one line that represents the average of many different trials. 
#       One way of computing the average involves holding all of your data in one list, with one element for each of 300 time steps, 
#       and adding to each data point during each trial. Then, at the end, each element of the list is divided by the total number of trials, 
#       thus taking the average of each element of the list. 
#       However, if this idea confuses you, feel free to ignore the hint and implement it however makes the most sense to you.
#
# Consult reference documentation on pylab as reference. Scroll down on the page to find a list of all the plotting commands in pylab.
# https://matplotlib.org/stable/api/pyplot_summary.html 
#
# HINT: Compared to the previous problem sets, testing your simulation code is more challenging, because the behavior of the code is stochastic, 
# and the expected output is not exactly known. How do you know whether your plots are correct or not? 
# One way to test this is to run the simulation with extreme input values (i.e. initialization parameters), and check that the output matches your intuition. 
# For example, if maxBirthProb is set to 0.99 instead of 0.1, then you would expect that the virus population rapidly increases over a short period of time. 
# Similarly, if you run your simulation with clearProb = 0.99 and maxBirthProb = 0.1, then you should see the virus population quickly decreasing within a small number of steps. 
# You can also try to vary the input values, and check whether the output plots change as you expect. For example, if you run multiple simuation runs, each time increasing maxBirthProb, 
# the curves in the successive plots should show an "upward" trend, since the virus will reproduce faster with a higher maxBirthProb.
#
# For further testing, we have provided the .pyc (compiled Python) files for the completed Patient and SimpleVirus classes 
# (and for Problem 5, the ResistantVirus and TreatedPatient classes) that you can use to confirm that your code is generating the correct results during simulation.
#
# If you comment out your versions of these classes in ps3b.py, and add the following import statements to the top of your file, 
# you can run the simulation using our pre-compiled implementation of these classes to make sure you are obtaining the correct results. 
# This is a good way to test if you've implemented these classes correctly. 
# Make sure to comment out the import statement and uncomment your implementations before moving to Problem 4.
#
# Use this code in the grader, to plot:
# pylab.plot(YOUR_Y_AXIS_VALUES, label = "SimpleVirus")
# pylab.title("SimpleVirus simulation")
# pylab.xlabel("Time Steps")
# pylab.ylabel("Average Virus Population")
# pylab.legend(loc = "best")
# pylab.show()
# For Python 3.7: from ps3b_precompiled_37 import *

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    time_steps = 300
    virus_population = [0] * time_steps # initialize the virus population list
    for trial in range(numTrials): # run the simulation for numTrials trials
        viruses = [SimpleVirus(maxBirthProb, clearProb) for _ in range(numViruses)] # create a list of SimpleVirus instances
        patient = Patient(viruses, maxPop) 
        for i in range(time_steps):
            virus_population[i] += patient.update()
    avg_virus_population = [x / numTrials for x in virus_population] # average the virus population
    pylab.plot(avg_virus_population, label = "SimpleVirus")
    # pylab.plot(virus_population, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

# Testing the simulationWithoutDrug function
# simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

# A good question to consider as you look at your plot is: about how long does it take before the population stops growing?
# The population stops growing after about 150 time steps. The population grows rapidly at first, but then levels off.

# Part B: Problem 3: Implementing a Simulation With Drugs
#
# In this problem, we consider the effects of both administering drugs to the patient and the ability of virus particle offsprings 
# to inherit or mutate genetic traits that confer drug resistance. As the virus population reproduces, mutations will occur in the virus offspring, 
# adding genetic diversity to the virus population. 
# Some virus particles gain favorable mutations that confer resistance to drugs.
#
# ResistantVirus class
#
# In order to model this effect, we introduce a subclass of SimpleVirus called ResistantVirus. 
# ResistantVirus maintains the state of a virus particle's drug resistances, 
# and accounts for the inheritance of drug resistance traits to offspring. Implement the ResistantVirus class.
#
# HINT: If you are really unsure about how to think about what each child resistances should be changed to, here is a different approach. 
#       If the probability mutProb is successful, the child resistance switches. Otherwise, the child resistance stays the same as the parent resistance.
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        return self.resistances.get(drug, False)


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
        if random.random() < (self.maxBirthProb * (1 - popDensity)):
            resistances = self.resistances.copy()
            for drug, resistance in resistances.items(): # iterate over the resistances dictionary
                if random.random() < self.mutProb:
                    resistances[drug] = not resistance
            return ResistantVirus(self.maxBirthProb, self.clearProb, resistances, self.mutProb)
        else:
            raise NoChildException()

# # Testing the ResistantVirus class
# virus = ResistantVirus(0.1, 0.05, {'guttagonol': False, 'srinol': False}, 0.005)
# print(virus.getResistances())
# print(virus.getMutProb())
# print(virus.isResistantTo('guttagonol'))
# print(virus.isResistantTo('srinol'))
# print(virus.reproduce(0.5, ['guttagonol', 'srinol']))

# Part B: Problem 4: TreatedPatient Class
#
# We also need a representation for a patient that accounts for the use of drug treatments and manages a collection of ResistantVirus instances. 
# For this, we introduce the TreatedPatient class, which is a subclass of Patient. 
# TreatedPatient must make use of the new methods in ResistantVirus and maintain the list of drugs that are administered to the patient.
#
# Drugs are given to the patient using the TreatedPatient class's addPrescription() method. What happens when a drug is introduced? 
# The drugs we consider do not directly kill virus particles lacking resistance to the drug, 
# but prevent those virus particles from reproducing (much like actual drugs used to treat HIV). 
# Virus particles with resistance to the drug continue to reproduce normally. Implement the TreatedPatient class.
#
# HINT: If you are really unsure about how to think about what each child resistances should be changed to, here is a different approach. 
#       If the probability mutProb is successful, the child resistance switches. Otherwise, the child resistance stays the same as the parent resistance.

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        resist_pop = 0
        for virus in self.viruses:
            if all(virus.isResistantTo(drug) for drug in drugResist):
                resist_pop += 1
        return resist_pop


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        surviving_viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                surviving_viruses.append(virus)
        
        self.viruses = surviving_viruses # update the list of viruses
        popDensity = len(self.viruses) / self.maxPop
        new_viruses = []
        for virus in self.viruses:
            try:
                new_viruses.append(virus.reproduce(popDensity, self.drugs))
            except NoChildException:
                pass
        self.viruses += new_viruses # add offspring to the list of viruses
        return len(self.viruses)
    
# # Testing the TreatedPatient class
# virus = ResistantVirus(0.1, 0.05, {'guttagonol': False, 'srinol': False}, 0.005)
# viruses = [virus]
# patient = TreatedPatient(viruses, 1000)
# print(patient.getPrescriptions())
# patient.addPrescription('guttagonol')
# print(patient.getPrescriptions())

# GRADER TESTS:
# Test: TreatedPatient 1
# Create a TreatedPatient with virus that is never cleared and always reproduces.

# Output:
# virus = ResistantVirus(1.0, 0.0, {}, 0.0)
# patient = TreatedPatient([virus], 100)
# Updating patient for 100 time steps
# Test completed.
# Test: TreatedPatient 2
# Create a TreatedPatient with virus that is always cleared and always reproduces.

# Output:
# virus = ResistantVirus(1.0, 1.0, {}, 0.0)
# patient = TreatedPatient([virus], 100)
# Updating patient for 100 time steps
# Test completed.
# Test: TreatedPatient 3
# Test for adding duplicate prescriptions in TreatedPatient

# Output:
# Test completed.
# Test: TreatedPatient 4
# Test addPrescription and getPrescription in TreatedPatient.

# Output:
# patient = TreatedPatient([], 100)
# Adding prescription Drug P
# Drug P in plist: True
# Adding prescription Drug W
# Drug W in plist: True
# Adding prescription Drug R
# Drug R in plist: True
# Adding prescription Drug G
# Drug G in plist: True
# Adding prescription Drug I
# Drug I in plist: True
# Adding prescription Drug D
# Drug D in plist: True
# Adding prescription Drug A
# Drug A in plist: True
# Adding prescription Drug Z
# Drug Z in plist: True
# Adding prescription Drug O
# Drug O in plist: True
# Adding prescription Drug J
# Drug J in plist: True
# Adding prescription Drug P
# Drug P in plist: True
# len(patient.getPrescriptions()): 10
# Adding prescription Drug W
# Drug W in plist: True
# len(patient.getPrescriptions()): 10
# Adding prescription Drug R
# Drug R in plist: True
# len(patient.getPrescriptions()): 10
# Adding prescription Drug G
# Drug G in plist: True
# len(patient.getPrescriptions()): 10
# Adding prescription Drug I
# Drug I in plist: True
# len(patient.getPrescriptions()): 10
# Test completed.
# Test: TreatedPatient 5
# Test of getting TreatedPatient's resistant pop

# Output:
# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
# virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
# patient = sm.TreatedPatient([virus1, virus2, virus3], 100)
# patient.getResistPop(['drug1']): 2
# patient.getResistPop(['drug2']): 2
# patient.getResistPop(['drug1','drug2']): 1
# patient.getResistPop(['drug3']): 0
# patient.getResistPop(['drug1', 'drug3']): 0
# patient.getResistPop(['drug1','drug2', 'drug3']): 0
# Test completed.
# Test: TreatedPatient 6
# Test for virus populations in TreatedPatient.

# Output:
# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
# patient = TreatedPatient([virus1, virus2], 1000000)
# patient.addPrescription("drug1")
# Updating patient 5 times
# Expect resistant population to be 2^5 +/- 10
# Expect total population to be the resistant population plus 1
# Test completed.

# Part B: Problem 5: Running and Analyzing a Simulation With a Drug

# In this problem, we will use the implementation you filled in for Problem 4 to run a simulation. 
# You will create a TreatedPatient instance with the following parameters, then run the simulation:
    # viruses, a list of 100 ResistantVirus instances
    # maxPop, maximum sustainable virus population = 1000
# Each ResistantVirus instance in the viruses list should be initialized with the following parameters:
    # maxBirthProb, maximum reproduction probability for a virus particle = 0.1
    # clearProb, maximum clearance probability for a virus particle = 0.05
    # resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
    # mutProb, probability of a mutation in a virus particle's offspring = 0.005
# 
# Run a simulation that consists of 150 time steps, followed by the addition of the drug, guttagonol, followed by another 150 time steps. 
# You should make use of the function simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials). 
# As with problem 3, perform up to 100 trials and make sure that your results are repeatable and representative.
# 
# Create one plot that records both the average total virus population and the average population of guttagonol-resistant virus particles over time.
# A few good questions to consider as you look at your plots are: What trends do you observe? Are the trends consistent with your intuition? 
# Feel free to discuss the answers to these questions in the forum, to fully cement your understanding of this problem set, processing and interpreting data.
#
# Again, as in Problem 2, you can use the provided .pyc file to check that your implementation of the TreatedPatient and ResistantVirus classes work as expected.

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    time_steps = 150
    total_time_steps = 2 * time_steps
    virus_population = [0] * total_time_steps # initialize the virus population list
    resist_population = [0] * total_time_steps # initialize the resistant population list
    for trial in range(numTrials): # run the simulation for numTrials trials
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for _ in range(numViruses)] # create a list of ResistantVirus instances
        patient = TreatedPatient(viruses, maxPop) 
        for i in range(time_steps):
            virus_population[i] += patient.update()
            resist_population[i] += patient.getResistPop(['guttagonol'])
        patient.addPrescription('guttagonol')
        for i in range(time_steps, 2 * time_steps):
            virus_population[i] += patient.update()
            resist_population[i] += patient.getResistPop(['guttagonol'])
    avg_virus_population = [x / numTrials for x in virus_population] # average the virus population
    avg_resist_population = [x / numTrials for x in resist_population] # average the resistant population
    pylab.plot(avg_virus_population, label = "Total Virus Population")
    pylab.plot(avg_resist_population, label = "Resistant Virus Population")
    pylab.title("ResistantVirus simulation with drug")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

# Testing the simulationWithDrug function
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)

# GRADING TESTS:
# Test: simulation 1
# Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module.
# For grading, please plot the total viruses first, then plot the resistant viruses second, in two separate calls to 'pylab.plot.'
# Be sure you call pylab.show() last. The order of other lines do not matter.

# Output:
# Test: simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
# Plotting...
# Plotting values: [2.0, 4.0, 6.4, 7.6, 9.2, 9.6, 9.8, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
# Plotting...
# Plotting values: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# Successfully called pylab.title with label: ResistantVirus simulation with drug
# Successfully called pylab.xlabel with label: Time Steps
# Successfully called pylab.ylabel with label: Average Virus Population
# Successfully called pylab.legend
# Successfully called pylab.show
# Test: simulation 2
# Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module.
# For grading, please plot the total viruses first, then plot the resistant viruses second, in two separate calls to 'pylab.plot.'
# Be sure you call pylab.show() last. The order of other lines do not matter.

# Output:
# Test: simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
# Plotting...
# Plotting values: [1.8, 3.4, 6.2, 10.8, 14.8, 19.4, 20.2, 21.2, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4, 21.4]
# Plotting...
# Plotting values: [1.0, 1.8, 3.2, 5.2, 7.6, 9.4, 9.8, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2]
# Successfully called pylab.title with label: ResistantVirus simulation with drug
# Successfully called pylab.xlabel with label: Time Steps
# Successfully called pylab.ylabel with label: Average Virus Population
# Successfully called pylab.legend
# Successfully called pylab.show
# Test: simulation 3
# Note: your simulation should only be using the plot, title, xlabel, ylabel, legend, figure, and show functions from the Pylab module.
# For grading, please plot the total viruses first, then plot the resistant viruses second, in two separate calls to 'pylab.plot.'
# Be sure you call pylab.show() last. The order of other lines do not matter.

# Output:
# Test: simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
# Plotting...
# Plotting values: [88.0, 90.0, 93.0, 95.0, 98.0, 95.0, 97.0, 95.0, 95.0, 94.0, 98.0, 97.0, 92.0, 94.0, 96.0, 91.0, 91.0, 94.0, 99.0, 101.0, 96.0, 97.0, 97.0, 94.0, 97.0, 94.0, 98.0, 94.0, 99.0, 94.0, 89.0, 93.0, 96.0, 96.0, 94.0, 92.0, 101.0, 95.0, 89.0, 97.0, 99.0, 93.0, 96.0, 96.0, 94.0, 97.0, 92.0, 97.0, 99.0, 99.0, 92.0, 91.0, 93.0, 94.0, 93.0, 94.0, 94.0, 101.0, 99.0, 97.0, 99.0, 93.0, 92.0, 93.0, 98.0, 97.0, 101.0, 93.0, 98.0, 95.0, 88.0, 95.0, 92.0, 88.0, 95.0, 95.0, 97.0, 97.0, 95.0, 98.0, 95.0, 95.0, 102.0, 93.0, 94.0, 93.0, 91.0, 98.0, 94.0, 96.0, 95.0, 100.0, 104.0, 94.0, 97.0, 95.0, 100.0, 95.0, 95.0, 96.0, 95.0, 89.0, 90.0, 101.0, 101.0, 96.0, 99.0, 96.0, 95.0, 93.0, 90.0, 91.0, 95.0, 96.0, 101.0, 97.0, 96.0, 93.0, 91.0, 91.0, 92.0, 95.0, 94.0, 90.0, 91.0, 91.0, 85.0, 88.0, 94.0, 97.0, 98.0, 91.0, 96.0, 96.0, 99.0, 90.0, 93.0, 89.0, 87.0, 98.0, 94.0, 96.0, 99.0, 102.0, 97.0, 96.0, 96.0, 94.0, 93.0, 91.0, 91.0, 83.0, 86.0, 88.0, 88.0, 86.0, 82.0, 77.0, 81.0, 82.0, 83.0, 75.0, 71.0, 69.0, 66.0, 60.0, 60.0, 61.0, 55.0, 53.0, 47.0, 50.0, 52.0, 47.0, 51.0, 50.0, 54.0, 54.0, 57.0, 55.0, 54.0, 56.0, 57.0, 52.0, 45.0, 43.0, 43.0, 42.0, 39.0, 40.0, 41.0, 46.0, 45.0, 46.0, 45.0, 46.0, 45.0, 44.0, 43.0, 41.0, 36.0, 36.0, 42.0, 41.0, 38.0, 39.0, 40.0, 39.0, 41.0, 44.0, 49.0, 51.0, 50.0, 49.0, 50.0, 49.0, 47.0, 43.0, 42.0, 42.0, 40.0, 37.0, 42.0, 41.0, 40.0, 38.0, 39.0, 37.0, 38.0, 39.0, 34.0, 36.0, 35.0, 33.0, 31.0, 31.0, 29.0, 30.0, 27.0, 29.0, 27.0, 29.0, 31.0, 32.0, 33.0, 36.0, 34.0, 38.0, 37.0, 40.0, 40.0, 42.0, 44.0, 45.0, 47.0, 43.0, 45.0, 39.0, 35.0, 34.0, 38.0, 38.0, 41.0, 38.0, 38.0, 36.0, 40.0, 43.0, 46.0, 44.0, 45.0, 44.0, 46.0, 45.0, 51.0, 53.0, 51.0, 54.0, 53.0, 53.0, 52.0, 49.0, 45.0, 44.0, 47.0, 42.0, 42.0, 39.0, 36.0, 33.0, 32.0, 32.0, 34.0, 31.0, 23.0, 22.0, 21.0, 20.0, 22.0, 22.0]
# Plotting...
# Plotting values: [74.0, 69.0, 64.0, 60.0, 58.0, 56.0, 55.0, 50.0, 51.0, 50.0, 47.0, 46.0, 40.0, 45.0, 48.0, 49.0, 50.0, 51.0, 52.0, 56.0, 53.0, 54.0, 56.0, 52.0, 53.0, 53.0, 56.0, 51.0, 57.0, 51.0, 48.0, 49.0, 48.0, 52.0, 50.0, 48.0, 54.0, 52.0, 48.0, 51.0, 50.0, 48.0, 50.0, 47.0, 48.0, 53.0, 51.0, 49.0, 52.0, 52.0, 48.0, 49.0, 52.0, 54.0, 54.0, 50.0, 48.0, 51.0, 50.0, 46.0, 50.0, 48.0, 46.0, 45.0, 41.0, 39.0, 43.0, 39.0, 40.0, 41.0, 41.0, 45.0, 46.0, 42.0, 47.0, 48.0, 52.0, 48.0, 47.0, 53.0, 51.0, 49.0, 52.0, 48.0, 47.0, 46.0, 49.0, 52.0, 50.0, 49.0, 48.0, 51.0, 57.0, 52.0, 52.0, 53.0, 55.0, 52.0, 53.0, 54.0, 53.0, 52.0, 54.0, 55.0, 53.0, 51.0, 52.0, 50.0, 49.0, 47.0, 44.0, 47.0, 45.0, 46.0, 47.0, 44.0, 46.0, 45.0, 42.0, 43.0, 47.0, 47.0, 46.0, 44.0, 43.0, 43.0, 39.0, 44.0, 47.0, 49.0, 47.0, 42.0, 47.0, 49.0, 48.0, 44.0, 45.0, 44.0, 42.0, 49.0, 46.0, 47.0, 55.0, 55.0, 53.0, 55.0, 53.0, 51.0, 53.0, 51.0, 48.0, 44.0, 43.0, 43.0, 42.0, 39.0, 35.0, 30.0, 30.0, 29.0, 27.0, 26.0, 24.0, 20.0, 20.0, 17.0, 15.0, 14.0, 12.0, 11.0, 13.0, 13.0, 13.0, 11.0, 11.0, 11.0, 10.0, 10.0, 10.0, 10.0, 9.0, 11.0, 11.0, 9.0, 7.0, 7.0, 8.0, 8.0, 7.0, 8.0, 9.0, 10.0, 12.0, 11.0, 10.0, 10.0, 9.0, 8.0, 8.0, 7.0, 9.0, 11.0, 11.0, 11.0, 8.0, 9.0, 10.0, 9.0, 12.0, 13.0, 14.0, 18.0, 15.0, 14.0, 12.0, 11.0, 10.0, 10.0, 10.0, 10.0, 10.0, 8.0, 8.0, 6.0, 6.0, 5.0, 5.0, 4.0, 6.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 4.0, 5.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 10.0, 12.0, 11.0, 10.0, 9.0, 9.0, 8.0, 8.0, 8.0, 6.0, 6.0, 5.0, 5.0, 6.0, 7.0, 8.0, 9.0, 7.0, 8.0, 8.0, 10.0, 10.0, 11.0, 12.0, 13.0, 11.0, 13.0, 13.0, 16.0, 16.0, 14.0, 14.0, 12.0, 12.0, 10.0, 7.0, 7.0, 7.0, 7.0, 6.0, 7.0, 6.0, 5.0, 6.0, 5.0, 7.0, 8.0, 5.0, 3.0, 2.0, 3.0, 4.0, 3.0, 5.0]
# Successfully called pylab.title with label: ResistantVirus simulation with drug
# Successfully called pylab.xlabel with label: Time Steps
# Successfully called pylab.ylabel with label: Average Virus Population
# Successfully called pylab.legend
# Successfully called pylab.show