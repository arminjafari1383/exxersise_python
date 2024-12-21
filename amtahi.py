def calculator(n, m, li):
    # مرحله 1: تقسیم لیست به گروه‌ها و محاسبه‌ی جمع هر گروه
    group_sums = []
    for i in range(0, n, m):
        group_sums.append(sum(li[i:i + m]))


    # مرحله 2: محاسبه ارزش نهایی لیست
    result = 0
    for i in range(len(group_sums)):
        if i % 2 == 0:
            result += group_sums[i]  # اعضای فرد را اضافه می‌کنیم
        else:
            result -= group_sums[i]  # اعضای زوج را کم می‌کنیم


    return result
