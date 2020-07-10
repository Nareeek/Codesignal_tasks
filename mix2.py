white = []
black = []
letters = "ABCDEFGH"
digits = "12345678"

i = 0
j = 0

while j < 8:
    while i < 8:
        black.append(letters[i] + digits[j])
        i += 1
        j += 1
        black.append(letters[i] + digits[j])
        i += 1
        j -= 1
    j += 2
    i = 0

print(black)
