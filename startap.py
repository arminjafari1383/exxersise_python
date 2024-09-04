def simulate_chocolate_eating(chocolates):
    # تعداد شکلات‌های خورده شده توسط هر نفر
    eaten = [0, 0, 0, 0]
    
    # نفر جاری که در نوبت است
    current_person = 0
    
    while chocolates[current_person] > 0:
        # فرد جاری یک شکلات از بخش مقابلش می‌خورد
        chocolates[current_person] -= 1
        eaten[current_person] += 1
        
        # چرخش ظرف در جهت عکس عقربه‌های ساعت
        current_person = (current_person + 1) % 4
    
    return eaten

# ورودی از کاربر
chocolates = list(map(int, input().split()))

# شبیه‌سازی و نمایش نتیجه
result = simulate_chocolate_eating(chocolates)
print(" ".join(map(str, result)))