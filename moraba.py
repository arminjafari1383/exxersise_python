def jam_sum(n,k,a):
    sum_jam = sum(a)
    required_sum = (sum_jam -  k *(n))
    return required_sum

n,k = map(int,input("").split())
a = map(int,input("").split())
print(jam_sum(n,k,a))
