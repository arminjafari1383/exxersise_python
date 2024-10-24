# def gcd(a, b):
#     # اگر b برابر با صفر شد، a همان ب.م.م است
#     if b == 0:
#         return abs(a)
#     # بازگشت به تابع با استفاده از الگوریتم اقلیدس
#     return gcd(b, a % b)

# # دریافت ورودی از کاربر
# a = int(input())
# b = int(input())

# # محاسبه و چاپ ب.م.م
# print(gcd(a, b))

def gcd(a,b):
    if b == 0:
        return abs(a)
    return gcd(b,a % b)
a = int(input())
b = int(input())
print(gcd(a,b))
