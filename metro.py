# # دریافت وضعیت صندلی‌ها
# row1 = list(map(int, input().split()))  # وضعیت ردیف اول
# row2 = list(map(int, input().split()))  # وضعیت ردیف دوم


# # شمارش تعداد جفت‌های چشم تو چشم
# count = 0
# for i in range(8):
#     if row1[i] == 1 and row2[i] == 1:
#         count += 1

# # چاپ خروجی
# print(count)

row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))
count = 0
for i in range(8):
    if row1[i] == 1 and row2[i] == 1:
        count += 1
print(count)
