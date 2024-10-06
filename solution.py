# دریافت ورودی‌ها
N = int(input())  # تعداد سوالات
answers = input()  # کلید سوالات

# تعریف الگوها
keyvoon_pattern = [3, 3, 1, 1, 2, 2]  # دوره تناوب 6
nezam_pattern = [1, 2, 3]  # دوره تناوب 3
shirfarhad_pattern = [2, 1, 2, 3]  # دوره تناوب 4

# شمارش تعداد پاسخ‌های درست
keyvoon_score = 0
nezam_score = 0
shirfarhad_score = 0

for i in range(N):
    if int(answers[i]) == keyvoon_pattern[i % len(keyvoon_pattern)]:
        keyvoon_score += 1
    if int(answers[i]) == nezam_pattern[i % len(nezam_pattern)]:
        nezam_score += 1
    if int(answers[i]) == shirfarhad_pattern[i % len(shirfarhad_pattern)]:
        shirfarhad_score += 1

# پیدا کردن بیشترین نمره
max_score = max(keyvoon_score, nezam_score, shirfarhad_score)

# چاپ بیشترین نمره
print(max_score)

# چاپ نام افرادی که بیشترین نمره را دارند
if keyvoon_score == max_score:
    print("keyvoon")
if nezam_score == max_score:
    print("nezam")
if shirfarhad_score == max_score:
    print("shir farhad")