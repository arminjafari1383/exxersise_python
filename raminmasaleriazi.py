def find_sqrt_floor(n):
    """بزرگ‌ترین عدد صحیح x که x^2 <= n"""
    low, high = 0, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def find_sqrt_ceil(n):
    """کوچک‌ترین عدد صحیح x که x^2 >= n"""
    low, high = 0, n
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# تعداد سوالات
q = int(input())

# پردازش هر سوال
results = []
for _ in range(q):
    l, r = map(int, input().split())
    # پیدا کردن بازه ریشه‌های مربع
    start = find_sqrt_ceil(l)
    end = find_sqrt_floor(r)
    # محاسبه تعداد اعداد مربع کامل
    count = max(0, end - start + 1)
    results.append(count)

# چاپ نتایج
for res in results:
    print(res)










def find_sqrt_floor(n):
    low,high = 0,n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def find_sqrt_ceil(n):
    low,high = 0,n
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

q = int(input())
results = []
for _ in range(q):
    l,r = map(int,input().split())
    start = find_sqrt_ceil(l)
    end = find_sqrt_floor(r)
    count = max(0,end - start + 1)
    results.append(count)

for res in results:
    print(res)
