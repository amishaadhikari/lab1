print("Armstrong numbers between 100 and 999 are:")
for n in range(100, 1000):
    h=n//100
    t = (n // 10) % 10
    u= n % 10
    s=h**3 + t**3 + u**3
    if n == s:
        print(n)