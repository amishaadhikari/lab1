s = "hello"
a=set(s)
d = {}
for i in a:
    d[i] = s.count(i)
print(d)