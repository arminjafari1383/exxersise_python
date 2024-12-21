# دریافت ورودی‌ها
n = int(input())  # تعداد اعداد
numbers = list(map(int, input().split()))  # لیست اعداد

# آرایه نهایی که نتیجه در آن ذخیره می‌شود
result = []

# پردازش اعداد یکی در میان بین امیر و محمد
turn_amir = True  # نوبت امیر است

while numbers:
    if turn_amir:
        # اگر نوبت امیر است، بزرگترین عدد را انتخاب و حذف کن
        max_num = max(numbers)
        result.append(max_num)
        numbers.remove(max_num)
    else:
        # اگر نوبت محمد است، کوچکترین عدد را انتخاب و حذف کن
        min_num = min(numbers)
        result.append(min_num)
        numbers.remove(min_num)
    
    # تغییر نوبت
    turn_amir = not turn_amir

# چاپ آرایه نهایی
print(" ".join(map(str, result)))
