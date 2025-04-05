def encrypt_pes(input_string):
    # Count occurrences of each character (case insensitive)
    char_count = {}
    for char in input_string:
        lower_char = char.lower()
        char_count[lower_char] = char_count.get(lower_char, 0) + 1

    result = []
    for char in input_string:
        # Determine A_i
        if char.islower():
            A_i = ord(char) - ord('a')
        else:
            A_i = ord(char) - ord('A')

        # Determine X_i
        X_i = char_count[char.lower()]

        # Calculate y
        y = (X_i * A_i + 1) % 26

        # Determine the new character
        if char.islower():
            new_char = chr(ord('a') + y)
        else:
            new_char = chr(ord('A') + y)

        result.append(new_char)

    return ''.join(result)

# Input
input_string = input().strip()

# Encrypt and print the result
encrypted_string = encrypt_pes(input_string)
print(encrypted_string)