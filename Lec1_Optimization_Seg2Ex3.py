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
        # print("subset in loop: " + str(subsets)) # to help follow the recursion

    return subsets

def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False

print(get_all_subsets([1,2])) #prints [[], [1], [2], [2, 1]]

# The time complexity of get_all_subsets is O(2^n) because the function is recursive and calls itself twice for each element in the list.
# Technically, the complexity is actually O (n * 2^n) because the sum() is O(n), but 2^n is already large enough that we can ignore the n multiplier.