def solve_problem(test_cases):
    results = []
    for n, S, a in test_cases:
        # محاسبه مقدار x از معادله
        numerator = S - a  # صورت معادله
        denominator = n    # مخرج معادله
        
        # بررسی اینکه آیا تقسیم عدد صحیح و مثبت می‌شود
        if numerator > 0 and numerator % denominator == 0:
            x = numerator // denominator
            results.append(x)
        else:
            results.append(-1)
    return results

# ورودی را از کاربر دریافت کنید
t = int(input(""))
test_cases = []
for _ in range(t):
    n, S, a = map(int, input().split())
    test_cases.append((n, S, a))

# حل مسئله و نمایش خروجی
output = solve_problem(test_cases)
print("\n".join(map(str, output)))