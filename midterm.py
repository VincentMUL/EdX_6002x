import random

# # The following function is stochastic:
# def f(x):
#     # x is an integer
#     return int(x + random.choice([0.25, 0.5, 0.75]))
# #answer False int!

# In Python, we can use random.seed(100) at the beginning of a program to generate the same sequence of random numbers each time we run a program.
# Answer: True
# random.seed(100)
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))

# A brute force solution to the 0/1 knapsack problem will always produce an optimal solution.
# Answer: True, it will albeit inefficiently sometimes, but it will always produce an optimal solution.

# Consider an undirected graph with non-negative weights that has an edge between each pair of nodes. 
# The shortest distance between any two nodes is always the path that is the edge between the two nodes.
# Answer: False, it is the sum of the weights of the edges between the two nodes.

# Which of the following problems can be solved using dynamic programming? Check all that work.
# 1. Sum of elements - Given a list of integer elements, find the sum of all the elements.
# 2. Binary search - Given a list of elements, check if the element X is in the list.
# 3. Dice throws - Given n dice each with m faces, numbered from 1 to m, 
#    find the number of ways to get sum X. X is the summation of values on each face 
#    when all the dice are thrown.
# Answer: 3 and only 3
# Not 2, because binary search is a divide and conquer algorithm, not a dynamic programming algorithm. (cf mergesort)
# Not 1, because the sum of elements is a trivial problem that does not require dynamic programming;
# no overlapping subproblems exist because each subproblem is only computed once

# What is the exact probability of rolling at least two 6's when rolling a die three times?
# 1/6 * 1/6 * 5/6 = 5/216 (probability of rolling exactly two 6's) 
# There are 3 ways to do this, so 5/216 * 3 = 15/216
# 1/6 * 1/6 * 1/6 = 1/216 (probability of rolling three 6's)
# 15/216 + 1/216 = 16/216 = 4/54 = 2/27
# Answer: 2/27

# A greedy optimization algorithm:
# 1. is typically efficient in time.
# 2. always finds an answer faster than a brute force algorithm.
# 3. always returns the same answer as the brute force algorithm.
# 4. never returns the optimal solution to the problem.
# Answer: 1
# A greedy optimization algorithm is typically efficient in time, but it does not always find the optimal solution to a problem.

# Suppose you have a weighted directed graph and want to find a path 
# between nodes A and B with the smallest total weight. 
# Select the most accurate statement:
# 1. If some edges have negative weights, depth-first search finds a correct solution.
# 2. If all edges have weight 2, depth-first search guarantees that the first path found to be is the shortest path.
# 3. If some edges have negative weights, breadth-first search finds a correct solution.
# 4. If all edges have weight 2, breadth-first search guarantees that the first path found to be is the shortest path.
# Answer: 4 
# Breadth-first search guarantees that the first path found is the shortest path if all edges have the same weight (or are unweighted).

# Which of the following functions are deterministic?
def F():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    return mylist

# first = F()
# for i in range(10000000):
#     test = F()
#     if test != first:
#         print(False)
#         break

# def testDeterministic(func, numTests = 9999999):
#     first=func()
#     print(first)
#     for i in range(numTests):
#         test=func()
#         if test != first:
#             return False
#         else:
#             return True

# # print(testDeterministic(F))

def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            # print(mylist)
            return mylist

# print(testDeterministic(G))

# first = G()
# for i in range(1000000000):
#     test = G()
#     if test != first:
#         print(False)
#         break

# Answer: Both functions are deterministic because they both use random.seed(0) at the beginning of the part of the function that matters.

# Consider a list of positive (there is at least one positive) and negative numbers. 
# You are asked to find the maximum sum of a contiguous subsequence. For example,
# in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
# in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
# One algorithm goes through all possible subsequences and compares the sums 
# of each contiguous subsequence with the largest sum it has seen. 
# What is the time complexity of this algorithm in terms of the length of the list, N?
# Answer: O(N^2)? O(N^3)? O(2^N)? O(N)? O(N log N)?
# The time complexity of this algorithm is O(N^3) because it goes through all possible subsequences,
# which is O(2^N), and compares the sums of each contiguous subsequence with the largest sum it has seen,
# which is O(N^2). Therefore, the time complexity is O(N^3).


# Problem 3
# You are given a list of unique positive integers L sorted in descending order and a positive integer sum s. 
# The list has n elements. Consider writing a program that finds values for multipliers m(0),m(1),...,m(n-1) 
# such that the following equation holds: s = L[0]*m(0) + L[1]*m(1) + ... + L[n-1]*m(n-1)
# Assume a greedy approach to this problem. You calculate the integer multipliers m_0, m_1, ..., m_(n-1) by 
# finding the largest multiplier possible for the largest value in the list, then for the second largest, 
# and so on. Write a function that returns the sum of the multipliers using this greedy approach. 
# If the greedy approach does not yield a set of multipliers such that the equation above sums to s, return the string "no solution". 
# Write the function implementing this greedy algorithm with the specification below:

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sum = 0
    for i in L:
        if s >= i:
            sum += s // i
            s = s % i
    if s == 0:
        return sum
    else:
        return "no solution"
    
# # Example usage:
# L = [10, 6, 3]
# s = 24
# print(greedySum(L, s))

# #Testing
# Test: greedySum([], 10)
# Output:
# 'no solution'
# Test: greedySum([1], 20)
# Output:
# 20
# Test: greedySum([2], 5)
# Output:
# 'no solution'
# Test: greedySum([10, 5, 1], 11)
# Output:
# 2
# Test: greedySum([10, 8, 5, 2], 16)
# Output:
# 'no solution'
# Test: greedySum([101, 51, 11, 2, 1], 3000)
# Output:
# 36
# Test: greedySum([10, 7, 6, 3], 19)
# Output:
# 'no solution'

# Problem 4
# You are given the following code. It has functions to create a random graph and to find a path between two nodes. 
# The graph is represented by a dictionary; integer keys represent all the nodes in the graph; 
# each key has a list of integers representing the nodes that the key has a directed edge to. 
# Assume the code in the provided functions meets the specifications given.
import random
  
# You are given this function - do not modify
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0,1,2,3,4,5,6,7,8,9], 7)
    for i in n:
        g[i] = []
    edges = random.randint(10,20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count += 1
    return g

# You are given this function - do not modify
def findPath(g, start, end, path=[]):
    """ Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes """
    path = path + [start]
    if start == end:
        return path
    if not start in g:
        return None
    for node in g[start]:
        if node not in path:
            newpath = findPath(g, node, end, path)
            if newpath: return newpath
    return None
                
#########################        
## WRITE THIS FUNCTION ##
#########################        

def allReachable(g, n):
    """
    Assumes g is a directed graph and n a node in g.
    Returns a sorted list (increasing by node number) containing all 
    nodes m such that there is a path from n to m in g. 
    Does not include the node itself.
    """
    reachable = []
    for node in g:
        if node != n:
            if findPath(g, n, node) != None:
                reachable.append(node)
    return sorted(reachable)

# You are not allowed to import anything. Do not leave any debugging print stataments. 
# Click "See full output" to see the test cases passed/failed. 
# Paste only the allReachable function and any helper functions you made for yourself (if any).

# g = {
#     0: [1, 2],
#     1: [3],
#     2: [4],
#     3: [5],
#     4: [3],
#     5: []
# }

# print(allReachable(g, 0))  # Expected output: [1, 2, 3, 4, 5]
# print(allReachable(g, 3))  # Expected output: [5]
# print(allReachable(g, 5))  # Expected output: []

# Tests
# Test: 10
#         g = {0: [2], 1: [8, 3], 2: [4, 3, 8], 3: [4, 2, 0], 4: [8, 0], 5: [4, 1, 3], 8: [2, 0, 5, 3, 1]}
#         n = 8
# Output:
# [0, 1, 2, 3, 4, 5]

# Test: 9
#         g = {1: [7], 2: [5], 4: [], 5: [1, 2, 4], 6: [4], 7: [4, 6, 1, 9], 9: [2, 6]}
#         n = 5
# Output:
# [1, 2, 4, 6, 7, 9]

# Problem 5
# In lecture, we explored the concept of a random walk, using a set of different models of drunks. 
# Below is the code we used for locations and fields and the base class of drunks – 
# you should not have to study this code in detail, since you have seen it in lecture.
import pylab

class Location(object):
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
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


import random, math

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

# !!!!!! New code !!!!!!!
# The following function is new, and returns the actual x and y distance 
# from the start point to the end point of a random walk.

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())

# Drunk variations
# Here are several different variations on a drunk:

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)

# #Trying to decipher EDrunk, but failed.
# for i in range(10):
#     a = math.sin(2 * math.pi * random.random())
#     b = math.cos(2 * math.pi * random.random())
#     c = 0.5 + 0.5 * random.random()
#     print("length is ", c)
#     print("return is x = ", a*c, "y = ", b*c)


# The problem:
# Suppose we use a simulation to simulate a random walk of a class of drunk, 
# returning a collection of actual distances from the origin for a set of trials.

# Each graph below was generated by using one of the above five classes of a drunk 
# (UsualDrunk, ColdDrunk, EDrunk, PhotoDrunk, or DDrunk). For each graph, 
# indicate which Drunk class is mostly likely to have resulted in that distribution of distances. 
# Click on each image to see a larger view.

# Answer: I'm afraid I've twisted UsualDrunk and EDrunk, I think they're very similar.

#Problem 6

# # Graphs are a convenient way to represent the relations between people, objects, concepts, and more.

# # There are many ways to create a graph, some of which are random. 
# # A random graph is one that is generated by randomly adding edges to a list of nodes. 
# # The list of nodes for this problem is initialized as follows:

# # nodes = []
# for i in range(n):
#     nodes.append(newNode(i)) # newNode takes one parameter, the number of the node

# # A helper method, addEdge, is referenced in this problem. 
# # The addEdge method takes two integers - representing nodes in the graph - 
# # and adds a directed edge from the first node to the second node. 
# # So, addEdge(8, 2) adds a directed edge from Node 8 to Node 2.

# # In each code piece below, a graph is generated using the above node 
# # set by adding edges in some fashion. Your job is to examine the code 
# # and select the type of graph that will be generated.
# #  Your choices for each question will be: 
# # tree; graph (undirected graph); line graph; digraph (directed graph); 
# # complete graph or clique; bar graph; bipartite graph; loop or connected chain of nodes. 
# # Note that this last option refers to a graph that consists of one single, 
# # large loop or connected chain of nodes.

# for i in range(len(nodes)):
# 	x = random.choice(nodes)
# 	y = random.choice(nodes)
# 	addEdge(x,y)