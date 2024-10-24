# def min_screams(n):
#     # دارا و سارا در اولین نمایش جیغ می‌زنند
#     screams = 2
#     # اگر تعداد عروسک‌ها بیش از 1 باشد، باقی‌مانده‌ها را حساب می‌کنیم
#     for i in range(2, n+1):
#         # اگر عروسک i در موقعیت زوج باشد (کوچک‌ترین عروسک جدید است)
#         # دارا جیغ نمی‌زند، ولی سارا جیغ می‌زند.
#         # اگر عروسک i در موقعیت فرد باشد (بزرگ‌ترین عروسک جدید است)
#         # دارا جیغ می‌زند و سارا جیغ نمی‌زند.
#         screams += 1
#     return screams

# # دریافت ورودی
# n = int(input())

# # چاپ خروجی
# print(min_screams(n))

def min_screams(n):
    screams = 2
    for i in range(2,n + 1):
        screams += 1
    return screams
n = int(input())
print(min_screams(n))