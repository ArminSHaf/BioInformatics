S = "ACGTTGCATTACGTTGCAGT"

for letter in sorted(set(S)):
    count = S.count(letter)
    print(f"{letter}: {count}")

print("\nrelatiev probability : \n")

for letter in sorted(set(S)):
    count = S.count(letter)
    print(f"{letter}: {count/len(S)}")
