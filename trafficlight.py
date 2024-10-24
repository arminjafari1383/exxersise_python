# خواندن ورودی‌ها
n, l = map(int, input().split())# 4 30

traffic_lights = []
for _ in range(n):
    d, r, g = map(int, input().split())#7 13 5
    traffic_lights.append((d, r, g))

# زمان سپری شده برای حرکت باقر
current_time = 0
position = 0

for d, r, g in traffic_lights:
    # باقر تا این چراغ حرکت می‌کند
    current_time += (d - position)  # مسافت تا چراغ بعدی7
    position = d#7
    
    # محاسبه زمان باقی‌مانده چراغ در وضعیت قرمز
    cycle_time = r + g  # 18طول چرخه‌ی زمانی
    time_at_light = current_time % cycle_time  #16موقعیت باقر در چرخه
    
    # بررسی اینکه آیا باقر پشت چراغ قرمز توقف می‌کند یا خیر
    if time_at_light < r:
        current_time += (r - time_at_light)  # زمان توقف پشت چراغ قرمز

# حرکت تا انتهای مسیر (دانشگاه)
current_time += (l - position)

# چاپ خروجی
print(current_time)