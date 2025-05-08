def simulate_snake(moves):
    grid = [[0] * 8 for _ in range(2)]  # ساخت ماتریس ۲×۸
    row, col = 1, 0  # شروع از خانه‌ی پایین چپ
    grid[row][col] = 1  # علامت‌گذاری محل شروع

    for move in moves:
        col += 1  # به ستون بعدی می‌رویم

        if move == 'F':
            pass  # سطر تغییر نمی‌کند
        elif move == 'L':
            row -= 1
        elif move == 'R':
            row += 1

        # بررسی برخورد با دیواره
        if not (0 <= row <= 1 and 0 <= col <= 7):
            print("DEATH")
            return

        grid[row][col] = 1  # علامت‌گذاری خانه جدید

    # چاپ وضعیت نهایی مار
    print(''.join(str(cell) for cell in grid[0]))
    print(''.join(str(cell) for cell in grid[1]))


# خواندن ورودی و اجرا
moves = input().strip()
simulate_snake(moves)

