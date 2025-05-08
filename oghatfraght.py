# def count_occurrences(n, m, grid, word):
#     count = 0
#     word_len = len(word)

#     # جستجوی افقی (در هر ردیف)
#     for row in grid:
#         for i in range(m - word_len + 1):
#             if row[i:i + word_len] == word:
#                 count += 1

#     # جستجوی عمودی (در هر ستون)
#     for col in range(m):
#         col_str = ''.join(grid[row][col] for row in range(n))
#         for i in range(n - word_len + 1):
#             if col_str[i:i + word_len] == word:
#                 count += 1

#     return count

# # خواندن ورودی
# n, m = map(int, input().split())
# grid = [input().strip() for _ in range(n)]
# word = input().strip()

# # محاسبه و چاپ نتیجه
# print(count_occurrences(n, m, grid, word))

def count_occaurremces(n,m,grid,word):
    count = 0
    word_len = len(word)
    for row in grid:
        for i in range(m - word_len + 1):
            if row[i:i + word_len] == word:
                count += 1
    for col in range(m):
        col_str = ''.join(grid[row][col]for row in range(n))
        for i in range(n - word_len + 1):
            if col_str[i:i + word_len] == word:
                count += 1
    return count
n,m = map(int,input().split())
grid = [input().strip() for _ in range(n)]
word = input().strip()
print(count_occaurremces(n,m,grid,word))