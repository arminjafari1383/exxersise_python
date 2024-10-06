# دریافت ورودی
n = int(input())

# شمارش تعداد تقسیم ها بر ۲
log_value = 0
while n > 1:
    n //= 2
    log_value += 1

# چاپ نتیجه
print(log_value)
