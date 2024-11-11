# Search Tree gave a better answer in short time for such a small problem.
# NOTE: If stuck in an endless calculation, use Ctrl+c in the console to stop the program.
# Trying out larger examples:
import random
from Lec2_DynamicPr_Seg1 import *

# #Code below will run a long time, that's why it's commented out
# def buildLargeMenu(numItems, maxVal, maxCost):
#     items = []
#     for i in range(numItems):
#         items.append(Food(str(i),
#                           random.randint(1, maxVal), #argument is sequence of integers and returns a random integer from the sequence
#                           random.randint(1, maxCost)))
#     return items

# for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#     items = buildLargeMenu(numItems, 90, 250)
#     testMaxVal(items, 750, False)
#     # testGreedys(items, 750)

# Exponentially slowing down, not hopeless in practise: Dynamic programming.
# Dynamic Programming (btw; name was used to make it sound impressive)
# - Break problem into subproblems
# - Solve each subproblem just once and save its answer
# - Avoid recomputing the answer by solving each subproblem just once
# - Use the saved answers to solve the original problem
# - This is a good strategy when a problem has overlapping subproblems
# - A problem has overlapping subproblems if an optimal solution involves solving the same subproblem multiple times
# - Dynamic programming is a good strategy when a problem has optimal substructure
# - A problem has optimal substructure if an optimal solution can be constructed efficiently from optimal solutions of its subproblems
# - Dynamic programming is a good strategy when the space of subproblems can be made small

# Example of Recursive Implementation of Fibonacci:
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(120)) #takes around 250000 years time to compute
# Bellman decided to use memoization, because it's a bad idea to repeat work 
# ie once fib(5) is computed, it should be saved and not computed again
# trading time for space; creating a table with data that is computed and saved
# then just check table for the data instead of computing it again

def fastFib(n, memo = {}): #default argument is an empty dictionary
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1: #base case
        return 1
    try: # try and see if in the dictionary
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result #store the result in the dictionary
        return result

# # Using the recursive fib function will take a long time, starting to struggle around '38'
# for i in range(121):
#     print('fib(' + str(i) + ') =', fib(i))

# This will run much faster than the recursive implementation
for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))

# This is clearly an ENORMOUS win in time complexity.
# But it only works when it has optimal substructure and overlapping subproblems.
# Optimal substructure: an optimal solution can be constructed efficiently from optimal solutions of its subproblems
# For Fibonacci, this is true because fib(n) = fib(n-1) + fib(n-2)
# For merge sort, this is also true because the optimal solution for a list of length n can be constructed from the optimal solutions of two lists of length n/2
# Overlapping subproblems: an optimal solution involves solving the same subproblem multiple times
# For Fibonacci, this is true because fib(n-1) + fib(n-2) = fib(n-2) + fib(n-3) + fib(n-2)
# For merge sort, this is not true because the subproblems are independent of each other