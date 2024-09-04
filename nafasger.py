# دریافت میزان نفس‌گیری هر سوال
a = list(map(int, input().split()))

# دریافت تعداد نفراتی که هر سوال را حل کردند
b = list(map(int, input().split()))


for i in range(2):
    if b[i] <= a[i]:
        print("yes")
        break
    else:
        print("no")
        break
