n = int(input())  # تعداد دکمه‌ها
caps_lock = False  # وضعیت ابتدایی CapsLock خاموش است
result = []

for _ in range(n):
    key = input().strip()  # دکمه وارد شده را می‌گیریم
    if key == "CAPS":
        caps_lock = not caps_lock  # وضعیت CapsLock را تغییر می‌دهیم
    else:
        if caps_lock:
            result.append(key.upper())  # اگر CapsLock روشن باشد، حرف را بزرگ اضافه می‌کنیم
        else:
            result.append(key.lower())  # اگر CapsLock خاموش باشد، حرف را کوچک اضافه می‌کنیم

print("".join(result))  # نتیجه را به صورت یک رشته چاپ می‌کنیم

