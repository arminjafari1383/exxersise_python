s,f,l,x = map(int,input().split())
if x < s :
    print("exam did not started!")
elif x >= f:
    print("exam finished!")
else:
    remaining_time = min(f - x,l)
    print(remaining_time)
