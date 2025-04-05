def average_shalap(n):
    # محاسبه نصف n
    half = n // 2
    
    # محاسبه مجموع بر اساس زوج یا فرد بودن n
    if n % 2 == 0:
        total = half * (half + 1)
    else:
        total = 2 * (half * (half + 1)) // 2 + (half + 1)
    
    # محاسبه میانگین
    return total / (n + 1)

# دریافت ورودی
n = int(input())
# چاپ خروجی با دقت ۶ رقم اعشار
print(f"{average_shalap(n):.6f}")

