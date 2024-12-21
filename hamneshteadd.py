# تابعی برای محاسبه بزرگترین مقسوم‌علیه مشترک
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# ورودی
a, b = map(int, input().split())

# محاسبه بزرگترین مقسوم‌علیه مشترک
g = gcd(a, b)

# پیدا کردن تمام مقسوم‌علیه‌های g
divisors = []
for i in range(1, g + 1):
    if g % i == 0:
        divisors.append(i)

# چاپ خروجی
print(" ".join(map(str, sorted(divisors))))
