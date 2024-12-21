def decimal_to_base(n, b):
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEF"  # برای نمایش اعداد بزرگ‌تر از ۹
    result = ""
    
    while n > 0:
        remainder = n % b  # باقی‌مانده تقسیم
        result = digits[remainder] + result
        n //= b  # تقسیم عدد بر مبنای خواسته شده
    
    return result

# دریافت ورودی
n, b = map(int, input().split())

# تبدیل و چاپ نتیجه
output = decimal_to_base(n, b)
print(output)