def is_ronde(number):
    # ویژگی ۱: بررسی تکرار ۴ بار یک رقم
    for digit in set(number):
        if number.count(digit) >= 4:
            return True

    # ویژگی ۲: بررسی سه رقم متوالی یکسان
    for i in range(6):
        if number[i] == number[i+1] == number[i+2]:
            return True

    # ویژگی ۳: بررسی آینه‌ای بودن
    if number == number[::-1]:
        return True

    return False


# ورودی
t = int(input())  # تعداد شماره‌های تلفن
numbers = [input().strip() for _ in range(t)]  # شماره‌های تلفن

# خروجی
for number in numbers:
    if is_ronde(number):
        print("Ronde!")
    else:
        print("Rond Nist")
