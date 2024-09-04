# دریافت تعداد فیلم‌ها
n = int(input())

# پردازش هر فیلم
for _ in range(n):
    # دریافت نام فیلم
    film_name = input()
    # تبدیل نام فیلم به فرمت مطلوب
    formatted_name = film_name.title()
    # چاپ نام اصلاح شده
    print(formatted_name)