# دریافت ورودی‌ها
a, b, x = map(int, input().split())

# شمارش تعداد حالت‌های ممکن
count = 0

# برای هر مضرب a از a تا x
for i in range(a, x + 1, a):
    # برای هر مضرب b از b تا x
    for j in range(b, x + 1, b):
        # بررسی اینکه مجموع از x بیشتر نشود
            count += 1

# چاپ خروجی
print(count)