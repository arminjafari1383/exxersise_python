# دریافت تعداد سوالات
t = int(input())
l = []

# پردازش هر سوال
for _ in range(t):
    x, y = map(int, input().split())
    
    if (x + y) % 2 == 0:
            if x == 0 and y == 0:
                 h = x + y
                 l.append(h)
            else:
                 z = x + y - 1
                 l.append(z)
    elif(x + y) % 2 != 0:
            h = x + y
            l.append(h)
    else:
        l.append(-1)

# چاپ نتایج
for i in l:
    print(i)