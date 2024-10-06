def fruits(tuple_of_fruits):
    good_fruits = {}  # لغت‌نامه برای ذخیره تعداد میوه‌های خوب
    
    for fruit in tuple_of_fruits:
        # بررسی شرایط خوب بودن میوه
        if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            name = fruit['name']
            if name in good_fruits:
                good_fruits[name] += 1  # اگر میوه قبلاً وجود دارد، مقدارش را افزایش می‌دهیم
            else:
                good_fruits[name] = 1  # اگر میوه وجود ندارد، آن را اضافه می‌کنیم
    
    return good_fruits
