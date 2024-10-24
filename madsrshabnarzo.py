# لیست برای صندلی‌های عقب: [چپ, وسط, راست]
back_seats = [None, None, None]

for _ in range(4):
    entry = input().split()  # خواندن ورودی
    name, door = entry[0], entry[1]  # جدا کردن اسم مسافر و دری که از آن وارد شده
    
    if door == 'L':
        back_seats[0] = name  # مسافر در صندلی چپ می‌نشیند
    elif door == 'R':
        if back_seats[2] is None:
            back_seats[2] = name  # اگر صندلی راست خالی است، این مسافر آنجا می‌نشیند
        else:
            back_seats[1] = back_seats[2]  # مسافر قبلی که سمت راست نشسته بود به وسط منتقل می‌شود
            back_seats[2] = name  # مسافر جدید سمت راست می‌نشیند

# خروجی: اسم مسافری که وسط نشسته است
print(back_seats[1])