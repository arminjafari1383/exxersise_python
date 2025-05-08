import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [input().rstrip() for _ in range(n)]

ans = 0

# ۱) شمارش زنجيره‌هاي متوالي '|' در هر سطر
for i in range(n):
    prev = '.'  # نشانهٔ شروع يا كاراكتر غير '|' 
    for j in range(m):
        c = A[i][j]
        if c == '|' and prev != '|':
            ans += 1
        prev = c

# ۲) شمارش زنجيره‌هاي متوالي '-' در هر ستون
for j in range(m):
    prev = '.' 
    for i in range(n):
        c = A[i][j]
        if c == '-' and prev != '-':
            ans += 1
        prev = c

print(ans)
