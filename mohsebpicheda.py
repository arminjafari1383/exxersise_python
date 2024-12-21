# تابعی برای محاسبه فاکتوریل
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# تابعی برای محاسبه ترکیب nCk
def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# ورودی
a, x, n = map(int, input().split())

# محاسبه بسط دوجمله‌ای
result = 0
for k in range(n + 1):
    result += combination(n, k) * (x ** k) * (a ** (n - k))

# خروجی
print(result)
