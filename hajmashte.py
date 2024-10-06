def determine_title(trips):
    if trips[0] == 'Y':
        return "Haji"
    elif trips[1] == 'Y':
        return "Karbalaee"
    elif trips[2] == 'Y':
        return "Mashti"
    else:
        return "Agha"

# دریافت ورودی
trips = input()

# چاپ نتیجه
print(determine_title(trips))