input = input("Was ist dein Satz? ")
input = input.lower()

vokale = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for x in input:
    for y in vokale:
        if x == y:
            vokale[y] = vokale[y] + 1

print(vokale)