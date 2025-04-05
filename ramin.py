import math
q = int(input())
results = []
for _ in range(q):
    L,r = map(int,input().split())
    count = math.floor(math.sqrt(r)) - math.ceil(math.sqrt(L)) + 1
    results.append(str(count))
print("\n".join(results))