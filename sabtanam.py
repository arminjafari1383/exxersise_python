def check_registration_rules(**kwargs):
    valid_usernames = []
    for username, password in kwargs.items():
        # 1. نام‌های کاربری غیرمجاز
        if username in ["quera", "codecup"]:
            continue
        # 2. بررسی طول نام کاربری
        if len(username) < 4:
            continue
        # 3. بررسی طول رمز عبور
        if len(password) < 6:
            continue
        # 4. بررسی اینکه رمز عبور فقط عدد نباشد
        if password.isdigit():
            continue
        # اگر همه شرایط برقرار بود، نام کاربری معتبر است
        valid_usernames.append(username)
    return valid_usernames