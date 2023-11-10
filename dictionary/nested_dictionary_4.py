d={
    'naman':{'age':20,'class':'12th','course':'basic'},
    'sagar':{'age':23,'class':'b.sc','course':'python'},
    'harsh':{'age':21,'class':'m.com','course':'o level'}
    }
print(d)
print(d["sagar"]) #we can get the specific value by giving key
print(d['harsh']['course']) #we can also get the dictionary like it

'''
    how to iterate a dictionary
    '''
for j,k in d.items():
    print(j,k)
    for l in k.values():
        print(l)
'''
    we can get the all values and keys by for loop
    '''

for x,y in d.items():
    print(x,y['age'],y['course'])
'''
    we can get the values by passing the key name
    '''

# how to update the nested dictionary

d['naman']['class']='A level'
print(d)
d.clear()
print(d)
        

