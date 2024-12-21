def count_possible_moves(board):
    moves = 0
    # جهت‌های ممکن: (dx, dy)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(7):
        for j in range(7):
            if board[i][j] == 'o':  # اگر نخود باشد
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy  # مختصات همسایه
                    nni, nnj = i + 2 * dx, j + 2 * dy  # مختصات پشت همسایه
                    # بررسی حرکت ممکن
                    if (
                        0 <= ni < 7 and 0 <= nj < 7 and
                        0 <= nni < 7 and 0 <= nnj < 7 and
                        board[ni][nj] == 'o' and
                        board[nni][nnj] == '.'
                    ):
                        moves += 1
    return moves


# دریافت ورودی از کاربر
board = []
print("")
for _ in range(7):
    board.append(input().strip())

# محاسبه و چاپ نتیجه
result = count_possible_moves(board)
print(f"{result}")
