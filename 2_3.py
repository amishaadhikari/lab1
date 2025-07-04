num=int(input("enter a number"))
i=1
f=1
if(num < 0):
    print("factorial does not exist")
else:
    while(i<=num):
        f=f*i
        i+=1
    print(f"factorial of {num} is {f} ")