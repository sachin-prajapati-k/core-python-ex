#some tuple functions

t=(10,20,10,30,40)
a=max(t)
print(a)
#finds the maximum value in tuple
#but not support string when string is into the tuple
#works only with numeric value

b=min(t)
print(b)
#it finds the minimum value in a tuple

c=t.count(10)
print(c)
#it counts the giving value in a tuple

i=t.index(30)
print(i)
# it gives the index number of the giving value in a tuple

print(sum(t))
#it sum the all values of a tuple
#but works only with numeric value

print(sum(t,10))
#it sum and add the default value given by comma
