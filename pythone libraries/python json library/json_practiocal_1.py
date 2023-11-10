import json
d={
    'name':'sachin',
    'course':'python',
    'time':'2 hour'
    }
f=json.dumps(d)
print(f)
print(type(f))
