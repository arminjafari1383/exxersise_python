# h =int(input())
# list = []
# for i in range(h):
#     a , b , c = map(int,input().split())
#     if a == c:
#         list.append(1)
#     else:
#         d = a - b
#         f = c // d
#         list.append(f)
# for j in range(h):
#     print(list[j])
t = int(input())
results = []

for _ in range(t):
    a, b, h = map(int, input().split())
    
    day = 0
    height = 0
    
    while True:
        day += 1
        height += a
        if height >= h:
            results.append(day)
            break
        height -= b

for r in results:
    print(r)
