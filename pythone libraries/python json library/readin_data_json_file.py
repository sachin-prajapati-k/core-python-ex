import json
file=open("post.json","r")
x=file.read()
finaldata=json.loads(x)

for a in finaldata:
    print(a['WHAT'],a['AMOUNT'])
