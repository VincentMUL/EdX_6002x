# Programs to help understand the world and solve practical problems.

# Easy about the knapsack problem is the lack of relationship between the items.

# Graph theory: Graph representation using adjacency list
# Nodes (vertices), which might have properties
# Edges (arcs) are links between nodes, each edge consisting of pair of nodes
# Directed(digraph) or undirected(graph)
# Digraph has a source(parent) and a destination(child)
# Undirected graphs are symmetric
# Weighted or unweighted edges (for either digraph or undirected graph)
# Weighted edges have a number associated with each edge, could be capacity, distance, cost, etc.

# Wy Graphs?
# Graphs can capture relationships between things (friends, cities, family etc.)
# Tree is a special kind of graph, where there is only one path between any two nodes (eg family tree, search tree, etc.)

# Example of Getting John to the office:
# Model road system using digraph: nodes are intersections, edges are roads
# Each edge has a length or weight (time to traverse)
# Weights are dynamically computed
# Shortest path from John's house to office is the path with the smallest sum of weights -> classic graph optimization problem

# Leonard Euler 's Seven Bridges of Konigsberg:
# Konigsberg had 7 bridges connecting 4 land masses
# Euler asked if it was possible to walk across all 7 bridges once and only once
# Euler proved it was impossible, and in the process invented graph theory
    # Each island a node, each bridge an undirected edge
    # model abstracts away irrelevant details
# Is there a path that crosses each edge exactly once? -> Eulerian path
# For this each node except start and end must have an even number of edges
# No node in this example has an even number of edges, so no Eulerian path exists
# IMPORTANCE: new way of thinking about a large class of problems

#---------------------------------------------------
# Exercise 1:
#---------------------------------------------------

# Some classes must occur at least one semester before certain other classes 
# (e.g., Calculus I must be taken before Calculus II), but not all classes have prerequisites.
# If we want to represent the catalog as a graph, which variables should be represented as edges and vertices?
# -> Each vertex is a class, while a directional edge indicates that one class must come before another.

# Second graders are lining up to go to their next class, 
# but must be ordered alphabetically before they can leave. 
# The teacher only swaps the positions of two students that are next to each other in line.
# If we want to represent this situation as a graph, which variables should be represented as edges and vertices?
# -> Vertices represent permutations of the students in line. 
#    Edges connect two permutations if one can be made into the other by swapping two adjacent students.

class Node(object): #for now only has property of its name, could have just been a string, but future proofing
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object): #this allows edges to have directions (useable in both digraphs and undirected graphs)
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
    
# With a dense graph (lots of edges relative to nodes), adjacency matrix is more efficient
# Rows are source nodes, columns are destination nodes
# Cells cell[s,d] is 1 if there is an edge from s to d, 0 otherwise
# Cells can be weights or even lists when multiple edges are allowed

# Adjacency list is more efficient for sparse graphs (few edges relative to nodes)
# For each node; a list of destination nodes.
# Alternative: For each node, store a list of edges that have that node as source

class Digraph(object): #adjacency list representation
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {} #dictionary of nodes and their children
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = [] 
    def addEdge(self, edge):#edge is a tuple of two nodes, gets added to the graph
        src = edge.getSource() #get the source node
        dest = edge.getDestination() #get the destination node
        if not (src in self.edges and dest in self.edges): #if either node is not in the graph
            raise ValueError('Node not in graph')
        self.edges[src].append(dest) #add the destination node to the list of children of the source node
    def childrenOf(self, node): #return the children of a node
        return self.edges[node]
    def hasNode(self, node): #check if a node is in the graph
        return node in self.edges
    def getNode(self, name):#get a node by its name
        for n in self.edges:#iterate over the nodes in the graph
            if n.getName() == name: #if the name of the node matches the name we are looking for
                return n #return the node
        raise NameError(name) #if the node is not in the graph, raise an error
    def __str__(self):#return a string representation of the graph
        result = ''
        for src in self.edges:#iterate over the nodes in the graph
            for dest in self.edges[src]:#iterate over the children of the node
                result = result + src.getName() + '->' + dest.getName() + '\n'#add the edge to the result
        return result[:-1] #omit final newline

    
# in real code there is often as much code for errors as for the actual code
# about the __str__ method: there are fancier alternatives, but this is the simplest

class Graph(Digraph): #a graph is a digraph where every edge from src to dest has a corresponding edge from dest to src
    def addEdge(self, edge): #add an edge to the graph in both directions
        Digraph.addEdge(self, edge) #add the edge to the graph
        rev = Edge(edge.getDestination(), edge.getSource()) #create the reverse edge
        Digraph.addEdge(self, rev) #add the reverse edge to the digraph
#this is a simple way to create an undirected graph from a directed graph
#Why is Graph a subclass of Digraph and not the other way around?
# -> Substitution rule: If client code works correctly using an instance of a superclass,
#   it should also work correctly when an instance of a subclass is substituted for the superclass instance.
#   Important behaviour of the supertype should be supported by each of its subtypes.
#   But not vice versa! Remember code that works for Student superclass, should work correctly on TransferStudent subclass.
#   There is no reason to expect that code working for TransferStudent will work for Student.

# Apply this to shortest path from n1 to n2
# Formally given graph, find shortest sequence of edges where
# source node of first edge is n1 and destination node of last edge is n2
# for any edges, e1 and e2, in the sequence, the destination node of e1 is the source node of e2
# Alternatively; Finding the shortest weighted path
# minimize the sum of the wieghts of the edges in the path
# SHORTEST PATH problems are everywhere: biology, internet, gps etc.

# Presence of cycles can complicate the shortest path problem (not a problem in search trees)
# So can end points with no edges leading to them

def buildCityGraph(graphType):#graphType allows us to pass in either Digraph or Graph (instead of leaving blank and using g=Digraph())
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence'))) #using function addEdge from Digraph on class Edge with getNode function from Digraph
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
    
# # print(buildCityGraph(Digraph))
# print(buildCityGraph(Graph)) #this is the same graph as above, but now it is undirected

#---------------------------------------------------
# Exercise 2:
#---------------------------------------------------
# # Students in line:
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

#Now add the appropriate edges to the graph
g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB")))
g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC")))
g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))
g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))
g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))
g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA")))



# # because the graph is undirected, we only need to add one edge for each pair of nodes!