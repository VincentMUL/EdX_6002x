a = [1,2,3,4,5,6]
b= ['I', 'am', 'a', 'list']
c = [1, 2, 3, 'am', 2.3]
d= [(1,2), (2,3), (3,4)] #list of tuples
e = [{1:2, 3:4},{1:"I"}] #list of dictionaries
f = [{1:2, 3:4},(1,2),5] #list of a dictionary, a tuple and an integer
g = [[1,2,3],[4,5,6],[7,8,9]] #nested lists

print(a[0]) #prints the first element of the list
print(b[-2]) #prints the second element from the end of the list
print(c[:2+1]) #prints the first 3 elements of the list

print(f[0][3]) #prints the value of the key 3 in the first dictionary of the list

a.append(7) #appends 7 to the end of the list
a.extend([8,9]) #appends 8 and 9 to the end of the list
a.pop() #removes the last element of the list
a.reverse() #reverses the order of the list

# mutable objects are objects that can be changed after they are created
# immutable objects are objects that cannot be changed after they are created
# lists are mutable objects
# tuples are immutable lists (objects), but can be sliced and indexed like lists

h = ([1,2,3],5,6,{1:'Tom',2:'Jerry'}, (9,10)) #tuple of a list, integers, a dictionary and a tuple
print(h[3][2]) #prints the value of the key '2' in the dictionary
print(h[0][1]) #prints the second element of the list
print(h[2:3+1]) #prints second integer and the dictionary
print(h[::2]) #prints the first, third and fifth elements of the tuple
# Tuples positions are fixed, so you cannot change the value of a tuple after it is created.
# Tuples are great for storing coordinates, dates, and other data that should not be changed.
