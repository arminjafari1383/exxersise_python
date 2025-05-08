hex_number = input().strip()
decimal_number = int(hex_number,16)
decimal_number += 1
print(hex(decimal_number)[2:].upper())
