"""

Big O notation is a way of writing down the time complexity of an algorithm.
Time complexity refers to how fast an algorithm works compared to the input size n.
Big O is one form of asymptotic notation; the worst case scenario. 
Big Theta (two-sided bound) is average case scenario. Big Omega (one-sided) is best case scenario. All three are asymptotic notations.
In other words Big Omega is minimum runtime, Big Theta is average runtime, and Big O is maximum runtime.

Constant time: O(1)
Logarithmic time: O(log n)
Linear time: O(n)
Linearithmic time: O(n log n)
Polynomial time: O(n^c)
Exponential time: O(c^n)
Factorial time: O(n!)
c being 2 or 10 or any other constant

Favoured is Constant time or Logarithmic time.
"""

# O(1) "Constant time"
num = 100

def deductOne(num):
    num-=1
    return num

print("O(1): \n"+str(deductOne(num))+"\n")
# Regardless of the size of the input, it's just 1 operation; the time taken to run this function will always be the same.

# O(log n) "Logarithmic time"
num = 100

def divide(num):
    while num > 1:
        num//=2
        print(num)
    return num

print("O(log n): \n")
print(str(divide(num))) #different from divide(num) because divide(num) only prints the intermediate values and not the return value
print("\n")

# O(n) "Linear time"
num = 10

def addOnesToTestList(num):
    testList = []
    for i in range(0,num):
        testList.append(1)
        print(testList)
    return testList

print("O(n): \n")
addOnesToTestList(num) #see remark on line 41
print("\n")

# -> Linear time is way less efficient compared to Logarithmic time, because it takes n operations to complete.

# O(n log n) "Linearithmic time"
testList = [1,43,31,21,6,96,48,13,25,5]

def mergeSort(testList):
    if len(testList) < 2:
        return testList
    else:
        middle = len(testList)//2
        left = mergeSort(testList[:middle])
        right = mergeSort(testList[middle:])
        result = []
        print ("Left: ", left)
        print ("Right: ", right)
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        result += left
        result += right
        print ("Result: ", result)
        return result
# 10 elements divided by 2, divided by 2, divided by 2, etc. until 1 element is left -> logarithmic time O(log n)
# once divide into single elements, compare elements to each other, smallest element on the left, largest on the right;
# every element will be appended to a new list -> linear time O(n)

print("O(n log n): \n")
mergeSort(testList)
print("\n")

# -> Linearithmic time is less efficient than Linear time and Logarithmic time. 
# Linearithmic time complexity represents algorithms that perform logarithmic operations for each element in the input.

# O(n^c) "Polynomial time"
testList = [1,43,31,21,6,96,48,13,25,5]

def bubbleSort(testList):
    for i in range(len(testList)):
        for j in range(i+1, len(testList)):
            if testList[j] < testList[i]:
                testList[j], testList[i] = testList[i], testList[j]
            print(testList)

print("O(n^c): \n")
bubbleSort(testList)
print("\n")

# -> Polynomial time is less efficient than Linearithmic time, Linear time and Logarithmic time.
# Polynomial time complexity represents algorithms that perform a polynomial number of operations for each element in the input.
# Mostly this is caused by nested loops.

# O(c^n) "Exponential time"
# For instance trying to break a password by trying all possible combinations.
# When assuming numeric passwords, the number of possible combinations is 10^n, where n is the number of digits in the password.


"""
Function: 10n**2 + 10n + 20
n = 1000, output: 10,010,020
Clearly 20 and 10n will not have much of an impact on the output, so we can ignore them.
For the algorithm, only write the big O notation for the slowest part of the algorithm.
In this case, the slowest part is 10n**2, so the big O notation is O(n**2) -> Polynomial time
"""