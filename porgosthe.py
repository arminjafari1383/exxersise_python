# دریافت ورودی
n, m = map(int, input().split())

# خواندن ظرف اول و شمارش گوشت‌ها
first_dish_meat_count = 0
for _ in range(n):
    row = input().strip()
    first_dish_meat_count += row.count('*')

# خواندن ظرف دوم و شمارش گوشت‌ها
second_dish_meat_count = 0
for _ in range(n):
    row = input().strip()
    second_dish_meat_count += row.count('*')

# چاپ خروجی
print(first_dish_meat_count, second_dish_meat_count)