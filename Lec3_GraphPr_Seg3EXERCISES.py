# After DFS and BFS

#---------------------------------------------------
# EXERCISE 3:
#---------------------------------------------------

# For questions 1 and 2, consider our previous problem (permutations of 3 students in a line).

# When represented as a tree, each node will have how many children?
#2
#Given two permutations, 
#what is the maximum number of swaps it will take to reach one from the other?
#3

# For questions 3 and 4, consider the general case of our previous problem 
# (permutations of n students in a line). 
# Give your answer in terms of n.
# When represented as a tree, each node will have how many children?
#n-1
# In any permutation, n students are lined up and there are exactly n-1 pairs we are able to swap.

#what is the maximum number of swaps it will take to reach one from the other?
# n(n-1)/2
# This is related the the maximum number of inversions in a permutation.
# The total number of pairs in n elements. Since all pairs are inverted in the reverse permutation.
# Therefore the maximum number of swaps or inversions is n(n-1)/2.
# Example: [4,3,2,1] has 6 inversions:(4,3),(4,2),(4,1) and (3,2),(3,1) and (2,1)
# Other way to think about it: move last person to front, then second to last person to second, etc.
# This is a sum: (n-1) + (n-2) + ... 2 + 1 = n(n-1)/2

#---------------------------------------------------
# EXERCISE 4:
#---------------------------------------------------

# Consider our continuing problem of permutations of three students in a line. 
# Use the enumeration we established when adding the nodes to our graph.
# nodes = []
# nodes.append(Node("ABC")) # nodes[0]
# nodes.append(Node("ACB")) # nodes[1]
# nodes.append(Node("BAC")) # nodes[2]
# nodes.append(Node("BCA")) # nodes[3]
# nodes.append(Node("CAB")) # nodes[4]
# nodes.append(Node("CBA")) # nodes[5]

from Lec3_GraphPr_Seg1_2 import Graph, Digraph, Node, Edge, buildCityGraph

def generate_permutations(nums, current=[], result=[]):
    """Generates all permutations of a list of items or numbers"""
    if not nums:
        result.append(current.copy())
        return

    for i in range(len(nums)):
        num = nums[i]
        current.append(num)
        remaining_nums = nums[:i] + nums[i+1:]
        generate_permutations(remaining_nums, current, result)
        current.pop()


def buildPupilsGraph(graphType):#graphType allows us to pass in either Digraph or Graph (instead of leaving blank and using g=Digraph())
    g = graphType()
    inputList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    n = 3
    pupils = inputList[:n]
    permutations = []
    generate_permutations(pupils, result=permutations)
    # nodes = []
    node_names = []
    for i in range(len(permutations)):
        stringlist= ''.join(map(str, permutations[i]))
        g.addNode(Node(stringlist))
        # nodes.append(Node(stringlist)) # nodes[i]
        # print("node ",str(i)," : ",str(stringlist))# to test node indexing
        node_names.append(str(stringlist))
    for node_name in node_names:
        for i in range(len(node_name) - 1):
            # Swap with the next character
            swapped = list(node_name)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            swapped_name = ''.join(swapped)
            if swapped_name in node_names:
                g.addEdge(Edge(g.getNode(node_name), g.getNode(swapped_name)))
    return g

# buildPupilsGraph(Digraph) #test the function

def printPath(path): #print the path
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)): #iterate over the nodes in the path
        result = result + str(path[i]) #add the node to the result
        if i != len(path) - 1: #if the node is not the last node in the path
            result = result + '->' #add an arrow to the result
    return result #return the result

def DFS(graph, start, end, path, shortest, toPrint = False): #added toPrint argument
    """Assumes graph is a Digraph; start and end are nodes; path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start] #add node to end of path
    if toPrint: #if toPrint is True
        print('Current DFS path:', printPath(path)) #print the current path
    if start == end: #base case; if start is the same as end, then we have found a path (the target node has been found)
        return path
    for node in graph.childrenOf(start): #recursive case; for each node connected to start
        if node not in path: #avoid cycles by checking if node is already in path
            if shortest == None or len(path) < len(shortest): #if shortest is None or the length of path is less than the length of shortest
                newPath = DFS(graph, node, end, path, shortest, toPrint) #recursive call; newPath is the path from node to end
                if newPath != None:#if newPath is not None, then we have found a path
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest #if no path was found in the for loop, return None (no path exists)

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start] #initialize the path with the start node
    pathQueue = [initPath] #used to store all paths currently being explored
    while len(pathQueue) != 0: #while the path queue is not empty
        if toPrint: #if toPrint is True
            print('Current BFS path:', printPath(pathQueue[0])) #print the current path
        tmpPath = pathQueue.pop(0) #get and remove the oldest element in pathQueue and assign to tmpPath;
        #this dequeues the oldest path in the pathQueue, ensuring paths are explored in the order added to the queue
        lastNode = tmpPath[-1] #get the last node in the path
        if lastNode == end: #if the last node is the target node; solution found
            return tmpPath #exit while-loop: only 1 solution is found and returned; this is OK because it finds the shortest path
        for nextNode in graph.childrenOf(lastNode): #for each node connected to the last node
            if nextNode not in tmpPath: #avoid cycles by checking if node is already in path
                newPath = tmpPath + [nextNode] #create a new path with one of its children
                pathQueue.append(newPath) #enqueue every new paths; add to pathQueue
    return None #if no path was found, return None

def shortestPath(graph, start, end, search, toPrint = False): #wrapper function, gets recusive function started and provides abstraction
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    if search == 'DFS':
        return DFS(graph, start, end, [], None, toPrint) # path to empty and shortest to None
    elif search == 'BFS':
        return BFS(graph, start, end, toPrint)
    else:
        print('Invalid search algorithm')
        return None

def testSP(source, destination, search): #test the shortest path function with source and destination nodes
    # g = buildCityGraph(Digraph) #create a directed graph for cities
    g = buildPupilsGraph(Digraph) #create a directed graph for pupils
    if search=='DFS' or search=='BFS':
        sp = shortestPath(g, g.getNode(source), g.getNode(destination),search, toPrint = True) #find the shortest path from node 0 to target node
        if sp != None: #if a path was found
            print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
        else: #if no path was found
            print('There is no path from', source, 'to', destination)
    else:
        print('Invalid search algorithm')
        return None

# #example use of generate_permutations
# testSP('Boston', 'Phoenix', 'DFS')
# testSP('Boston', 'Phoenix', 'BFS')
# testSP('ABC', 'CAB', 'DFS') # first path reaching destination ABC->BAC->BCA->CBA->CAB or ABC->ACB->CAB
# testSP('CAB', 'ACB', 'DFS') # first path reaching destination CAB->ACB
# testSP('ACB', 'ACB', 'DFS') # first path reaching destination ACB->ACB
# testSP('BAC', 'CAB', 'DFS') # first path reaching destination BAC->ABC->ACB->CAB
# testSP('BAC', 'BCA', 'DFS') # first path reaching destination BAC->ABC->ACB->CAB->CBA->BCA
# testSP('BCA', 'ACB', 'DFS') # first path reaching destination BCA->CBA->CAB->ACB or BCA->BAC->ABC->ACB

# !!!!!!!! HARD QUESTION !!!!!!!!
# We saw before that for permutations of 3 people in line, 
# any two nodes are at most three edges, or four nodes, away. 
# But DFS has yielded paths longer than three edges! 
# In this graph, given a random source and a random destination, 
# what is the probability of DFS finding a path of the shortest possible length?
# 2/3

#EXPLANATION:
# This graph is a circle of 6 nodes, see Vizualize code.
# Given any node, we know that DFS will prioritize the lower-numbered neighbor.
# If our destination is our source, we terminate the DFS, 
# and return a path of length zero, which is clearly the shortest.
# Otherwise, we continue in a circle in one direction and we cannot change direction.
# Because the path may not contain any node more than once.
# It will have found the shortest path for the nodes that are 0, 1, 2, or 3 edges away, 
# but will yield paths of length 4 and 5 for the last two nodes that are, 
# in reality, 2 and 1 edges away, respectively.
# As it has found the shortest path for 4 nodes, 
# but not for 2, the probability is 4 in 6, or 2/3.

#---------------------------------------------------
# EXERCISE 5: CHALLENGING
#---------------------------------------------------

# In the following examples, assume all graphs are undirected. 
# That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

#A clique is an unweighted graph where each node connects to all other nodes. 
#We denote the clique with n nodes as KN. Answer the following questions in terms of n.

# 1. How many edges are in KN?
# n(n-1)/2 eg 5 nodes = 4+3+2+1 = 10

# 2. Consider the new version of DFS. 
# This traverses paths until all non-circular paths from the source to the destination have been found, 
# and returns the shortest one.
# Let A be the source node, and B be the destination in KN. How many paths of length 2 exist from A to B?
# n-2 eg 5 nodes = A and B are static, so going through the other 3 = 3 paths

# 3. How many paths of length 3 exist from A to B?
# (n-2)*(n-3) eg 5 nodes = A and B are static, so going through '1' (C) of the other 3 twice (once for every one left),
# then going through ever other '1' (D and E) also twice = 6 paths
# also derives from (n-2)!/(n-4)! = (n-2)*(n-3) = 6

# 4. Continuing the logic used above, calculate the number of paths of length m from A to B, 
# where 1<=m<=(n-1) and write this number as a ratio of factorials.
# (n-2)!/(n-m-1)! eg 5 nodes = (5-2)!/(5-3)! = 6
# so this would become (n-2)*(n-3)*(n-4)*...*(n-m) 

# 5. Using the fact that for any n; 1/(0!) + 1/(1!) + 1/(2!) + ... + 1/(n!) <=e for all n,
# where e is some constant, determine the asymptotic bound on the number of paths explored by DFS. 
# For simplicity, write O(n) as just n, O(n²) as n^2, etc.
# Given that the number of paths of length m is (n-2)!/(n-m-1)!,
# the number of paths explored is the sum of this over all m from 1 to n-1.
# This is the sum of (n-2)!/(n-m-1)! from m=1 to n-1.
# We can consider this as limit ( n! * 1/(n!) ) + ( n! * 1/(n-1)! ) + ... + ( n! * 1/(2!) ) + ( n! * 1/(1!) ) = limit (n! * ( 1/n + 1/(n-1) + ... + 1/2 + 1/1 ) )= e * limit n! = e * n!
# This migh be the same as (n-2)! , but I am not sure


# ---------------------------------------------------
# EXERCISE 6
# ---------------------------------------------------

#In the following examples, assume all graphs are undirected. 
#That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.
# A clique is an unweighted graph where each node connects to all other nodes. 
# We denote the clique with n nodes as KN. Answer the following questions in terms of n.

# 1. What is the asymptotic worst-case runtime of a Breadth First Search on KN? 
# For simplicity, write O(n) as just n, O(n²) as n^2, etc.
# n
# BFS begins by checking all the paths of length 1. In its worst case, 
# it must check the paths to every node from the source to find the destination. This is at most, n-1 checks.

# 2. BFS will always run faster than DFS.
# False
# Consider a graph of two nodes, A and B, connected by an edge. 
# You wish to search for a path from A to B. 
# As there is exactly one edge in the graph, and exactly one path from A to B,
# both DFS and BFS run in an equal number of steps.

# 3. If a BFS and DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), 
# BFS will always run at least as fast as DFS when run on two nodes in KN.
# True 
# As seen in our previous problems in this lecture sequence, BFS checks at most n-1 paths in KN,
# and DFS always checks (n-2)! paths. If given the same node prioritization, both will first find the desired node in the same number of steps.


# 4. If a BFS and Shortest Path DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first),
# BFS will always run at least as fast as Shortest Path DFS when run on two nodes in any connected unweighted graph.
# True
# While Shortest Path DFS may find the desired node first in this case, 
# it still must explore all other paths before it has determined which path is the fastest. BFS will explore only a fraction of the paths.

# 5. Regardless of node priority, BFS will always run at least as fast as Shortest Path DFS on 
# two nodes in any connected unweighted graph.
# True
# Shortest Path DFS must always explore every path from the source to the destination to ensure that it has found the shortest path. 
# Once BFS has found a path, it knows that it is the shortest, and does not have to explore any other paths.

#---------------------------------------------------
# EXERCISE 7
#---------------------------------------------------

# Consider once again our permutations of students in a line. 
# Recall the nodes in the graph represent permutations, and that the edges represent swaps of adjacent students. 
# We want to design a weighted graph, weighting edges higher for moves that are harder to make. 
# Which of these could be easily implemented by simply assigning weights to the edges already in the graph?
# A. A large student who is difficult to move around in line.
# B. A sticky spot on the floor which is difficult to move onto or off of.
# C. A student who resists movement to the back of the line, but accepts movement toward the front.
# Answer: If we consider our graph to be with nodes that represent permutations of students in a line
# and edges that represent swaps of adjacent students, the answer is A and B.

# Write a WeightedEdge class that extends Edge. 
# Its constructor requires a weight parameter, as well as the parameters from Edge. 
# You should additionally include a getWeight method. 
# The string value of a WeightedEdge from node A to B with a weight of 3 should be "A->B (3)".

# Refresher:
# The __init__ method in Python is called a constructor. 
# It's a special method in a class that gets automatically called when a new instance (object) of the class is created. 
# Its main job is to initialize the object's attributes, meaning it sets up the initial state or properties of that specific instance.

class Edge(object): #this allows edges to have directions (useable in both digraphs and undirected graphs)
    def __init__(self, src, dest): #constructor (self represents the instance itself, allowing access to the instance's attributes and methods)
        """Assumes src and dest are nodes"""
        self.src = src #initialize the source of the edge
        self.dest = dest #initialize the destination of the edge
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):#Child class of Edge
    def __init__(self, src, dest, weight): #constructor
        Edge.__init__(self, src, dest)
        # super().__init__(src, dest) #alternative initialization
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.weight) + ')' #return the string representation of the edge