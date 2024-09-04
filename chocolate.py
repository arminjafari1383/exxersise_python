def solve(chocolates):
    eaten = [0, 0, 0, 0]
    current_person = 0
    current_section = 0

    while chocolates[current_section] > 0:
        # نفر فعلی یک شکلات از بخش روبرویش می‌خورد
        eaten[current_person] += 1
        chocolates[current_section] -= 1

        # چرخاندن ظرف به اندازه 90 درجه در جهت عکس عقربه‌های ساعت
        current_section = (current_section + 3) % 4

        # نفر بعدی
        current_person = (current_person + 1) % 4

        # اگر شکلاتی در بخش روبروی نفر فعلی باقی نمانده، حلقه متوقف می‌شود
        if chocolates[current_section] == 0:
            break
    
    print(' '.join(map(str, eaten)))

# ورودی‌های نمونه
chocolates = list(map(int, input().split()))
solve(chocolates)