# n = int(input())  # تعداد ستون‌ها
# heights = [int(input()) for _ in range(n)]  # ارتفاع ستون‌ها

# # محاسبه مجموع ارتفاع‌ها
# total_height = sum(heights)

# # ارتفاع هدف
# target_height = total_height // n

# # محاسبه تعداد جابجایی‌های لازم
# moves = 0
# for height in heights:
#     if height > target_height:
#         moves += height - target_height

# print(moves)

n = int(input())
heights = [int(input()) for _ in range(n)]
total_height = sum(heights)
target_height = total_height // n
moves = 0
for height in heights:
    if height > target_height:
        moves += height - target_height
print(moves)
