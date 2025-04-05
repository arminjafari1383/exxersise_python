# def can_reach_one(n):
#     visited = set()  # برای جلوگیری از ورود به چرخه
#     while n != 1:
#         if n in visited:  # اگر وارد چرخه شد
#             return "No"
#         visited.add(n)
#         if n % 2 == 0:  # اگر n زوج است
#             n //= 2
#         else:  # اگر n فرد است
#             n = 3 * n + 3
#         # بررسی می‌کنیم که اگر n از حد منطقی بزرگ‌تر شود، دیگر امکان ندارد به ۱ برسد
#         if n > 10**14:
#             return "No"
#     return "Yes"

# # ورودی
# n = int(input())
# # خروجی
# print(can_reach_one(n))

def can_reach_one