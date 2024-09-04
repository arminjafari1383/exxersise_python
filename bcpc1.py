def fish_hook_encryption(n, l, message):
    rows = [''] * n  # لیستی از رشته‌ها برای هر ردیف

    # مقادیر اولیه برای ردیف‌های بالا و پایین
    top_row = 0
    bottom_row = n - 1

    i = 0  # شاخص فعلی پیام

    while i < l:
        # حرکت به پایین
        for r in range(top_row, bottom_row + 1):
            if i < l:
                rows[r] += message[i]
                i += 1
        
        # حرکت به بالا
        for r in range(bottom_row - 1, top_row, -1):
            if i < l:
                rows[r] += message[i]
                i += 1

    # ترکیب تمام ردیف‌ها برای ایجاد پیام نهایی
    return ''.join(rows)

# گرفتن ورودی از کاربر
first_line = input("Enter l and n separated by space: ")
l, n = map(int, first_line.split())
message = input("Enter the message: ")

# فراخوانی تابع و نمایش خروجی
print(fish_hook_encryption(n, l, message))