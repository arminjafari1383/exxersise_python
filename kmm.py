# دریافت ورودی
p, d = map(int, input().split())

# پیدا کردن کوچکترین مضرب d که باقیمانده آن بین 0 و p//2 باشد
for i in range(1, 1001):
    if d * i % p <= p // 2:
        print(d * i)
        break