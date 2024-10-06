def readable_size(m):
    if m < 1024:
        return f"{m}B"
    elif m < 1024**2:
        return f"{m // 1024}KiB"
    else:
        return f"{m // (1024**2)}MiB"

T = int(input())  # تعداد تست‌ها
result = []  # لیست برای ذخیره نتایج
for _ in range(T):
    m = int(input())  # مقدار فایل برای هر تست
    result.append(readable_size(m))  # اضافه کردن نتیجه به لیست

# چاپ همه آیتم‌های لیست به صورت زیر هم
for item in result:
    print(item)
