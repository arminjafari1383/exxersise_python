def calculate_rest_time(W, S, I):
    total_work = W + S - I
    R = 24 - total_work
    return R

# نمونه ورودی‌ها و تست‌ها
print(calculate_rest_time(10, 11, 2))  # خروجی باید 5 باشد
print(calculate_rest_time(4, 5, 4))    # خروجی باید 19 باشد
