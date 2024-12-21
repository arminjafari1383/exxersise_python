# Input processing
a, b, c, d, m = map(int, input().split())

# Calculate final prices after m months
final_price_red = a + m * c
final_price_green = b + m * d

# Determine which elixir has the higher final price
if final_price_red > final_price_green:
    chosen_price = final_price_red
    initial_price = a
else:
    chosen_price = final_price_green
    initial_price = b

# Check if the profit per bottle is higher
if chosen_price > initial_price:
    print("Eyval baba!")
else:
    print("Naaa, eshtebahe!")
