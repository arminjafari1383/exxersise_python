# تابعی برای تبدیل عدد a به مبنای b
def to_base_b(a, b):
    digits = []
    while a > 0:
        digits.append(a % b)  # باقی‌مانده تقسیم a بر b را به لیست اضافه می‌کنیم
        a //= b  # a را بر b تقسیم می‌کنیم
    return digits[::-1]  # ارقام را از راست به چپ برمی‌گردانیم

# ورودی
a, b = map(int, input().split())

# تبدیل عدد a به مبنای b
digits = to_base_b(a, b)

# محاسبه sum1 و sum2
sum1 = sum(digits[i] for i in range(0, len(digits), 2))  # جمع ارقام فرد (0، 2، 4، ...)
sum2 = sum(digits[i] for i in range(1, len(digits), 2))  # جمع ارقام زوج (1، 3، 5، ...)

# مقایسه sum1 و sum2 و چاپ نتیجه
if sum1 == sum2:
    print("Yes")
else:
    print("No")
