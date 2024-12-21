def calculate_rest_time(W,S,I):
    total_work = W + S - I
    R = 24 - total_work
    return R
W,S,I = map(int,input().split())
rest_time = calculate_rest_time(W,S,I)
print(rest_time)
