# def fix_sentence(s):
#     result = []
    
#     for char in s:
#         if char == '=':
#             if result:  # اگر رشته خالی نباشد
#                 result.pop()  # آخرین حرف را حذف کن
#         else:
#             result.append(char)  # حرف را به رشته اضافه کن
    
#     return ''.join(result)

# # دریافت ورودی
# s = input()

# # چاپ خروجی
# print(fix_sentence(s))

def fix_sentence(s):
    result = []
    for char in s:
        if char == '=':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)
s = input()
print(fix_sentence(s))

