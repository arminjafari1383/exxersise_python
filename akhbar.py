# def min_time_to_find_omid(n, A, m, O):
#     # پیدا کردن طول بلندترین پیشوند مشترک
#     l = 0
#     while l < n and l < m and A[l] == O[l]:
#         l += 1
#     return n + m - 2 * l

# # ورودی
# n = int(input())
# A = input()
# m = int(input())
# O = input()

# # خروجی
# print(min_time_to_find_omid(n, A, m, O))

def min_time_to_find_omid(n,A,m,O):
    l = 0
    while l < n and l < m and A[l] == O[l]:
        l += 1
    return n + m - 2 * l

n = int(input())
A = input()
m = int(input())
O = input()
print(min_time_to_find_omid(n,A,m,O))