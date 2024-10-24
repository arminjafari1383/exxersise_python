def check_cutlery(n, sequence):
    # تعداد S و F را شمارش می‌کنیم
    count_S = sequence.count('S')
    count_F = sequence.count('F')

    # بررسی می‌کنیم که آیا تعداد S و F برابر با n است یا خیر
    if count_S == n and count_F == n:
        return "YES"
    else:
        return "NO"

# دریافت ورودی
n = int(input())
sequence = input().strip()

# چک کردن و چاپ نتیجه
result = check_cutlery(n, sequence)
print(result)
