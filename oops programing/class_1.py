# functions defined in the class are known as methods.
''' we can make objects in the class and use them by using the different variables
'''
class DemoClass:
    a=20
    def mul(self):
        print(5*7)

demoobject=DemoClass()
demoobject1=DemoClass()
print(demoobject1.a)
print(demoobject.a)

demoobject.mul();
