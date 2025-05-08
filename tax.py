list1 = []
while True:
    income = int(input())
    if income == 0:
        break
    if income <= 1000000:
        net_income = income
        list1.append(net_income)
    elif income <= 5000000:
        net_income = income - int(income * 0.1)
        list1.append(net_income)
    else:
        net_income = income - int(income * 0.2)
        list1.append(net_income)

m = len(list1)
for i in range(m):
    print(list1[i])
    
