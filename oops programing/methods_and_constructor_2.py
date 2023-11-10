#methods
class DemoClass():
    a=4
    def plusmul(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)
    def str(self):
        print("sachin prajapati")
    def argm(self,a,b):
        print(a+b)
obj=DemoClass()
obj.plusmul()
obj.str()
obj.argm(10,20)

print("constucture ---------------")
#constructure
''' when you make a constructure no need to call it
    constructure is defined with '__init__' keyword it is fix or reserve'''
class DemoClass1:
    def __init__(self):
        print("sachin prajapati")
obj1=DemoClass1()

        
