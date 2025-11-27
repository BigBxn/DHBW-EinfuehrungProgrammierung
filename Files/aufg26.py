ziele = []

with open("ziele.txt", "r") as reader:
    for line in reader:
        name, geplant, einheit = line.strip().split(";")
        ziele.append((name, float(geplant), einheit))

print("\nBitte gib an, wie viel du diese Woche erreicht hast:\n")

for name, geplant, einheit in ziele:
    while True:
        try:
            tatsaechlich = float(input(f"{name} (geplant {geplant} {einheit}): "))
            break
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    prozent = (tatsaechlich / geplant) * 100
    print(f"{name}: {tatsaechlich}/{geplant} {einheit} = {prozent:.1f}%")

