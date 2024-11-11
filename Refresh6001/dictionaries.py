#dict is a mutable datastructure that stores data in key-value pairs
#keys are unique and immutable (strings, numbers, tuples)
#values (not unique) can be any data type (even list or another dictionary)
#hashing; a process of converting a key into a unique value that can be used to identify the key

a = {1: 'Tom', 2: 'Jerry', 3: 'Spike'}
b = {(12, 'A'): 'John', (14, 'B'): 'Jane', (12, 'B'): 'Lydia', (14, 'A'): 'Mike'}
#keys need to be unique, for instance room number and class section so there are no duplicates

c = {2: ['I am', 'my name'], 3: ['this is it', 'i like you', 'i hope so']}
# values can be lists, numbers of words in each element of the list is the key in this example
d = {'E123': {'name': 'Tom', 'Age': 23}, 'E235':{'name': 'Jerry', 'Age': 25}}
# students are identified by their student number, and their essential details are stored in a dictionary
print(d['E123'])
print(d['E235']['Age'])
# dictionaries can be nested, and the values can be accessed by using the keys

a.keys() #returns a list of all the keys in the dictionary
a.values() #returns a list of all the values in the dictionary
a.items() #returns a list of all the key-value pairs in the dictionary as tuples
a.pop(2) #removes the key-value pair with the key 2
a.popitem() #removes the last key-value pair from the dictionary

# ALIASING
# aliasing is when multiple variables refer to the same object in memory
# if the object is mutable, then changing one variable will change the object
# ie modifying the data through one name will modify the data associated with all aliased names
# if the object is immutable, then changing one variable will not change the object
# aliasing is especially important when working with lists and dictionaries (mutable objects)
# shallow copy is a copy of the object, but the object is still the same object in memory
# deep copy is a copy of the object, and the object is a new object in memory

a = [1,2,3,4,5]
print(id(a)) #returns the memory address of the object
b = a #aliasing
print(id(b)) #returns the same memory address as a
b.append(6) #modifying b will also modify a
print(b) #prints [1,2,3,4,5,6]
print(a) #prints [1,2,3,4,5,6]
# in other words, b is a deep copy of a

# this would not occur in a string because strings are immutable

c = a[:] #shallow copy
c.append(7) #modifying c will not modify a
print(c) #prints [1,2,3,4,5,6,7]
print(a) #prints [1,2,3,4,5,6]
print(id(c)) #returns a different memory address from a

print(a == b) #returns True because the values are the same
print(a is b) #returns True because they are the same object in memory
print(a == c) #returns False because the values are different

d = 3.1212345676543212345
e = 3.1212345676543212345
print( d == e) #returns True because the values are the same
print( d is e) #returns False because they are different objects in memory, except here because of the float value

