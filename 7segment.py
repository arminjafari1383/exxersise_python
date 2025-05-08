seg = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,
       '6':6,'7':3,'8':7,'9':6}

s = input().strip()
mant, exp = s.split('e')
b = int(exp)

# جداسازی بخش صحیح و اعشاری
if '.' in mant:
    X, Y = mant.split('.')
    L = len(Y)
    D = X + Y
else:
    D = mant
    L = 0

zeros = b - L   # تعداد صفرهای انتهایی
# جمع سگمنت‌های D و صفرهای الحاقی
ans = sum(seg[c] for c in D) + zeros * seg['0']
print(ans)

