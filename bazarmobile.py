def count_good_phones(n, phones):
    bad_phones = set()  # Set to store indices of bad phones

    for i in range(n):
        for j in range(n):
            if i != j:  # Ensure we are not comparing the phone with itself
                if phones[i][0] >= phones[j][0] and phones[i][1] <= phones[j][1]:
                    bad_phones.add(i)  # Phone i is bad

    # Good phones are those not in bad_phones
    return n - len(bad_phones)

# Input processing
n = int(input())
phones = [tuple(map(int, input().split())) for _ in range(n)]

# Compute and print the result
print(count_good_phones(n, phones))
