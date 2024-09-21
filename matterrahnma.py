# دریافت تعداد کارکنان
n = int(input())

# دیکشنری برای شمارش نام‌های کوچک
first_name_count = {}

# دریافت نام و نام خانوادگی هر کارمند
for _ in range(n):
    first_name, last_name = input().split()
    
    # افزایش شمارش نام کوچک در دیکشنری
    if first_name in first_name_count:
        first_name_count[first_name] += 1
    else:
        first_name_count[first_name] = 1

# محاسبه حداقل تعداد رنگ‌های مختلف
min_colors = max(first_name_count.values())

# چاپ نتیجه
print(min_colors)