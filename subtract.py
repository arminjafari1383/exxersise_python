# def Kam(a):
#     for i in len(int(range(a))):
#         b = a // 10
#         print(b)

# k = int(input())
# print(Kam(k))
def game(number):
    b = number % 10
    c = number // 10
    if b > c:
        d = b - c
        return(d)
    else:
        d = c -b
        return(d)
    
print(game(17))
