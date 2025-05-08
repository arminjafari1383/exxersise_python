n = int(input())

# اگر فقط یک رأس داریم، اصلاً یالی وجود نداره
if n == 1:
    print(0)
else:
    degree = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1

    print(max(degree))


