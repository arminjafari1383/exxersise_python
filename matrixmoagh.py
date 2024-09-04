# تابعی برای بررسی اینکه یک خانه زینی است یا نه
def is_saddle_point(matrix, i, j):
    # بررسی ۴ همسایه خانه
    up = matrix[i-1][j] if i > 0 else None
    down = matrix[i+1][j] if i < len(matrix)-1 else None
    left = matrix[i][j-1] if j > 0 else None
    right = matrix[i][j+1] if j < len(matrix[0])-1 else None

    # شرایط زینی بودن
    if up is not None and down is not None and left is not None and right is not None:
        if (matrix[i][j] > left and matrix[i][j] > right and matrix[i][j] < up and matrix[i][j] < down) or \
           (matrix[i][j] < left and matrix[i][j] < right and matrix[i][j] > up and matrix[i][j] > down):
            return True
    return False

# دریافت ورودی‌ها
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# شمارش خانه‌های زینی
count = 0
for i in range(n):
    for j in range(m):
        if is_saddle_point(matrix, i, j):
            count += 1

# چاپ نتیجه
print(count)

