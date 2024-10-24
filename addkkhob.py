# def count_divisors(num):
#     count = 0
#     for i in range(1, int(num**0.5) + 1):
#         if num % i == 0:
#             count += 1
#             if i != num // i:  # اگر مقسوم‌علیه برابر نباشند
#                 count += 1
#     return count

# def find_first_good_number_with_min_divisors(k):
#     n = 1
#     while True:
#         good_number = n * (n + 1) // 2  # محاسبه عدد خوب
#         if count_divisors(good_number) >= k:
#             return good_number
#         n += 1

# # دریافت ورودی
# k = int(input())

# # پیدا کردن و چاپ عدد خوب
# result = find_first_good_number_with_min_divisors(k)
# print(result)

def count_divisors(num):
    count = 0
    for i in range(1,int(num ** 0.5)+1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count
def find_first_good_number_with_min_divisors(k):
    n = 1
    while True:
        good_number = n * (n + 1) // 2
        if count_divisors(good_number) >= k:
            return good_number
        n += 1
k = int(input())
result = find_first_good_number_with_min_divisors(k)
print(result) 