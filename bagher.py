def next_permutation(x):
    # تبدیل عدد به لیست از ارقام
    x = list(str(x))
    
    # پیدا کردن نقطه شکست
    i = len(x) - 2
    while i >= 0 and x[i] >= x[i + 1]:
        i -= 1
    
    # اگر نتوانستیم نقطه‌ای پیدا کنیم، یعنی بزرگترین جایگشت است
    if i == -1:
        return 0
    
    # پیدا کردن جایگزین مناسب
    j = len(x) - 1
    while x[j] <= x[i]:
        j -= 1
    
    # جابجایی ارقام
    x[i], x[j] = x[j], x[i]
    
    # مرتب‌سازی باقی ارقام
    x = x[:i + 1] + sorted(x[i + 1:])
    
    # تبدیل لیست به عدد
    return int("".join(x))

# خواندن ورودی
x = int(input())

# چاپ خروجی
print(next_permutation(x))







