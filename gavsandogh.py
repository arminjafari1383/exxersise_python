# ورودی گرفتن تعداد چرخانه‌ها و رمز
k = int(input())
password = input().strip()

# ورودی گرفتن اعداد هر چرخانه و محاسبه حداقل چرخش‌ها
total_turns = 0

for i in range(k):
    dial = input().strip()
    current_number = dial[0]#1
    target_number = password[i]#2
    
    # پیدا کردن شاخص عدد فعلی و عدد هدف در چرخانه
    current_index = dial.index(current_number)#0
    target_index = dial.index(target_number)#0
    
    # محاسبه تعداد چرخش‌ها در جهت ساعتگرد و پادساعتگرد
    clockwise_turns = (target_index - current_index) % 9#0
    counterclockwise_turns = (current_index - target_index) % 9#0
    
    # اضافه کردن کمترین تعداد چرخش به مجموع
    total_turns += min(clockwise_turns, counterclockwise_turns)

# چاپ حداقل تعداد چرخش‌ها
print(total_turns)