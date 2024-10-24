def bank_day(day):
    if day in ["shanbe", "doshanbe", "chaharshanbe"]:
        return "perspolis"
    elif day in ["yekshanbe", "seshanbe", "panjshanbe"]:
        return "bahman"
    elif day == "jome":
        return "tatil"

# خواندن ورودی
day = input().strip()

# چاپ خروجی
print(bank_day(day))
