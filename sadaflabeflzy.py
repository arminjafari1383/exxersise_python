# t, w = map(int, input().split())

# # محاسبه x با استفاده از فرمول بالا
# x = t / (2 * (1 - (0.5) ** w))

# # چاپ با ۴ رقم اعشار
# print(f"{x:.4f}")

t,w= map(int,input().split())
x = t / (2 * (1 - (0.5) ** w))
print(f"{x:.4f}")

