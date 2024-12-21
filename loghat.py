from itertools import product

def find_last_character(n):
    # ایجاد لیست رشته‌ها تا زمانی که حداقل n رشته داشته باشیم
    strings = []
    length = 1
    while len(strings) < n:
        strings.extend([''.join(p) for p in product('ab', repeat=length)])
        length += 1
    
    # گرفتن رشته‌ی nام و چاپ آخرین کاراکتر آن
    nth_string = strings[n - 1]
    return nth_string[-1]

# ورودی گرفتن
n = int(input())
print(find_last_character(n))
