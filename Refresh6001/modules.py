import math as mathematics
a = mathematics.ceil(3.5)
print(a)

from math import ceil, pi
b = ceil(3.5)
c = pi
print(b)
print(c)

from math import ceil as c, pi as p

print(c(3.5))
print(p)

from math import *
print(ceil(3.5))
print(pi)

from mymath import *
print(inc(3.2))
print(dec(3.2))

# When you import a Python file (module), Python executes the entire file, 
# not just the specific class or function you import.
# Any code in the global scope of the module (outside functions or classes) 
# gets executed (eg print statements, plots etc. that are outside def or class).
# Python will execute file, import def/class, then execute def/class.

# To prevent top-level code in a module from executing during import, 
# use the if __name__ == "__main__": construct. 
# This ensures that code runs only when the file is executed directly, 
# not when it's imported.

# Code that should only run when this file is executed directly
if __name__ == "__main__":
    print("This gets executed only when pythonfile.py is run directly.")
    my_function()
    MyClass()

# Python is designed this way to allow for standalone scripts and reusable modules.
# The __name__ variable is a special variable in Python that gets set to "__main__"
# when the file is executed directly, and to the module name when imported.
