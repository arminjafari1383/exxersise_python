user_input = input()
year, month,day = map(int,user_input.split('/'))
if month < 7:
    month = month - 1
    month = month * 31    
    total = day + month
    final = (365 - total) + 1
    print(final)
elif month >= 7 and month <= 11:
    month = month - 7
    month = 186 + month * 30
    final = 365 - month
    day = final - day + 1
    print(day)
else:
    day = 29 - day
    print(day)
