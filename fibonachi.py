def ShowFibNth(n, next_n):
    # چاپ مقدار فعلی
    print(n)
    
    # شرط پایان بازگشتی: اگر به جمله اول یا صفرم رسیدیم، بازگشت کنیم
    if n == 1 and next_n == 1:
        return
    if n == 1 and next_n == 2:
        return
    if n == 0:
        return

    # فراخوانی بازگشتی برای یافتن جملات قبلی فیبوناچی
    ShowFibNth(next_n - n, n)

# دریافت ورودی‌ها
n = int(input())
next_n = int(input())

# فراخوانی تابع
ShowFibNth(n, next_n)