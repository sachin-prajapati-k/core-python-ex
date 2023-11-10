#list insert functions

#we can change the any item by assign new value at any index
l=[10,20,30,40,50,70]
l[0]=15
print(l)

#insert function
#it insert the new value at the given index no.
#first parameter is index no. and second is value
l1=[10,20,30,40,60]
l.insert(0,25)
print(l)

#append function
#it append(add) the new value or data type to the list
#it also append the different data type
l2=[10,20,70,40]
l3=[70,80]
l2.append(55)
print(l2)
l2.append(l3)
print(l2)

#extend function
#it add the value of data type
l4=[10,30,40,60]
l5=[55,77]
l4.extend(l5)
print(l4)
