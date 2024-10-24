def days_from_start_of_year(month, day):
    # تعداد روزهای هر ماه در سال ۱۳۹۹
    days_in_months = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    
    # جمع روزها از ابتدای سال تا شروع ماه داده شده
    total_days = sum(days_in_months[:month-1]) + day
    return total_days

# دریافت ورودی‌ها
m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

# محاسبه تعداد روزهای هر تاریخ از ابتدای سال
days1 = days_from_start_of_year(m1, d1)
days2 = days_from_start_of_year(m2, d2)

# محاسبه و چاپ فاصله
print(abs(days1 - days2))
