# # دریافت ورودی
# n, m = map(int, input().split())

# # تولید مستطیل 3n x 3m
# for i in range(3 * n):
#     row = ""
#     for j in range(3 * m):
#         if ((i // n) + (j // m)) % 2 == 0:
#             row += 'X'
#         else:
#             row += '.'
#     print(row)

n,m = map(int,input().split())
for i in range(3*n):
    row = ""
    for j in range(3 * m):
        if ((i // n) + (j // m)) % 2 == 0:
            row += 'X'
        else:
            row += '.'
    print(row)
    