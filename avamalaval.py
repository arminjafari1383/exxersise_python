n = int(input())
factors = []

i = 2
while i * i <= n:
    count = 0
    while n % i == 0:
        n //= i
        count += 1
    if count > 0:
        if count == 1:
            factors.append(f"{i}")
        else:
            factors.append(f"{i}^{count}")
    i += 1

if n > 1:
    factors.append(f"{n}")

print("*".join(factors))
