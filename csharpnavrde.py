def min_moves(n,m):
    pos = {
        1:(0,0),
        2:(0,1),
        3:(1,0),
        4:(1,1)
    }
    x1,y1 = pos[n]
    x2,y2 = pos[m]
    return abs(x1 - x2) + abs(y1 - y2)
n = int(input())
m = int(input())
print(min_moves(n,m))
