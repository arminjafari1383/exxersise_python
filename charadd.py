def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def solve(n, a, b, c, d):
    nums = [a, b, c, d]
    total = 0

    # ترکیب‌هایی با اندازه‌های مختلف (1 تا 4 عضوی)
    for i in range(1, 16):  # از 0001 تا 1111 (نمایش باینری)
        bits = []
        for j in range(4):
            if (i >> j) & 1:
                bits.append(nums[j])

        # محاسبه‌ی ک.م.م. برای ترکیب انتخاب‌شده
        l = bits[0]
        for k in range(1, len(bits)):
            l = lcm(l, bits[k])

        count = n // l
        if len(bits) % 2 == 1:
            total += count  # اگر تعداد اعضای ترکیب فرد بود، اضافه کن
        else:
            total -= count  # اگر زوج بود، کم کن

    return total

# گرفتن ورودی از کاربر
n, a, b, c, d = map(int, input().split())
print(solve(n, a, b, c, d))

