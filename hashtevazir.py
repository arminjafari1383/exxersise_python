import tkinter as tk

# تابع برای بررسی اینکه آیا وزیر در این مکان امن است یا خیر
def is_safe(board, row, col, n):
    # بررسی تهدیدات در سمت چپ همان ردیف
    for i in range(col):
        if board[row][i] == 1:
            return False

    # بررسی تهدیدات در قطر بالایی چپ
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # بررسی تهدیدات در قطر پایینی چپ
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# تابع برای حل معمای ۸ وزیر با استفاده از بک‌ترکینگ
def solve_n_queens(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            board[i][col] = 0
    
    return False

# تابع برای رسم صفحه شطرنج و موقعیت وزیرها
def draw_board(board, n):
    window = tk.Tk()
    window.title("8 Queens Puzzle")

    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    cell_size = 400 // n

    # رسم صفحه شطرنج
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j * cell_size, i * cell_size,
                                    (j + 1) * cell_size, (i + 1) * cell_size,
                                    fill=color)

    # رسم وزیرها
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                canvas.create_oval(j * cell_size + 10, i * cell_size + 10,
                                   (j + 1) * cell_size - 10, (i + 1) * cell_size - 10,
                                   fill="black")

    window.mainloop()

# مقداردهی اولیه صفحه شطرنج
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

# حل معمای ۸ وزیر
if solve_n_queens(board, 0, n):
    # نمایش صفحه شطرنج و وزیرها با Tkinter
    draw_board(board, n)
else:
    print("No solution exists")