n = int(input())
l = [int(input())for _ in range(n)]
for i in range(n):
    if l[i] > 15:
        print("cooler")
    else:
        print("heater")