#list delete functions


#del keyword
#it will use to remove the given index item, but we can not print it directly
l=[10,20,30,40,60]
del(l[1]) 
print(l)

#pop keyword
#it remove the item but also return the removed item
l1=[10,20,30,40,50,60]
l1.pop(2)
print(l1.pop(2))
print(l1)

#remove keyword
#it removes the given value directly without index no. but not return the removed
#value
l2=[10,20,30,0,50,60]
l2.remove(50)
print(l2)

#clear keyword
#it clear the complete list
l3=[10,20,30,40,60]
l3.clear()
print(l3)

