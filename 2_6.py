p=0
n=0
z=0
for i in range(1,11):
    num=int(input(f"enter number {i}:"))
    if num > 0:
        p+=1
    elif num < 0:
        n+=1
    else:
        z+=1
print(f"positive= {p} negative= {n}   zero= {z}")