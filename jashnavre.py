# # دریافت ورودی
# n = int(input().strip())

# # یافتن بزرگترین مقسوم علیه n که بیشتر از 1 است
# for i in range(n // 2, 0, -1):
#       if n % i == 0:
#         print(i)
#         break


n = int(input().strip())
for i in range(n // 2,0,-1):
    if n % i == 0:
        print(i)
        break
    