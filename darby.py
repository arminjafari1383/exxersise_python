l = []
t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    perspolis_total = a + c 
    estaghal_total = b + d
    
    if perspolis_total > estaghal_total:
        l.append("perspolis")
    elif estaghal_total > perspolis_total:
        l.append("esteghlal")
    else:
        if c > b:
            l.append("perspolis")
        elif b > c:
            l.append("esteghlal")
        else:
            l.append("penalty")

for lp in l:
    print(lp)
