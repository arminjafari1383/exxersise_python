t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    score_c = 0
    score_q = 0
    for ch in s:
        if ch == 'C':
            score_c += 1
        else: 
            score_q += 1
        if score_c == 25:
            print("CodeCup")
        if score_q == 25:
            print("Quera")
            break