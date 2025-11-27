dinge = []

print("Gib Dinge ein, die du bewerten möchtest (Restaurant, Spiel, Serie, ...).")
print("Drücke einfach ENTER, um die Eingabe zu beenden.\n")

while True:
    name = input("Name des Dings (ENTER zum Beenden): ").strip()
    if name == "":
        break

    while True:
        try:
            bewertung = int(input(f"Bewertung für '{name}' (1-10): "))
            if 1 <= bewertung <= 10:
                break
            else:
                print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    dinge.append((name, bewertung))

dinge_sortiert = sorted(dinge, key=lambda x: x[1], reverse=True)

print("\n--- Rangliste ---")
for platz, (name, bewertung) in enumerate(dinge_sortiert, start=1):
    print(f"{platz}. {name} – Bewertung: {bewertung}")
