import random

# FIRST REFRESH GENERATORS:
# Generator is any function with the word "yield" in it.
def genTest():
    yield 1
    yield 2
genTest() #<generator object genTest at 0x00000146F9524B40>
# generators have a __next__ method that returns the next value:
#   yield suspends execution and returns a value and continue until running out of yield and then raise a StopIteration exception

# Why use this?
# Generators are useful when you need to compute a series of values, 
# but don't need to compute them all at once; especially in a loop.
# Generators are also useful when you don't know how many values you will need to compute, 
# or if you need to compute an infinite number of values.
def genFib() :
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        # this is an infinite loop

# To use a generator, you can either iterate over it, or call next on it.
fib = genFib()
print(fib) #<generator object genFib at 0x00000146F9524B40>
print(next(fib)) #1
print(next(fib)) #1
print(next(fib)) #2
print(next(fib)) #3
print(next(fib)) #5
print(next(fib)) #8
print(fib.__next__()) #13

for n in genFib():
    if n > 1000000:
        break
    print(n, end=' ')

# Generators seperate the concept of computing the elements of a series from the actual computation.
# This makes it easier to understand and maintain the code. Instead of generating a series of values,
# you can generate a specific value when you need it.

# EXERCISE 1:

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#Remember that with this case of 2 bags; there are 3 possible places for items: bag1, bag2, or neither -> 3**N combinations
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

# Functions to test the yieldAllCombos function
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

# TEST1:
items = buildItems()
combos = yieldAllCombos(items)
# Testing all the correct combinations exist in your solution
# Test successfully completed.

#TEST2:
items = buildRandomItems(1)
combos = yieldAllCombos(items)
# Testing all the correct combinations exist in your solution
# Test successfully completed.