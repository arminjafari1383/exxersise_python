def can_fit(a, b, c, d, e, f):
    # تمام حالات ممکن از چرخش قالب یخ
    permutations = [
        (d, e), (d, f), (e, d), (e, f), (f, d), (f, e)
    ]
    for x, y in permutations:
        # بررسی تطابق با کف جعبه (a, b)
        if (x <= a and y <= b) or (x <= b and y <= a):
            return "zende mimuni"
    return "dari mimiri"

# ورودی را دریافت کنید
a, b, c, d, e, f = map(int, input().split())

# محاسبه و چاپ نتیجه
print(can_fit(a, b, c, d, e, f))