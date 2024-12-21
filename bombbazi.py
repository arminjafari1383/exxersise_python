# تابعی برای بررسی و به‌روزرسانی خانه‌های اطراف یک بمب
def update_neighbors(board, row, col, n, m):
    for i in range(-1, 2):  # بررسی سطرهای مجاور
        for j in range(-1, 2):  # بررسی ستون‌های مجاور
            new_row = row + i
            new_col = col + j
            # بررسی اینکه در محدوده جدول قرار دارد و بمب نیست
            if 0 <= new_row < n and 0 <= new_col < m and board[new_row][new_col] != '*':
                board[new_row][new_col] += 1

# ورودی‌ها
n, m = map(int, input().split())  # تعداد سطر و ستون‌ها
k = int(input())  # تعداد بمب‌ها

# ایجاد جدول m × n و پر کردن آن با صفر
board = [[0 for _ in range(m)] for _ in range(n)]

# دریافت مکان بمب‌ها
for _ in range(k):
    r, c = map(int, input().split())
    r -= 1  # تبدیل به اندیس صفرمبنای پایتون
    c -= 1  # تبدیل به اندیس صفرمبنای پایتون
    board[r][c] = '*'  # قرار دادن بمب
    update_neighbors(board, r, c, n, m)  # به‌روزرسانی خانه‌های اطراف بمب

# چاپ جدول نهایی
for row in board:
    print(" ".join(map(str, row)))



