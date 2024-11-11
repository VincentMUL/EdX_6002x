# Knapsack problem 0 - 1 
# Inherently exponential; NP-complete. Didn't prove it, but it is. (Can we prove it?)

# Approximate solutions are often good enough.
# Greedy algorithm is often a practical way to get a pretty good approximate solution.
# While knapsack is not full, put best available item in knapsack.
# But what does "best" mean?
# 1. Value density: value per unit weight
# 2. Value: value alone
# 3. Weight: weight alone

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

#flexible greedy algorithm
#keyFunction makes it flexible; can be value, cost, or value/cost -> independent of meaning of 'best'
#keyFunction is a function that maps elements of items to numbers
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
#remember sorted is a function that returns a new list, not modifying the original list (items) contrary to sort
# Check complexity of this algorithm: 
# O(nlogn) is lower bound (sorting)
# O(n) is upper bound (for loop)
# O(nlogn) is the complexity of this algorithm <<< O(2^n) of brute force algorithm

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

#LAMBDA FUNCTION - INTERMEZZO
#lambda function is an anonymous function:
#can have any number of arguments, but only one expression using those n arguments
f1 = lambda x: x
print(f1(2)) #returns 2
print(f1('hello')) #returns 'hello'
f2 = lambda x, y: x + y
print(f2(2, 3)) #returns 5
f3 = lambda x,y: 'factor' if x % y == 0 else 'not factor'
print(f3(9,3)) #returns 'factor'
print(f3(9,4)) #returns 'not factor'
# TIP: lambda functions are useful when you need a short function for a short period of time
# TIP: most of time easier to use a def statement than a lambda function
# Why was Lambda used in testGreedys? Because using getCost would order from most to least expensive, but we want the opposite

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
# testGreedys(foods, 750) #test greedy algorithm with 750 calories

# Why did we get different answers? 
# Because we don't get globally optimal solution, but locally optimal solution
# Greedy algorithm is often a practical way to get a pretty good approximate solution
# testGreedys(foods, 1000) #test greedy algorithm with 1000 calories
# here greedy by value was the winner
# should we use greedy algorithm? Yes, because easy to implement and computationally efficient
# but it's not always the best solution; don't even know how good the approximation is

# Exercise 2
# 0-1 Knapsack Problem
# Each item is represented by a pair (weight, value)
names = ['clock', 'picture', 'radio', 'vase', 'book', 'computer']
values = [175,90,20,50,10,200]
weights = [10,9,4,2,1,20]
items = buildMenu(names, values, weights)
# testGreedys(items, 20) #test greedy algorithm with 20 weight limit

# Exercise 3
# What is the complexity of these functions?

NUMBER = 3
def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        if n == NUMBER:
            return True
    return False
# O(n) time complexity

def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False
# O(n^2) time complexity

some_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def get_all_subsets(some_list): #function that creates the powerset of a list!
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset) # add partial_subset as is, without first_elt
        next_subset = partial_subset[:] + [first_elt] # create a new subset with first_elt
        subsets.append(next_subset) # add the new subset containing first_elt
    return subsets

print(get_all_subsets(some_list))

def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False