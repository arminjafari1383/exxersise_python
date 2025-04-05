# def is_divisible_by_6(three_digit_number):
#     num = three_digit_number[0] * 100 + three_digit_number[1] * 10 + three_digit_number[2]
#     return num % 6 == 0

# def rotate(lst, shift):
#     n = len(lst)
#     return lst[shift:] + lst[:shift]

# def can_unlock_lock(top_disk, bottom_disk):
#     for top_shift in range(5):
#         rotated_top = rotate(top_disk, top_shift)
#         for bottom_shift in range(5):
#             rotated_bottom = rotate(bottom_disk, bottom_shift)
            
#             # Compute the digit-wise sum and take only the last digit
#             summed_digits = [((rotated_top[i] + rotated_bottom[i]) % 10) for i in range(1, 4)]
            
#             if is_divisible_by_6(summed_digits):
#                 return "Boro joloo :)"
#     return "Gir oftadi :("

# # Read input
# top_disk = list(map(int, input().split()))
# bottom_disk = list(map(int, input().split()))

# # Check if we can unlock the lock
# print(can_unlock_lock(top_disk, bottom_disk))

def is_divisible_by_6(three_digit_number):
    num = three_digit_number[0] * 100 + three_digit_number[1] * 10 + three_digit_number[2]
    return num % 6 == 0

def rotate(lst,shift):
    n = len(lst)
    return lst[shift:] + lst[:shift]

def can_unlock_lock(top_disk, bottom_disk):
    for top_shift in range(5):
        rotated_top = rotate(top_disk,top_shift)
        for bottom_shift in range(5):
            rotated_bottom = rotate(bottom_disk,bottom_shift)
            summed_digits = [((rotated_top[i] + rotated_bottom[i])% 10) for i in range(1,4)]
            if is_divisible_by_6(summed_digits):
                return "Boro joloo :)"
    return "Gir oftadi :("
top_disk = list(map(int,input().split()))
bottom_disk = list(map(int,input().split()))
print(can_unlock_lock(top_disk,bottom_disk))
