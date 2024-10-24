# دریافت ورودی
n, current_position = input().split()
n = int(n)

# پردازش حرکات
for _ in range(n):
    a, b = input().split()
    # بررسی اینکه نخود زیر کدام لیوان است و آیا باید موقعیتش تغییر کند
    if current_position == a:
        current_position = b
    elif current_position == b:
        current_position = a

# چاپ موقعیت نهایی نخود
print(current_position)

