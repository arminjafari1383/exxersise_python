# def count_flips(cards):
#     flips = 0
#     for i in range(1, len(cards)):
#         if cards[i] != cards[i - 1]:
#             flips += 1
#     # اگر آخرین کارت پشت باشد، یک عملیات دیگر نیاز است
#     if cards[-1] == '0':
#         flips += 1
#     return flips


# # دریافت تعداد روزها و رشته‌های ورودی
# t = int(input())
# results = []
# for _ in range(t):
#     cards = input().strip()
#     results.append(count_flips(cards))


# # چاپ نتایج
# for res in results:
#     print(res)

def count_flips(cards):
    flips = 0
    for i in range(1,len(cards)):
        if cards[i] != cards[i - 1]:
            flips += 1
    if cards[-1] == '0':
        flips += 1
    return flips
t = int(input())
results = []
for _ in range(t):
    cards = input().strip()
    results.append(count_flips(cards))
for res in results:
    print(res)
        