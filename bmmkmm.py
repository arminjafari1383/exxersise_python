# تابع برای محاسبه ب.م.م. به روش اقلیدس
def gcd(n, m):# 8 20
    while m != 0:# 20
        n, m = m, n % m # 20 8
    return n

# تابع برای محاسبه ک.م.م.
def lcm(n, m, gcd_value):# 8 20 20
    return (n * m) // gcd_value

# دریافت ورودی از کاربر
n, m = map(int, input().split())

# محاسبه ب.م.م. و ک.م.م.
gcd_value = gcd(n, m)#20
lcm_value = lcm(n, m, gcd_value)# 8

# چاپ نتیجه
print(gcd_value, lcm_value)