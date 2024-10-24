# دریافت ورودی
rows1, cols1, cols2 = map(int, input().split())

# ایجاد و پر کردن ماتریس اول
matrix1 = []
for i in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)

# ایجاد و پر کردن ماتریس دوم
matrix2 = []
for i in range(cols1):
    row = list(map(int, input().split()))
    matrix2.append(row)

# ایجاد ماتریس نتیجه با ابعاد مناسب
result = [[0] * cols2 for _ in range(rows1)]

# انجام ضرب دو ماتریس
for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# چاپ ماتریس حاصل
for row in result:
    print(' '.join(map(str, row)))
