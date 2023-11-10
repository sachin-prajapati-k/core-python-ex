'''Encapsulation is a mechanism of wrapping the data (variables) and code acting
on the data (methods) together as a single unit. In encapsulation, the variables
of a class will be hidden from other classes, and can be accessed only through
the methods of their current class.'''

'''encapsulation's "getter" and "setter" methods'''
class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)
        
