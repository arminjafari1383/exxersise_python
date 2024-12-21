def find_winner(skills):
    max_skills = []
    
    for i, skill in enumerate(skills):
        max_skill = max(skill)
        max_skills.append((max_skill, i + 1))  # (مهارت، شماره شرکت‌کننده)
    
    # یافتن شرکت‌کننده با بیشترین مهارت
    winner = max(max_skills, key=lambda x: x[0])
    return winner[1]


# گرفتن ورودی از کاربر
skills = []
for i in range(4):
    skill = list(map(int, input().split()))
    skills.append(skill)


print(find_winner(skills))

