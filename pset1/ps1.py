###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict() #initialize an empty dictionary

    f = open(filename, 'r') #open the file for reading
    
    for line in f: #iterate over the lines in the file
        line_data = line.split(',') #split the line on the comma
        cow_dict[line_data[0]] = int(line_data[1]) #add the cow name as the key and the weight as the value to the dictionary
    return cow_dict #return the dictionary


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # #CODE BELOW DID NOT WORK IN GRADER; PYTHON VERSION ISSUE WITH DICT.SORTED()
    # copyCows = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True)) #sorting the cows by weight, using dict(sorted()) to preserve the dictionary structure
    # trips = [] #initialize an empty list to store the trips
    # while len(copyCows) > 0: #while there are cows left to transport
    #     trip = [] #initialize an empty list to store the cows on the current trip
    #     total = 0 #initialize a variable to store the total weight of the cows on the current trip
    #     for cow, weight in copyCows.items(): #iterate over the cows
    #         if total + weight <= limit: #if the cow can fit on the current trip
    #             trip.append(cow) #add the cow to the trip
    #             total += weight #update the total weight of the cows on the trip
    #     for cow in trip: #iterate over the cows on the trip
    #         del copyCows[cow] #remove the cow from the dictionary of cows
    #     trips.append(trip) #add the trip to the list of trips
    # return trips #return the list of trips

    #CODE BELOW WORKED IN GRADER;  
    trips = []
    cowsCopy = cows.copy()
    sortedCows = sorted(cowsCopy.items(), key=lambda x: x[1], reverse = True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        trips.append(ship)
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = [] #initialize an empty list to store the trips
    cowsCopy = cows.copy() #create a copy of the dictionary of cows
    for partition in get_partitions(cowsCopy.keys()): #iterate over all the possible partitions of the cows
        valid = True #initialize a variable to store whether the current partition is valid
        for trip in partition: #iterate over the trips in the partition
            total = sum(cowsCopy[cow] for cow in trip) #calculate the total weight of the cows on the trip
            if total > limit: #if the total weight exceeds the limit
                valid = False #set valid to False
                break #break out of the loop
        if valid: #if the partition is valid
            if not trips or len(partition) < len(trips): #if the partition is the first valid partition or has fewer trips than the current best partition
                trips = partition #update the current best partition
    return trips

    # going to use the next(get_partitions()) function to get all the possible partitions of the cows
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    #load the data from the file
    cows = load_cows("ps1_cow_data.txt")
    #set the weight limit
    limit = 10

    #run the greedy algorithm and measure the time it takes
    start = time.time()
    greedy = greedy_cow_transport(cows, limit)
    end = time.time()
    print("Greedy algorithm took", end - start, "seconds")
    print("Number of trips:", len(greedy))

    #run the brute force algorithm and measure the time it takes
    start = time.time()
    brute = brute_force_cow_transport(cows, limit)
    end = time.time()
    print("Brute force algorithm took", end - start, "seconds")
    print("Number of trips:", len(brute))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
# limit=10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

# print(greedy_cow_transport({'Patches': 60, 'Polaris': 20, 'Muscles': 65, 'Miss Bella': 15, 'Horns': 50, 'MooMoo': 85, 'Lotus': 10, 'Louis': 45, 'Clover': 5, 'Milkshake': 75}, 100))

# #Test 1:
# print(greedy_cow_transport({'MooMoo': 85, 'Milkshake': 75, 'Horns': 50, 'Miss Bella': 15, 'Clover': 5, 'Patches': 60, 'Muscles': 65, 'Polaris': 20, 'Lotus': 10, 'Louis': 45}, 100))
# print(greedy_cow_transport({'Buttercup': 72, 'Rose': 50, 'Abby': 38, 'Daisy': 50, 'Willow': 35, 'Betsy': 65, 'Patches': 12, 'Dottie': 85, 'Lilly': 24, 'Coco': 10}, 100))
# print(greedy_cow_transport({'Buttercup': 11, 'Rose': 42, 'Abby': 28, 'Coco': 59, 'Willow': 59, 'Betsy': 39, 'Luna': 41, 'Starlight': 54}, 120))

# #Test 2:
# print(brute_force_cow_transport({'Horns': 25, 'Miss Bella': 25, 'MooMoo': 50, 'Milkshake': 40, 'Boo': 20, 'Lotus': 40}, 100))
# print(brute_force_cow_transport({'Buttercup': 72, 'Betsy': 65, 'Daisy': 50}, 75))
# print(brute_force_cow_transport({'Luna': 41, 'Starlight': 54, 'Buttercup': 11, 'Betsy': 39}, 145))

# Test 3:
compare_cow_transport_algorithms()
# Using the given default weight limits of 10 and the given cow data, both algorithms should not take more than a few seconds to run.

# Now that you have run your benchmarks, which algorithm runs faster?
# The greedy transport algorithm. X
# The brute force transport algorithm.
# They take the same amount of time.

# Consider the properties of the GREEDY algorithm. Will it return the optimal solution?
# Yes, all the time.
# No, never. 
# It could, but it depends on the data, not always. X

# Consider the properties of the BRUTE FORCE algorithm. Will it return the optimal solution?
# Yes, all the time. X
# No, never.
# It could, but it depends on the data, not always.