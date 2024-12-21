# دریافت ورودی
x1 = int(input().strip())
v1 = int(input().strip())
x2 = int(input().strip())
v2 = int(input().strip())

# بررسی شرایط
if v1 == v2:
    # اگر سرعت‌ها برابر باشند
    if x1 == x2:
        print("SEE YOU")
    else:
        print("WAIT WAIT")
else:
    # اگر سرعت‌ها متفاوت باشند
    t = (x2 - x1) / (v1 - v2)
    if t > 0:
        print("SEE YOU")
    else:
        print("BORO BORO")


