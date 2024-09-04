# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def bth_prime_after_n(n, b):
#     count = 0
#     current = n + 1
#     while count < b:
#         if is_prime(current):
#             count += 1
#             if count == b:
#                 return current
#         current += 1

# # خواندن ورودی
# n = int(input())

# # محاسبه مجموع ارقام
# b = sum_of_digits(n)

# # پیدا کردن b امین عدد اول پس از n
# result = bth_prime_after_n(n, b)

# # چاپ نتیجه
# print(result)







def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def bth_prime_after_n(n,b):
    count = 0
    current = n + 1
    while count < b:
        if is_prime(current):
            count += 1
            if count == b:
                return current
        current += 1

n = int(input())
b = sum_of_digits(n)
result = bth_prime_after_n(n,b)
print(result)

