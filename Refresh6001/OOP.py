"""

Object-Oriented Programming (OOP) is a programming model focused on real-life objects,
instead of precesses that only input and output data. 

"""

class MITxStaff(object):
    firstName = ""
    lastName = ""


    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class TA(MITxStaff): # class subclass(superclass)
    awesomenessLevel = 0

    def __init__(self, firstName, lastName, awesomenessLevel):
        self.awesomenessLevel = awesomenessLevel
        MITxStaff.__init__(self, firstName, lastName) # call the superclass constructor, without re-initializing the variables
    
    def toString(self):
        return "{} {} has an awesomeness level of {}".format(self.firstName, self.lastName, self.awesomenessLevel)


Nitish = MITxStaff("Nitish", "Mittal")
Nitish = TA("Nitish", "Mittal", 100)

Jing = TA("Jing", "Liu", 9001)

print(Nitish.toString())
print(Jing.toString())