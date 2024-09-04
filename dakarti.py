def determine_direction(x, y, x1, y1):
    # محاسبه ضرب برداری
    cross_product = (x1 - x)
    
    if cross_product > 0:
        print("Right")
    else:
        print("Left")

# خواندن ورودی
x, y = map(int, input().split())
x1, y1 = map(int, input().split())

determine_direction(x, y, x1, y1)