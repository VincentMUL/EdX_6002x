from graphviz import Digraph
from Lec3_GraphPr_Seg1_2 import Node, Edge


def generate_permutations(nums, current=[], result=[]):
    if not nums: #if there are no items left, return nothing
        result.append(current.copy())
        return

    for i in range(len(nums)):#for each item in the list
        num = nums[i] #get the item
        current.append(num) #add the item to the current list
        remaining_nums = nums[:i] + nums[i+1:] #get the remaining items
        generate_permutations(remaining_nums, current, result) #recursive call
        current.pop() #remove the last item from the current list

# # Example usage:
# nums = [1, 2, 3]
# permutations = []
# generate_permutations(nums, result=permutations)
# # print(permutations) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

inputList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# #example use of generate_permutations
# n = 4
# pupils = inputList[:n]
# permutations = []
# generate_permutations(pupils, result=permutations)
# nodes = []
# for i in range(len(permutations)):
#     stringlist= ''.join(map(str, permutations[i]))
#     nodes.append(Node(stringlist)) # nodes[i]
#     print(str(stringlist))

# Define the buildCityGraph function using graphviz
def buildGraph():
    g = Digraph()  # Create a directed graph from graphviz
    n = 3
    pupils = inputList[:n]
    permutations = []
    generate_permutations(pupils, result=permutations)
    nodes = []
    node_names = []
    for i in range(len(permutations)):
        stringlist= ''.join(map(str, permutations[i]))
        nodes.append(Node(stringlist)) # nodes[i]
        node_names.append(str(stringlist))
    for pupil in nodes:
        g.node(pupil.getName())  # Add nodes using graphviz node function

    # Add edges using graphviz's edge method
    for node_name in node_names:
        for i in range(len(node_name) - 1):
            # Swap with the next character
            swapped = list(node_name)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            swapped_name = ''.join(swapped)
            if swapped_name in node_names:
                g.edge(node_name, swapped_name)

    return g

# Build the graph
graph = buildGraph()

# Render the graph
graph.render('pupil_graph', format='png', view=True)