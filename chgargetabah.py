# n, x, y = map(int, input().split())
# a = list(map(int, input().split()))

# a.sort(reverse=True)  # موبایل‌هایی که شارژ بیشتری دارند را اول می‌گذاریم

# needed = 0
# # می‌خواهیم n-1 موبایل را به 100 برسانیم
# for i in range(n - 1):
#     needed += 100 - a[i]

# # موبایل باقی‌مانده هر چقدر می‌تواند شارژ بدهد
# available = 0
# donor = a[-1]
# while donor >= x:
#     donor -= x
#     available += y

# if available >= needed:
#     print("YES")
# else:
#     print("NO")
n,x,y = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
nedded = 0
for i in range(n - 1):
    nedded += 100 - a[i]
available = 0
donor = a[-1]
while donor >= x:
    donor -= x
    available += y
if available >= nedded:
    print("YES")
else:
    print("NO")


