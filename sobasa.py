def solve():
    # ورودی گرفتن
    n, a, b = map(int, input().split())
    goals = list(map(int, input().split()))
    
    # زمان‌های نیمه اول و نیمه دوم
    half1_end = 45 + a
    half2_start = 45
    half2_end = 90 + b
    
    # بررسی کردن تقسیم گل‌ها به دو نیمه
    for k in range(1, n + 1):
        # گل‌های اول تا k باید در نیمه اول باشند
        if all(goals[i] <= half1_end for i in range(k)):
            # گل‌های k+1 تا n باید در نیمه دوم باشند
            if all(goals[i] >= half2_start and goals[i] <= half2_end for i in range(k, n)):
                # همچنین باید ترتیب زمانی رعایت شده باشد
                if all(goals[i] < goals[i+1] for i in range(k-1, n-1)):
                    print("YES")
                    return
    
    print("NO")

# فراخوانی تابع
solve()

