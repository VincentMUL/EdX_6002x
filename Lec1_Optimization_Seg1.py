# Optimization Model: Knapsack Problem
# What is an Optimization model?
# 1. objective function that is to be maximized or minimized
# 2. constraints that must be honored
# (3. decision variables that determine the values of the objective function)

# Many problems of real importance can be formulated as optimization models.
# It's way easier to reduce a problem to a problem that has already been solved than to solve it from scratch.
# Optimization problems are hard! Especially in computational complexity..
# A greedy algorithm is often a practical way to get a pretty good approximate solution.
# The knapsack problem is a classic optimization problem.

# 0 - 1 Knapsack Problem
# Given a set of items, each with a weight and a value, determine the number of each item to include in a collection
# so that the total weight is less than or equal to a given limit and the total value is as large as possible.

# Continuous or Fractional Knapsack Problem
# The same as the 0-1 knapsack problem, but you can take fractions of items.

# 0-1 Knapsack Problem
# Each item is represented by a pair (weight, value)
# The knapsack has a maximum capacity (weight limit) w
# A vector I of length n is used to represent the set of available items. Each element is 1 item.
# A vector V of length n is used to represent whether the items are taken or not. Each element is 1 or 0.
# V[i] = 1 if item I[i] is taken, V[i] = 0 if item I[i] is not taken.

# Essentially looking for a maximal value sum of (V*I.value) for the constraint (w) of the sum of (V*I.weight) <= w
# Number of solutions!

# First: Brute Force Algorithm
#1. Generate all possible combinations of items (powerset)
#2. Remove all combinations whose total weight exceeds the weight limit
#3. From the remaining combinations, select any one with the maximum value
# Not practical: size of powerset is 2^n (V is 0 or 1 and there are n items in I)
# O(2^n) time complexity (exponential time complexity)
# The 0-1 knapsack problem is inherently exponential; NP-complete. (Non-deterministic Polynomial-time complete)

# Exercise 1
items = {"dirt": (4,0), "computer": (10,30), "fork": (5,1), "problem set": (0,-10)}
# The weight of the dirt is 4, the value of the dirt is 0

def getValue(item):
    return items[str(item)][1]

def getWeight(item):
    return items[str(item)][0]

def metric1(item):
    weight = getWeight(item)
    if weight == 0:
        return float('inf')  # Avoid division by zero
    return getValue(item) / weight
# Problem set could give zerodivisionerror

def metric2(item):
    return  -getWeight(item)
# Picking lighter objects first; suboptimal

def metric3(item):
    return getValue(item)
# Picking objects with higher value first; suboptimal because:
# It will take the computer, the problem set, and the dirt because it has room for these three. 
# However, taking the problem set will decrease the value.

for item in items:
    # print(item) #checks if the dictionary is being read properly
    print(metric3(item))