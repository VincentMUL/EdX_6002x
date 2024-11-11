def func():
    print('x', x)

    a = 1 # local
    print('a', a)

    b=y+1 # local
    print('b', b)
    
    d = 3 # local
x = 5 # global
y = 11 # global
d = 9 # global

print("d before calling the function", d)
func()
print("d after calling the function", d)
# In this case, d is not changed by calling the function, 
# because the function creates a new local variable d, instead of changing the global variable d.

# Local variables are only accessible 'locally', inside the function they are defined in.
# print('a', a) # NameError: name 'a' is not defined

# Global variables can be changed from inside a function, using global keyword.
def func2():
    global d # this changed the global variable d
    a = 1 # local
    print('a', a)

    b=y+1 # local
    print('b', b)
    
    d = 3 # local
print("d before calling the second function", d)
func2()
print("d after calling the second function", d)