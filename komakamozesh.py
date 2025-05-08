# n = int(input())
# key_to_lamp = list(map(int,input().split()))
# lamp_status = list(map(int,input().split()))
# key_to_press = set()
# for lamp_index in range(n):
#     if lamp_status[lamp_index] == 1:
#         key_number = key_to_lamp[lamp_index]
#         key_to_press.add(key_number)
# print(" ".join(map(str, sorted(key_to_press))))

n = int(input())
key_to_lamp = list(map(int,input().split()))
lamp_status = list(map(int,input().split()))
key_to_press = set()
for lamp_index in range(n):
    if lamp_status[lamp_index] == 1:
        key_number = key_to_lamp[lamp_index]
        key_to_press.add(key_number)
print(" ".join(map(str,sorted(key_to_press))))