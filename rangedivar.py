# # خواندن ورودی
# x, y = map(int, input().split())   # مختصات گوشه‌ی بالا چپ مربع
# r = int(input())                   # طول ضلع مربع
# dx, dy = map(int, input().split())  # مختصات ترکیدن لیوان

# # بررسی شرایط برای داخل یا روی مربع بودن
# if x <= dx <= x + r and y - r <= dy <= y:
#     print("Mahdi")  # لیوان داخل یا روی مربع ترکیده است
# else:
#     print("Parsa")  # لیوان بیرون مربع ترکیده است

x,y = map(int,input().split())
r = int(input())
dx,dy = map(int,input().split())
if x <= dx <= x + r and y - r <= dy <= y:
    print("Mahdi")
else:
    print("Parsa")
    