# دریافت ورودی‌ها
n, m = map(int, input().split())

# لیست بازه‌های پیک اول و دوم
ranges1 = []
ranges2 = []

# دریافت بازه‌های پیک اول
for _ in range(n):
    l, r = map(int, input().split())
    ranges1.append((l, r))

# دریافت بازه‌های پیک دوم
for _ in range(m):
    l, r = map(int, input().split())
    ranges2.append((l, r))

# متغیر برای شمارش روزهای مشترک
common_days = set()

# بررسی تداخل بازه‌ها
for l1, r1 in ranges1:
    for l2, r2 in ranges2:
        # پیدا کردن روزهای مشترک بین دو بازه
        start = max(l1, l2)
        end = min(r1, r2)
        if start <= end:
            common_days.update(range(start, end + 1))

# خروجی تعداد روزهای مشترک
print(len(common_days))

