# دریافت ورودی از کاربر
n = int(input(""))
road = list(map(int, input().split()))

# بررسی دست‌اندازها
def has_bump(road, n):
    for i in range(1, n - 1):
        if road[i] > road[i - 1] and road[i] > road[i + 1]:
            return True
    return False

# نتیجه‌گیری بر اساس وجود دست‌انداز یا عدم آن
if has_bump(road, n):
    print("Ey baba :(")
else:
    print("Bah Bah! Ajab jooji!")