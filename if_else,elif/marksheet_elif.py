print("please enter your all subjects marks")
h=int(input("hindi = "))
m=int(input("math = "))
s=int(input("science = "))
a=int(input("art = "))
e=int(input("english = "))
tt=h+m+s+a+e
per=tt/500*100
print("total marks = ",tt,
      '''percentage= ''',per)
if per>80:
    print("A Grade")
elif per>60:
    print("B Grade")
elif per>50:
    print("C Grade")
else:
    print("you are fail")
