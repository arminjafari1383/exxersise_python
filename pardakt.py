from collections import Counter

# دریافت تعداد کلاس‌ها
t = int(input())

# برای هر کلاس
for _ in range(t):
    # دریافت تعداد دانش‌آموزان
    n = int(input())
    
    # حروف مورد نیاز برای هر کلمه
    all_counts = [Counter(input()) for _ in range(n)]
    
    # پیدا کردن بیشترین نیاز به حروف در هر کلاس
    result = Counter()
    
    for count in all_counts:
        for char, freq in count.items():
            result[char] = max(result[char], freq)
    
    # مجموع تعداد حروف مورد نیاز
    print(sum(result.values()))
