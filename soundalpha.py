# دریافت ورودی
word = input().strip()

# لیست حروف صدادار
vowels = {'a', 'e', 'i', 'o', 'u'}

# شمارش تعداد حروف صدادار در کلمه
vowel_count = sum(1 for char in word if char in vowels)

# محاسبه تعداد روش‌های خوانش
result = 2 ** vowel_count

# چاپ نتیجه
print(result)