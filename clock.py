# def mirror_clock(a, b):
#     # محاسبه‌ی مکان واقعی عقربه‌ی ساعت شمار
#     real_hour = 12 - a if a != 0 else 12
#     # محاسبه‌ی مکان واقعی عقربه‌ی دقیقه شمار
#     real_minute = 60 - b if b != 0 else 0
    
#     # اگر دقیقه 60 شد، ساعت را یک واحد افزایش می‌دهیم
#     if real_minute == 60:
#         real_minute = 0
#         real_hour += 1
#         if real_hour == 13:
#             real_hour = 1
    
#     # تبدیل ساعت و دقیقه به فرمت hh:mm
#     return f"{real_hour:02}:{real_minute:02}"

# # مثال
# a , b = map(int,input().split())
# print(mirror_clock(a, b))  # خروجی: 09:45



# def mirror_clock(a,b):
#     real_hour = 12 - a if a != 0 else 12 
#     real_minute = 60 - b if b != 0 else 0
#     if real_minute == 60:
#         real_minute = 0
#         real_hour += 1
#         if real_hour == 13:
#             real_hour = 1
#     if real_hour == 12:
#         real_hour = 12
#         real_hour_new = real_hour - 12
#         return  f"{real_hour_new:02}:{real_minute:02}"
#     return f"{real_hour:02}:{real_minute:02}"

# a,b= map(int,input().split())
# print(mirror_clock(a,b))






def Clock(a,b):
    hour_real = 12 - a  if  a != 0 else 12
    real_minute = 60 - b if b != 0 else 0
    if real_minute == 60:
        real_minute = 0
        hour_real += 1
        if hour_real == 13:
            hour_real = 1
    if hour_real == 12:
        hour_real = 12
        hour_real_new = hour_real - 12
        return f"{hour_real_new:02}:{real_minute:02}"
    return f"{hour_real:02}:{real_minute:02}"

a,b = map(int,input().split())
print(Clock(a,b))