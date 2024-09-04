# دریافت ورودی‌ها
n, t = input().split()
n = int(n)
result = []
# محاسبه زیرالفبای کد تخفیف معتبر
valid_subalphabet = set(t)
print(valid_subalphabet)

# بررسی کدهای تخفیف ورودی
for _ in range(n):
    s = input().strip()
    print(set(s))
    if set(s) == valid_subalphabet:
        result.append("Yes")
    else:
        result.append("No")

print("\n".join(result))
