import json
'''
    if you have a json string, you can pass it by using the
    json.loads() method.
    '''
#here we create a json
d='{"name":"sachin","class":"b.sc.","lan":"python"}'

#pass json
y=json.loads(d)
print(y)
print(type(y))
for a in y:
    print(a,y[a])
