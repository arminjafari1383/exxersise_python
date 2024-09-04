# دریافت ورودی‌ها
n, m = map(int, input().split())

# ساخت ماتریس هزینه‌ها
cost_matrix = []
for i in range(n):
    cost_matrix.append(list(map(int, input().split())))

# محاسبه مجموع هزینه سفرهای اسکندر
total_cost = 0
for _ in range(m):
    x, y = map(int, input().split())
    total_cost += cost_matrix[x - 1][y - 1]

# چاپ مجموع هزینه‌ها
print(total_cost)