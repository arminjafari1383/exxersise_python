def unique_xor(n, sequence):
    # شمارش تکرار هر عدد در دنباله
    count = {}
    for num in sequence:
        count[num] = count.get(num, 0) + 1
    
    # یافتن اعداد یکتا
    unique_numbers = [num for num, freq in count.items() if freq == 1]
    
    # محاسبه‌ی XOR اعداد یکتا
    result = 0
    for num in unique_numbers:
        result ^= num
    
    return result


# دریافت ورودی از کاربر
n = int(input())
sequence = list(map(int, input().split()))


# چاپ خروجی
print(unique_xor(n, sequence))
 

