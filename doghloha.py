def are_equal_necklaces(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
        a_rev = a[::-1]
    for i in range(len(a_rev)):
        if a_rev[i:] + a_rev[:i] == b:
            return True
    return False
t = int(input())
results = []
for _ in range(t):
    a,b = input().split()
    results.append("YES" if are_equal_necklaces(a,b) else "NO")
for res in results:
    print(res)

