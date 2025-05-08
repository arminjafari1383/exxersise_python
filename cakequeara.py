x = int(input())
if x <= 12:
    if 3 // x == 1:
        print("YES")
    elif x > 3 and x % 3 != 0:
        print("NO")
    elif x < 3 and x % 3 == 0:
        print("YES")
    else:
        print("YES")
else:
    print("out of range")
    