l=[]
for n in range (1,51):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count+=1
    if(count==1):
        l.append(n)
num=int(input("enter a number:"))
if num in l:
    print(f"{num} is in list")
else:
    print(f"{num} is not in list")