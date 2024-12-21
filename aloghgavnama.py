def concert_sound(t, a, b):
    time = 0  # زمان فعلی
    roar_count = 0  # تعداد عرعرها
    moo_count = 0  # تعداد ماماها
    
    while time < t:
        # عرعر کردن
        if time < t:
            roar_count += 1
            time += 1
        # سکوت پس از عرعر
        time += a
        
        # ماما کردن
        if time < t:
            moo_count += 1
            time += 1
        # سکوت پس از ماما
        time += b

    return roar_count, moo_count

# ورودی را از کاربر دریافت کنید
t, a, b = map(int, input().split())

# محاسبه و نمایش خروجی
roar, moo = concert_sound(t, a, b)
print(roar, moo)
