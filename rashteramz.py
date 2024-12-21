def encrypt_message(n, k, message):
    message = list(message)  # تبدیل رشته به لیست برای قابلیت تغییر
    for _ in range(k):
        # مرحله 1: انتقال حرف آخر به ابتدای رشته
        last_char = message.pop()  # حذف حرف آخر
        message.insert(0, last_char)  # افزودن آن به ابتدای لیست


        # مرحله 2: افزایش هر حرف به حرف بعدی در الفبا
        for i in range(len(message)):
            if message[i] == 'z':
                message[i] = 'a'
            else:
                message[i] = chr(ord(message[i]) + 1)


    return ''.join(message)  # تبدیل لیست به رشته و بازگرداندن نتیجه


# دریافت ورودی
n = int(input())
k = int(input())
message = input()


# چاپ نتیجه
print(encrypt_message(n, k, message))
