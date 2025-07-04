names=['a','a','b','b','c','c','b','e']
d={}
for name in names:
    if name not in d.keys():
        d[name]=names.count(name)
print(d)
