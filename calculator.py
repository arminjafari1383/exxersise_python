def calculate_floor(string):
    # شروع از طبقه‌ی ۰
    current_floor = 0

    # پیمایش رشته ورودی
    for move in string:
        # اگر 'U' بود، به طبقه بالا برو (افزایش ۱ به طبقه)
        if move == 'U':
            current_floor += 1
        # اگر 'D' بود، به طبقه پایین برو (کاهش ۱ از طبقه)
        elif move == 'D':
            current_floor -= 1

    # در نهایت طبقه مورد نظر را بازگردان
    return current_floor
