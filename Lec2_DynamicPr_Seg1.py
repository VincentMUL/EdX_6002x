# The Brute Force Algorithm
# 1. Enumerate all possible combinations of the input list
# 2. Remove all combinations that exceed the target sum
# 3. If any combinations remain, choose the one with largest value

# Search Tree Implementation of BFA ; also called Decision Tree 
# 1. Start at the root of the search tree
# 2. first element selected from still to be considered elements
# 3. While there is room in the knapsack:
#     a. If the element fits, add it to the knapsack = left child
#     b. If the element doesn't fit, don't add it to the knapsack = right child
# Apply this recursively to non-leaf children
# Use like a left-first depth-first search
# Note: Tree is upside down compared to a normal tree

# Computational complexity of the Search Tree
# Time is based on number of nodes generated (nodes in the tree)
# Number of levels is number of items to choose from; number of nodes at level i is 2^i 
# 1. Each element has two children
# 2. The tree has n levels
# 3. The number of leaves is 2^n
# -> The time complexity is O(2^n+1) - exponential!
# Obvious optimization: Prune the tree by not considering branches that exceed the target sum, but doesn't change the complexity


# Greedy algorithm example of menu
class Food(object): #begin with data abstraction and helper functions
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue() / self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
    
def buildMenu(names, values, calories): #build menu from data
    """names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction): #keyFunction provides ordering of items
    """Assumes items a list, maxCost >= 0,
       keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True) #sorts itemsCopy in descending order; from best to worse
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost: #check if there's room
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction) #matching result (list from greedy) and totalValue (float from greedy)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)

def testGreedys(foods, maxUnits): #test greedy algorithm
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue) #test greedy algorithm by value
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x)) #test greedy algorithm by cost
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750) #test greedy algorithm with 750 calories
# testGreedys(foods, 1000) #test greedy algorithm with 1000 calories

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


print('')
testMaxVal(foods, 750)
# It might need an extra restraint on the balance of drink vs food.
# Despite exponential time complexity, it's still a feasible solution for small problems: keep in mind 2^8 is not that big