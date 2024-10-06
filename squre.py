# دریافت اعداد a و b از ورودی
a = int(input())
b = int(input())

# شرط 1: بررسی ترتیب اشتباه
if b >= a:
    print("Wrong order!")
# شرط 2: بررسی اختلاف زوج نبودن
elif (a - b) % 2 != 0:
    print("Wrong difference!")
# شرط 3: رسم مربع توخالی
else:
    diff = (a - b) // 2  # اختلاف بین مربع بیرونی و داخلی
    for i in range(a):
        for j in range(a):
            if diff <= i < a - diff and diff <= j < a - diff:
                print("  ", end="")  # فضای خالی برای مربع داخلی
            else:
                print("* ", end="")  # ستاره برای مربع بیرونی
        print()  # رفتن به خط بعدی


