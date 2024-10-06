# دریافت تعداد کلمات و ورودی‌ها
n, m = map(int, input().split())

# دیکشنری برای ذخیره کردن پاسخ‌های آرایشگر
answers = {}

# خواندن ورودی‌های مربوط به پاسخ‌ها
for _ in range(n):
    question, response = input().split()
    answers[question] = response

# کلمات بز
bache_words = input().split()

# تولید و چاپ جواب آرایشگر
result = []
for word in bache_words:
    if word in answers:
        result.append(answers[word] + " kachal!")
    else:
        result.append("kachal!")

print(' '.join(result))