n,m,k = map(int,input().split())
broken_keys = set()
for _ in range(k):
    r,c = map(int,input().split())
    broken_keys.add((r,c))
if k % 2 == 1:
    print(0)
elif k == n * m:
    print(-1)
else:
    for i in range(1,n + 1):
        for j in range(1, m + 1):
            if (i,j) not in broken_keys:
                print(1)
                print(i,j)
                exit()
