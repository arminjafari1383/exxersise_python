def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # مجموعه حروف صدادار
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# گرفتن ورودی
s = input().strip()
print(count_vowels(s))
