#dictionary is a mutable data type
#in which we can store data in 'keys' and 'values'
#it stores data in unordered format
#data is contain in curly braces '{}'

d={
    'name':'sachin',
    'age':23,
    'subject':'python'
   }

#access elements from a dictionary
print(d)
'''we can print the dictionary with keyl and values
   by passing var in print function'''

print(d['name'])
'''we can also print a specific value by passing key
    in dictionery '''

for i in d:
    print(i,end=" ")
    print(d[i])
