# دریافت تعداد اعداد
n = int(input())  # تعداد اعداد برای جمع

# لیستی برای ذخیره اعداد
numbers = []

# خواندن اعداد
for _ in range(n):
    number = input()  # خواندن عدد به صورت رشته
    numbers.append(number)

# جمع زدن اعداد
total_sum = sum(int(num) for num in numbers)  # تبدیل رشته به عدد و جمع زدن

# چاپ نتیجه
print(total_sum)