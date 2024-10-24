def check_letter(s):
    i = 0
    while i < len(s):
        # تعداد تکرار حرف فعلی
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        # اگر تعداد تکرارها فرد باشد
        if count % 2 != 0:
            print("bad")
            return
        i += 1
    # اگر همه کلمات طول زوج داشته باشند
    print("khoob")

# ورودی نمونه
s = input()
check_letter(s)

