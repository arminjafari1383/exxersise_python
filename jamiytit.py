# P, L = map(int, input().split())
# Y = int(input())

# for _ in range(Y):
#     P = 2 * P - L

# print(P)

P,L = map(int,input().split())
Y = int(input())
for _ in range(Y):
    P = 2 * P - L
print(P)
