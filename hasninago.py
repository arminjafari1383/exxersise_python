# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# count = 0
# current_sum = 0

# for a in arr:
#     if current_sum + a > k:
#         count += 1
#         current_sum = a
#     else:
#         current_sum += a

# # عکس آخر اگه چیزی مونده بود
# if current_sum > 0:
#     count += 1

# print(count)

n,k = map(int,input().split())
arr = list(map(int,input().split))
count = 0
current_sum = 0
for a in arr:
    if current_sum + a > k:
        count += 1
        current_sum = a
    else:
        current_sum += a
if current_sum > 0:
    count += 1
print(count)
