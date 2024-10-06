# def find_least_frequent_color(n, colors):
#     # لیستی برای ذخیره تعداد هر رنگ (از 1 تا 100)
#     frequency = [0] * 101
    
#     # شمارش تعداد هر رنگ
#     for color in colors:
#         frequency[color] += 1
    
#     # پیدا کردن کمترین تعداد
#     min_count = float('inf')
#     min_color = -1
    
#     # بررسی تمام رنگ‌ها از 1 تا 100
#     for color in range(1, 101):
#         if frequency[color] > 0 and frequency[color] < min_count:
#             min_count = frequency[color]
#             min_color = color
    
#     return min_color

# # دریافت ورودی از کاربر
# n = int(input())  # تعداد ماژیک‌ها
# colors = list(map(int, input().split()))  # لیست رنگ‌ها

# # چاپ نتیجه
# print(find_least_frequent_color(n, colors))

def find_least_frequent_color(n,colors):
    frequency = [0] * 101
    for color in colors:
        frequency[color] += 1
    min_count = float('inf')
    min_color = -1
    for color in range(1,101):
        if frequency[color] > 0 and frequency[color] < min_count:
            min_count = frequency[color]
            min_color = color
    return min_color
n = int(input())
colors = list(map(int,input().split()))
print(find_least_frequent_color(n,colors))
