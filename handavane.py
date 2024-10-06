# ورودی را به صورت لیست از اعداد دریافت می‌کنیم
watermelons = list(map(int, input().split()))

# شمارش تعداد هندوانه‌هایی که میزان قرمزی آنها >= 80 است
red_count = sum(1 for watermelon in watermelons if watermelon >= 80)

# تصمیم‌گیری براساس تعداد هندوانه‌های با میزان قرمزی >= 80
if red_count >= 3:
    print("Mamma mia!")
elif 1 <= red_count <= 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
