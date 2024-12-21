def minimum_cocoa_needed(n, a):
    current_sum = 0
    min_cocoa = 0

    for value in a:
        current_sum += value
        if current_sum < min_cocoa:
            min_cocoa = current_sum

    return -min_cocoa

# ورودی نمونه
n = int(input())
a = list(map(int, input().split()))

# خروجی
print(minimum_cocoa_needed(n, a))

