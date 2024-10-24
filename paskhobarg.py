# دریافت ورودی
n = int(input())  # تعداد سوالات
key = input()  # کلید آزمون
k = int(input())  # تعداد پاسخ‌برگ‌ها
l = []
# پردازش هر پاسخ‌برگ
for _ in range(k):
    t = 0  # تعداد پاسخ‌های درست
    f = 0  # تعداد پاسخ‌های نادرست
    for i in range(n):
        answer = input()  # خواندن پاسخ سوال iام
        marked_count = answer.count('#')  # تعداد گزینه‌های علامت خورده
        correct_option = key[i]  # گزینه صحیح سوال iام
        
        # بررسی وضعیت سوال
        if marked_count == 0:
            continue  # نزده
        elif marked_count == 1 and answer['ABCD'.index(correct_option)] == '#':
            t += 1  # درست
        else:
            f += 1  # نادرست
    
    # محاسبه نمره
    score = 3 * t - f
    l.append(score)
    
for i in range(k):
    print(l[i])

