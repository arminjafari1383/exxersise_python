# دریافت ورودی
left1, right1 = input().split()  # هندزفری اول
left2, right2 = input().split()  # هندزفری دوم

# بررسی تطابق موسیقی‌ها
if left1 == right1 or right2 == left2 or left1 == right2 or right1 == left2:
    print("YES")
else:
    print("NO")