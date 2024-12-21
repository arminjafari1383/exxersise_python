# # تابعی برای محاسبه ب.م.م (GCD) دو عدد
# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# # تابعی برای محاسبه ک.م.م (LCM) دو عدد
# def lcm(x, y):
#     return x * y // gcd(x, y)

# # محاسبه LCM چند عدد
# def lcm_multiple(numbers):
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = lcm(result, num)
#     return result

# # دریافت ورودی‌ها
# q = int(input())  # تعداد مقسوم علیه‌ها
# divisors = list(map(int, input().split()))  # لیست مقسوم علیه‌ها

# # محاسبه LCM مقسوم‌علیه‌ها
# lcm_value = lcm_multiple(divisors)

# # شمارش تعداد اعداد ممکن بین 1 تا 1000 که مضرب LCM باشند
# count = 0
# for i in range(1, 1001):
#     if i % lcm_value == 0:
#         count += 1

# print(count)








def gcd(x,y):
    while y:
        x,y = y, x % y
    return x


def lcm(x,y):
    return x * y // gcd(x,y)


def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result,num)
    return result


q = int(input())
divisors = list(map(int,input().split()))
lcm_value = lcm_multiple(divisors)
count = 0
for i in range(1,1001):
    if i % lcm_value == 0:
        count += 1
print(count)
