def find_pythagorean_triplet(n):
    for a in range(1, n // 2):
        for b in range(a, (n - a) // 2):  # b ≥ a و b < n/2
            c = n - a - b
            if a * a + b * b == c * c:
                return f"{a} {b} {c}"
    return "Impossible"


# گرفتن ورودی
n = int(input().strip())
print(find_pythagorean_triplet(n))