def separator(ls):
    evens = []  # لیست برای اعداد زوج
    odds = []   # لیست برای اعداد فرد
    
    for num in ls:
        if num % 2 == 0:  # اگر عدد زوج باشد
            evens.append(num)
        else:  # اگر عدد فرد باشد
            odds.append(num)
    
    return (evens, odds)

