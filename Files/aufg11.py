zahl = int(input("Bitte geben Sie eine Zahl ein: "))
zahl = zahl + 1

for i in range(zahl):
    if i == 0:
        continue
    for j in range(zahl):
        if j == 0:
            continue
        rechnung = i*j
        print(f"{i} x {j} = {rechnung}")