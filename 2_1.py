n=int(input('enter a number'))
for i in range(2,n):
    if n%2==0:
        print(f'{n} is not prime')
        break
    else:
        print(f'{n} is  prime')
        break
