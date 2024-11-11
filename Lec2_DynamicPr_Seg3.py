# How will Dynamic Programming work for the 0 - 1 Knapsack Problem?
# Check if there is an optimal substructure: can local subproblems be combined to solve the global problem
# Check if there are overlapping subproblems: is the same subproblem solved multiple times

# We clearly have optimal substructure: each parent node can be solved by combining the solutions of its children
# eg the right answer for the root node is the better of the two children

# We also have overlapping subproblems: the same subproblem is solved multiple times
# in the simple example with the burger, pizza and beer no two nodes have the same contents for the same items available
# in the case of 2 beers, 1 pizza, 1 burger, the left child of the root node and the right child of the left child node have the same contents (a beer)
# You don't need copies of the same items for dynamic programming to still work (or overlapping subproblems to be found)
# This is especially true when you realize that for all the considered nodes, the value does not matter, only the weight matters.
# And which items are left to consider. In that case having the same items left to consider and the same weight left to fill, 
# the same subproblem is solved multiple times.

# def fastMaxVal(toConsider, avail, memo = {}): #memo key is a tuple of the items left to consider and the weight left to fill;
#     # the items left toConsider will be represented by len(toConsider); this works because items are always removed from the front of the list.
#     # first it'll check if the optimal solution is already in the memo dictionary
#     # last thing it does is update the memo

from Lec2_DynamicPr_Seg1 import *
import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items

def maxVal(toConsider, avail): #recursively calling toConsider and avail; which will change with each recursive call
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0: #base case; toConsider are items that nodes higher up in the tree have not yet considered and avail is the amount of space left in the knapsack
        result = (0, ())
    elif toConsider[0].getCost() > avail: #next item doesn't fit
        #Explore right branch only
        result = maxVal(toConsider[1:], avail) #recursive call for sliced toConsider, but avail unchanged
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost()) #recursive call for sliced toConsider and avail minus the cost of the next item
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
#Note: No search tree is explicitly constructed, but the recursion implicitly builds the tree and
#      the local variable result is used to keep track of the best solution found so far

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print(' ', item)

def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
        memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the
        0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:#check if the optimal solution is already in the memo dictionary
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:#base case
        result = (0, ())
    elif toConsider[0].getCost() > avail:#next item doesn't fit
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result #update the memo
    return result

def testFastMaxVal(foods, maxUnits, algorithm, printItems = True): #algorithm is either maxVal or fastMaxVal
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('  ', item)

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    # testFastMaxVal(items, 750, maxVal, False) #This will run a long time
    testFastMaxVal(items, 750, fastMaxVal, False) #Dynamic programming is a big win

# import sys
# sys.getrecursionlimit() #default is 1000
# sys.setrecursionlimit(2000) #set the recursion limit to 2000

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 1024):#1024 will exceed the recursion limit and give error
    items = buildLargeMenu(numItems, 90, 250)
    testFastMaxVal(items, 750, fastMaxVal, False) #Dynamic programming is a big win
#Dynamic programming is a big win, but it's not a panacea
# Error message: RecursionError: maximum recursion depth exceeded in comparison
# Every time a recursive call is made, a new frame is added to the call stack
# The runtime system places a limit on the depth of the call stack
# This limit is the maximum recursion depth, visualize using sys.getrecursionlimit()

#Change code to keep track of number of calls
def countingFastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    global numCalls
    numCalls += 1
    
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = countingFastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 countingFastMaxVal(toConsider[1:],
                            avail - nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = countingFastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

# Number of calls is enormously less than exponential.
# The problem is inherently exponential, but dynamic programming has reduced the number of calls to a manageable number
# Running time of fastMaxVal is governed by the number of distinct subproblems (number of distinct pairs <toConsider, avail>)
    # Number of possible values for toConsider is bounded by len(items); number of items
    # Number of possible values for avail is harder to characterize; bounded by the number of distinct sums of weights:
    # How many different ways are their to combine the weights of the available items to get a different answer.
# This is a pseudo-polynomial time algorithm; most of the time polynomial, but in some cases exponential (when no overlapping subproblems)

# SUMMARY Lec1 and Lec2:
# Many problems of practical importance can be formulated as optimization problems.
# Ask yourself if you can define a value function that you want to maximize or minimize, subject to set of constraints (possibly empty). 

# Greedy algorithms often provide adequate solutions, but not always optimal solutions, because local vs global.
# The global optimal solution is usually exponentially hard.

# But Dynamic programming often yields good performance for a subclass of optimization problems:
# Problems with optimal substructure AND overlapping subproblems:
# Solution always correct, but only fast under the right circumstances.
# Dynamic programming is a general algorithm design paradigm that can be used to solve optimization problems.

# Exercise 2: True or False

# 1. Dynamic programming can be used to solve optimization problems where the size of the space of possible solutions is exponentially large.
# True

# 2. Dynamic programming can be used to find an approximate solution to an optimization problem, but cannot be used to find a solution that is guaranteed to be optimal.
# False

# 3. Recall that sorting a list of integers can take O(nlogn) using an algorithm like merge sort. 
#    Dynamic programming can be used to reduce the order of algorithmic complexity of sorting a list of integers to something below n log n, 
#    where n is the length of the list to be sorted.
# False

# Problem: I need to go up a flight of N stairs. I can either go up 1 or 2 steps every time. 
# How many different ways are there for me to traverse these steps? For example:
# 3 steps -> could be 1,1,1 or 1,2 or 2,1
# 4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
# 5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2
# Does this problem have optimal substructure and overlapping subproblems?

# Solution:
# You need to find how many different ways you can go up a flight of stairs with N steps, where at each step, you have two choices:
# Either take 1 step or
# Take 2 steps.
# We need to find the total number of ways to get to the top of the staircase using combinations of 1-step and 2-steps.
# 
# Optimal Substructure:
# To find how many ways you can reach the nth step:
# If your last step was 1 step (then you must have been at step n-1).
# If your last step was 2 steps (then you must have been at step n-2).
# This gives us a recursive relation. The number of ways to reach the nth step is the sum of:
    # The number of ways to reach step n-1 (because from there, you could take a 1-step) and
    # The number of ways to reach step n-2 (because from there, you could take a 2-step).
    # T(n) = T(n-1) + T(n-2)
# Base cases: T(0) = 1 (there is one way to climb 0 steps: do nothing) and T(1) = 1 (there is one way to climb 1 step: take one 1-step).

# Overlapping Subproblems:
# A problem has overlapping subproblems if the same subproblems are solved multiple times during the computation.
# To compute T(4), you need T(3) and T(2) and to compute T(3), you need T(2) and T(1). You need T(2) twice.
