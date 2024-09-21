# دریافت ورودی‌ها
a, b, c = map(int, input().split())

# دریافت زمان ورود و خروج سه نفر
times = []
for _ in range(3):
    start, end = map(int, input().split())
    times.append((start, end))

# یک لیست برای شمردن تعداد افراد در هر دقیقه
minutes = [0] * 101  # از دقیقه 1 تا 100 (اندیس 1 تا 100)

# پر کردن تعداد افراد در هر دقیقه
for start, end in times:
    for i in range(start, end):
        minutes[i] += 1

# محاسبه هزینه
total_cost = 0
for i in range(1, 101):
    if minutes[i] == 1:
        total_cost += a
    elif minutes[i] == 2:
        total_cost += 2 * b
    elif minutes[i] == 3:
        total_cost += 3 * c

# چاپ نتیجه
print(total_cost)
