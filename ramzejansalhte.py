# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def generate_strong_primes(n):
#     results = []

#     def dfs(current):
#         if len(str(current)) == n:
#             results.append(current)
#             return
#         for digit in range(10):
#             next_num = current * 10 + digit
#             if is_prime(next_num):
#                 dfs(next_num)

#     for start in [2, 3, 5, 7]:
#         dfs(start)

#     results.sort()
#     return results

# # خواندن ورودی
# N = int(input())
# res = generate_strong_primes(N)
# for num in res:
#     print(num)









def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
    return True

def generate_strong_primes(n):
    results = []
    def dfs(current):
        if len(str(current)) == n:
            results.append(current)
            return
        for digit in range(10):
            next_num = current * 10 + digit
            if is_prime(next_num):
                dfs(next_num)
    for start in [2,3,5,7]:
        dfs(start)
    results.sort()
    return results
N = int(input())
res = generate_strong_primes(N)
for num in res:
    print(num)
    