# دریافت ورودی‌ها
n = int(input())  # تعداد دانشجویان
names = input().split()  # نام دانشجویان

# مرحله سلام کردن
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        print(f"{names[i]}: salam {names[j]}!")

# مرحله خداحافظی
for i in range(n):
    print(f"{names[i]}: khodafez bacheha!")
    for j in range(i + 1, n):
        print(f"{names[j]}: khodafez {names[i]}!")

