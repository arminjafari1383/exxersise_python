# تابع برای محاسبه فاکتوریل
def calculate_factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# ورودی
day, digit = map(int, input().split())

# محاسبه فاکتوریل به صورت دستی
factorial_result = str(calculate_factorial(day))

# شمارش تعداد تکرار رقم انتخابی
count = factorial_result.count(str(digit))

# خروجی
print(count)