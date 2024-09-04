
# دریافت تعداد سوالات
t = int(input())

# پردازش هر سوال
for _ in range(t):
    x, y = map(int, input().split())
    
    # بررسی اینکه آیا خر در مختصات (x, y) حضور داشته است یا خیر
    if x >= y:
        print(x + y)
    else:
        print(-1)