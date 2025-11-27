aufgaben = {"Montag": "Planung", "Dienstag": "Meetings", "Mittwoch": "Frei", "Donnerstag": "Frei", "Freitag": "Frei"}
eingabe = input("Eingabe: ")
drinnen = False

for tag in aufgaben:
    if tag.lower() == eingabe.lower():
        drinnen = True
        ergebnis = tag

if drinnen == True:
    print(aufgaben[ergebnis])
else:
    print("Felher")