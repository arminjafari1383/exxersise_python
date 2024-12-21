# def display_exhibition(k):
#     # تعداد ردیف‌ها و ساختار دیوارها
#     wall = "########.......########"
#     row_template = "#{}.......{}#"
#     empty_space = " " * 13  # فضای خالی برای غرفه‌های خالی

#     # نمایش نمایشگاه
#     print(wall)  # دیوار بالایی
#     for i in range(0, 8, 2):  # هر بار دو غرفه را در یک بخش چاپ می‌کنیم
#         ghorfe_left = f"ghorfe{i + 1}" if i + 1 <= k else empty_space
#         ghorfe_right = f"ghorfe{i + 2}" if i + 2 <= k else empty_space
#         print(row_template.format(ghorfe_left.ljust(13), ghorfe_right.ljust(13)))
#         print(wall)

# # دریافت ورودی و نمایش نقشه نمایشگاه
# k = int(input("تعداد غرفه‌ها: "))
# display_exhibition(k)

def display_exibition(k):
    wall = "######.......######"
    row_template = "#{}.......{}#"
    empty_space = " " * 13
    print(wall)
    for i in range(0,8,2):
        ghorfe_left = f"ghorfe{i + 1}" if i + 1 <= k else empty_space
        ghorfe_right = f"ghorfe{i + 2}" if i +2 <= k else empty_space
        print(row_template.format(ghorfe_left.ljust(13),ghorfe_right.ljust(13)))
        print(wall)

k = int(input(""))
display_exibition(k)