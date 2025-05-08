n = int(input())
names = [input().strip() for _ in range(n)]

for i in range(n - 1):
    # 1. جمله اصلی: i به i+1
    print(f"{names[i]} to {names[i+1]}: ke ba in dar agar dar bande dar manand, dar manand.")
    
    # 2. شخص i+1 از i می‌پرسه
    print(f"{names[i+1]} to {names[i]}: dar manand?")
    
    # 3. زنجیره پرسش تا رسیدن به نفر اول
    for j in range(i, 0, -1):
        print(f"{names[j]} to {names[j-1]}: dar manand?")
    
    # 4. پاسخ نفر اول
    print(f"{names[0]} to {names[1]}: dar manand.")
    
    # 5. پاسخ برگشتی به سمت نفر جدید
    for j in range(1, i + 1):
        print(f"{names[j]} to {names[j+1]}: dar manand.")
