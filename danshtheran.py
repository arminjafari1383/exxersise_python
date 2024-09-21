a , b = map(int,input().split())
if a % b == 0:
    print(a // b)
else:
    c = a // b
    d = c + 1
    print(d)
    