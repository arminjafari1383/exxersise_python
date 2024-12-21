# import math

# # ورودی‌ها
# n = int(input())
# m = int(input())
# a = int(input())
# b = int(input())

# # تعداد مراحل لازم در هر دو حالت
# steps_vertical = math.ceil(n / a)
# steps_horizontal = math.ceil(m / b)

# # کمینه تعداد مراحل
# min_steps = min(steps_vertical, steps_horizontal)

# print(min_steps)

import math
n = int(input())
m = int(input())
a = int(input())
b = int(input())
steps_vertical = math.ceil(n / a)
steps_horizontal = math.ceil(m / b)
min_steps = min(steps_vertical,steps_horizontal)
print(min_steps)
