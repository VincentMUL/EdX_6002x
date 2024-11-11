# Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
# The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
# and explores as far as possible along each branch before backtracking.
# Similar to left fisrt depth first method of enumerating search tree
# Difference: Graphs can have cycles, so we must keep track of nodes we have visited to avoid infinite loops

from Lec3_GraphPr_Seg1_2 import Graph, Digraph, Node, Edge, buildCityGraph

# def DFS(graph, start, end, path, shortest):
#     path = path + [start] #add node to end of path
#     if start == end: #base case; if start is the same as end, then we have found a path (the target node has been found)
#         return path
#     for node in graph.childrenOf(start): #recursive case; for each node connected to start
#         if node not in path: #avoid cycles by checking if node is already in path
#             if shortest == None or len(path) < len(shortest): #if shortest is None or the length of path is less than the length of shortest
#                 newPath = DFS(graph, node, end, path, shortest) #recursive call; newPath is the path from node to end
#                 if newPath != None:#if newPath is not None, then we have found a path
#                     shortest = newPath
#     return shortest #if no path was found in the for loop, return None (no path exists)

# def shortestPath(graph, start, end): #wrapper function, gets recusive function started and provides abstraction
#     return DFS(graph, start, end, [], None) # path to empty and shortest to None
# # Client code should only worry about the graph and the start and end nodes
# # The arguments path and shortest are artifacts of the algorithm.

# added some functionality below for visibility

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

def shortestPath(graph, start, end, toPrint = False): #wrapper function, gets recusive function started and provides abstraction
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint) # path to empty and shortest to None

def testSP(source, destination): #test the shortest path function with source and destination nodes
    g = buildCityGraph(Digraph) #create a directed graph
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True) #find the shortest path from node 0 to target node

    if sp != None: #if a path was found
        print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
    else: #if no path was found
        print('There is no path from', source, 'to', destination)

# testSP('Chicago', 'Boston') #test the shortest path function with source and destination nodes, based on imported buildCityGraph function
testSP('Boston', 'Phoenix') 

# Now the Breadth-first search (BFS) algorithm
# The BFS algorithm succeeds in exploring the shortest path to a target node first
# by systematically exploring all nodes at the present depth level 
# before moving on to nodes at the next depth level.
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

# BFS explores all paths with n hops before exploring paths with n+1 hops
# BFS first looks for the shortest path and once it is found, it returns it.
# This is ok, because the first path found is the shortest path. 
# There might be an equally short path, but it will not be shorter.
# BFS explores all nodes at the current depth level before moving on to nodes at the next depth level. 

#rewrite the shortestPath function to use BFS instead of DFS
def shortestPath(graph, start, end, toPrint = False): #wrapper function, gets recusive function started and provides abstraction
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint) # path to empty and shortest to None

# testSP('Chicago', 'Boston') #test the BFS function with source and destination nodes, based on imported buildCityGraph function
testSP('Boston', 'Phoenix') #test the shortest path function with source and destination nodes, based on imported buildCityGraph function

# MINIMIZING WEIGHTED EDGES INSTEAD OF NUMBER OF EDGES
# If wanting to minimize the sum of the weights of the edges in the path, (not the number of edges)
# then the DFS algorithm can be easily modified to do this, but BFS cannot (obviously).
# BFS is enumerating the paths in length order.
# The shortest weighted path may have more then the minimum number of hops.
# Key to BFS is it explores most desirable first and looking at number of hops wouldn't be.
# For DFS enumerated number of hops, but easily modified to enumerate sum of weights.

# RECAP:
# Graphs are crucial to modelling; they capture relationships among objects
# Many important problems can be posed as graph optimization problems we can already solve
# DFS and BFS are fundamental algorithms for exploring graphs; can be used to solve many problems

# Next will be modelling situations with unpredictable events


#copilot suggested this function, not sure if useful yet:
# def testSP():
#     nodes = []
#     for name in range(6): #create 6 nodes
#         nodes.append(Node(str(name))) #add the nodes to the list
#     g = Digraph() #create a directed graph
#     for n in nodes: #add the nodes to the graph
#         g.addNode(n)
#     g.addEdge(Edge(nodes[0], nodes[1])) #add the edges to the graph
#     g.addEdge(Edge(nodes[1], nodes[2]))
#     g.addEdge(Edge(nodes[2], nodes[3]))
#     g.addEdge(Edge(nodes[2], nodes[4]))
#     g.addEdge(Edge(nodes[3], nodes[4]))
#     g.addEdge(Edge(nodes[3], nodes[5]))
#     g.addEdge(Edge(nodes[0], nodes[2]))
#     g.addEdge(Edge(nodes[1], nodes[0]))
#     g.addEdge(Edge(nodes[3], nodes[1]))
#     g.addEdge(Edge(nodes[4], nodes[0]))
#     sp = shortestPath(g, nodes[0], nodes[5], toPrint = True) #find the shortest path from node 0 to node 5
#     print('Shortest path found by DFS:', printPath(sp)) #print the shortest path found by DFS