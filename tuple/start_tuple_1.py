# tuple is immutable data type
#it is faster than other data type
#it is orederd data type i.e. uses index no,
# data is stored in paranthesis ()
t=(12,23,34,45)
print(type(t))
print(t)
a=t[2]
print(a)

#how to iterate tuple

l=len(t)
for i in range(l):
    print(t[i])
'''
    we can find the len and then pass it into the tupple
    '''
for b in t:
    print(b)
'''
    other methode to iterate the tuple
    '''
