print("inheritance in python-------------------")
class A:
    def view(self):
        print("sachin prajapati")
class B(A):
    def view2(self):
        print("harsh kumar")
class C(B):
    def view3(self):
        print("Jiya Verma")
obj=C()
obj.view()
obj.view2()
obj.view3()

#multiple inheritance
#it only works in python not in java or php
print("multiple inheritance-------------------")
class D:
    def view4(self):
        print("Rahul kumar")
class E:
    def view5(self):
        print("Aashu kumar")
class F(D,E):
    def view6(self):
        print("kartik rajput")

obj1=F()
obj1.view4()
obj1.view5()
obj1.view6()

