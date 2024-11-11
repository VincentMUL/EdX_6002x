a = " I'm going to watch the 'horror' movie!"
b = ''' I'm going to watch a "horror" movie!'''

#strings are indexed
print(a[0]) #index starts at 0; which is the space before the 'I'
print(a[5]) #space is also counted as an index; so the 5th index is the 'g' of going
print(a[-4]) #negative indexing to reach the 'o' of movie 
print(a[5:10])  #slicing; prints 'going' of the string (from the 5th index to the 9th index)
print(a[5:9+1]) #slicing; prints from the 5th index (6th character) until right before the second index (10th charac
print(a[5:-7+1]) #negative indexing
print(a[:5]) #don't need to add the start index if it has to start from 0th index
print(a[5:]) #don't need to add the end index if it has to go till the end of the string
print(a[::3]) #skipping characters; in this case starts with the 0th index and skips 2 characters
print(a[5:9+1:3]) #starts with the 5th index (6th character) and skips 2 characters until the 9th index (10th character)
print(a[::-1]) #reversing the string

help(str) #shows all the methods that can be used with strings
print(a.upper()) #converts all characters to uppercase
a.lstrip() #removes leading whitespaces
a.rstrip() #removes trailing whitespaces
a.replace(" ", "") #replaces all spaces with no space
a.find("going") #finds the index of the first occurrence of the word 'going', -1 if not found
a.find('l') #finds the index of the first occurrence of the letter 'l', -1 if not found
a.index('l') #finds the index of the first occurrence of the letter 'l', throws an error if not found

a = "Ana Bell Nitish Mittal Orhan Celikar"
a.split() #splits the string into a list of words; default is space

#strings are immutable 
a[0] = 'a' #this will throw an error because strings are immutable
a.replace('o', 'y') #this will work because it is not changing the original string
a = a.replace('o', 'y') #this will change the original string