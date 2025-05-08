lista = []
listb = []

for i in range(5):
    x = input()
    lista.append(x)

for index, value in enumerate(lista):
    if "FBI" in value:
        listb.append(index)

if listb:
    for k in listb:
        print(k + 1, end=' ')  # اضافه کردن 1 چون معمولاً ایندکس از 1 خواسته میشه
else:
    print("HE GOT AWAY!")

