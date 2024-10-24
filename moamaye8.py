import tkinter as tk
import random

class PuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle (Misplaced Tiles Heuristic)")
        
        # ایجاد دکمه‌های پازلی
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        self.board = self.generate_random_board()  # ایجاد پازل تصادفی

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    self.buttons[i][j] = tk.Button(root, text=str(self.board[i][j]), font=("Arial", 24), width=4, height=2)
                    self.buttons[i][j].grid(row=i, column=j)
                else:
                    self.buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=4, height=2, state=tk.DISABLED)
                    self.buttons[i][j].grid(row=i, column=j)

        # محاسبه تعداد قطعات نادرست
        self.misplaced_tiles = self.count_misplaced_tiles()
        self.label = tk.Label(root, text=f"Misplaced Tiles: {self.misplaced_tiles}", font=("Arial", 16))
        self.label.grid(row=3, columnspan=3)

    def generate_random_board(self):
        # ایجاد حالت تصادفی برای پازل
        numbers = list(range(9))  # اعداد ۰ تا ۸
        random.shuffle(numbers)  # ترتیب تصادفی اعداد
        board = [numbers[i:i+3] for i in range(0, 9, 3)]  # ماتریس ۳×۳
        return board
    
    def count_misplaced_tiles(self):
        """
        تابعی که تعداد قطعات نادرست را در پازل محاسبه می‌کند.
        """
        goal = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]  # حالت هدف

        misplaced = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0 and self.board[i][j] != goal[i][j]:
                    misplaced += 1
        
        return misplaced


# ایجاد رابط کاربری
root = tk.Tk()
app = PuzzleApp(root)
root.mainloop()