def count_possible_words(word):
    total_possibilities = 1
    for letter in word:
        if letter == 'K':
            total_possibilities *= 4  # K can be K or T
        elif letter == 'G':
            total_possibilities *= 2  # G can be G or D
        elif letter == 'R':
            total_possibilities *= 3  # R can be R, L, or F
        else:
            total_possibilities *= 1  # No change for other letters
    return total_possibilities

# ورودی را دریافت می‌کنیم
word = input().strip()

# نتیجه را محاسبه و چاپ می‌کنیم
print(count_possible_words(word))