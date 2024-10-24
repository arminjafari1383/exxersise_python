def find_character(position):
    if position == 1:
        return '1'
    
    # پیدا کردن طول نزدیکترین زیررشته‌ای که شامل position است
    length = 1
    while length < position:
        length = 2 * length
    
    if position <= length // 2:
        return find_character(position)
    else:
        return '0' if find_character(position - length // 2) == '1' else '1'

# ورودی
L, R = map(int, input().split())

# تولید خروجی از L تا R
result = ''.join(find_character(i) for i in range(L, R + 1))
print(result)


