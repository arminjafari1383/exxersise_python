def convert_to_base(n, base):
    result = ""
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

# ورودی‌ها
a = input().strip()
b = int(input())
c = int(input())

# تبدیل عدد a از مبنای b به مبنای 10
decimal_value = int(a, b)

# تبدیل عدد از مبنای 10 به مبنای c
converted_value = convert_to_base(decimal_value, c)

# بررسی اینکه آیا عدد در مبنای c پالیندروم است یا نه
if converted_value == converted_value[::-1]:
    print("YES")
else:
    print("NO")

