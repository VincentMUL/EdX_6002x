#From codereview.stackexchange.com                    
def partitions(set_): # recursive function to generate all possible partitions of a set
    if not set_: # base case
        yield []
        return
    for i in range(2**len(set_)//2): # iterate over all possible combinations of the set, eliminating duplicates given symetricity
        parts = [set(), set()] # initialize the two partitions (representing two subsets that will be built with each iteration)
        for item in set_:
            parts[i&1].add(item) #add item to first or second set/partition based on bit value of i
            #every i is read like: 000, 001, 010, 011, 100, 101, 110, 111
            i >>= 1 #shift i one bit to the right; decide which partition to add next item in set
        for b in partitions(parts[1]): #recursively generate partitions for the second set/partition
            yield [parts[0]]+b #combine first set/partition with the sub-partitions of the second set/partition


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_): # helper function to convert sets generated by partitions() into lists
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
# Effectively transforming each set-based partition into a list-based structure.


# ## Uncomment the following code  and run this file
# ## to see what get_partitions does if you want to visualize it:

# for item in (get_partitions(['a','b','c','d'])):
#     print(item)