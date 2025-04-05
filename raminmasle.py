def integer_sqrt(x):
    """محاسبه ریشه صحیح با استفاده از جستجوی دودویی"""
    if x == 0 or x == 1:
        return x  # ریشه‌ی صفر و یک، خودشان هستند
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans

def count_perfect_squares(q, queries):
    results = []
    for l, r in queries:
        # ریشه‌ی پایین و بالا را محاسبه می‌کنیم
        sqrt_r = integer_sqrt(r)
        sqrt_l = integer_sqrt(l - 1)  # ل-1 برای شامل نشدن ل کوچک‌تر از اولین مربع کامل
        count = sqrt_r - sqrt_l
        results.append(count)
    return results

# ورودی
q = int(input())  # تعداد پرسش‌ها
queries = [tuple(map(int, input().split())) for _ in range(q)]

# محاسبه و خروجی
results = count_perfect_squares(q, queries)
for res in results:
    print(res)







def integer_sqrt(x):
    if x == 0 or x == 1:
        return x
    low,high = 0,x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans

def count_perfect_squares(q,queries):
    result = []
    for l,r in queries:
        sqrt_r = integer_sqrt(r)
        sqrt_l = integer_sqrt(l - 1)