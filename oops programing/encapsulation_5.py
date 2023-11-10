''' An objects variables should not always be directly accessible.

The methods can ensure the correct values are set .
if an incorrect value is set, the mthod can return an error.'''

# private variables are defined by double underscore(__)
#we can not use the variables by objects
#we can use the variables inside the class and can't use out from class

'''class Student:
    __name="sachin"

objname=Student()
print(objname.__name)'''
'''this makes error'''

#we have to use the constructor to use the variable

class Student:
    __name1="sachin prajapati"
    def __init__(self):
        print(self.__name1) 
        self.__displayinfo()
    def __displayinfo(self):
        print("Hello World")
        

ob=Student()
#ob.__displayinfo()
'''this makes error'''
