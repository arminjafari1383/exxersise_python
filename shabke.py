n , m , k = map(int,input().split())

channels = []
for _ in range(n):
    channels.append(input().strip())

formul = (m - 1 + k) % n
print(channels[formul])