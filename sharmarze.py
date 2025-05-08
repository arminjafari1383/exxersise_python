n = int(input())
m = int(input())

if n == 1:
    print(m)
elif m == 1:
    print(n)
else:
    p = 2 *m + 2 * (n - 2)
    print(p)