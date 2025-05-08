def josephus(n):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1) + 2) % n or n

n = int(input())
print(josephus(n))

