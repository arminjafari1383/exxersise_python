def find(num1, num2, num3):
    # مجموعه‌ای از اعداد 1 تا 4
    all_numbers = {1, 2, 3, 4}
    
    # حذف اعداد انتخاب‌شده توسط مِلی، سَلیب و سَمیرا
    selected_numbers = {num1, num2, num3}
    
    # پیدا کردن عددی که انتخاب نشده است
    remaining_number = all_numbers - selected_numbers
    
    # تبدیل مجموعه به عدد و بازگرداندن آن
    return remaining_number.pop()


