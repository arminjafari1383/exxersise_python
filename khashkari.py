def tile_filling(n):
    # مقدارهای پایه
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # آرایه‌ای برای ذخیره نتایج
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # محاسبه با استفاده از رابطه بازگشتی
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# دریافت ورودی
n = int(input())
print(tile_filling(n))
