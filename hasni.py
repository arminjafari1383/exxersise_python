n, k = map(int, input().split())
a = list(map(int, input().split()))

photo_count = 0
current_sum = 0

for group in a:
    if current_sum + group <= k:
        current_sum += group
    else:
        photo_count += 1
        current_sum = group


if current_sum > 0:
    photo_count += 1

print(photo_count)
