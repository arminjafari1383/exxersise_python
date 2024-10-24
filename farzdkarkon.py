# def max_profit(n, profits):
#     max_so_far = 0
#     current_max = 0

#     for profit in profits:
#         current_max = max(0, current_max + profit)
#         max_so_far = max(max_so_far, current_max)

#     return max_so_far

# # ورودی
# n = int(input())  # تعداد روزها
# profits = list(map(int, input().split()))  # لیست سود و ضرر روزانه

# # خروجی
# print(max_profit(n, profits))

def max_profit(n,profits):
    max_so_far = 0
    current_max = 0
    for profit in profits:
        current_max = max(0,current_max + profit)
        max_so_far = max(max_so_far,current_max)
    return max_so_far
n = int(input())
profits = list(map(int,input().split()))
print(max_profit(n,profits))