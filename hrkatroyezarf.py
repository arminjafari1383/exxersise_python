def min_steps_to_equalize(a, b, c):
    # مجموع آب‌ها
    total = a + b + c
    n = 3  # تعداد ظروف
    
    # بررسی امکان‌پذیری
    if total % n != 0:
        return -1  # غیرممکن
    
    mean = total // n
    diffs = [mean - x for x in [a,b,c]]
    positive_steps = sum(x for x in diffs if x > 0)
    return positive_steps

a, b, c = map(int, input("").split())
result = min_steps_to_equalize(a, b, c)
if result == -1:
    print("")
else:
    print(f"{result}")
