fachbegrife = {"h2O": "Die chemische Schreibweise für Wasser.", "O": "Das chemische Zeichen für Sauerstoff.", "H": "Das chemische Zeichen für Wasserstoff."}
eingabe = input("Bitte geben Sie ein chemisches Zeichen ein: ")
drinnen = False

for x in fachbegrife:
    if eingabe == x:
        drinnen = True

if drinnen == True:
    print(fachbegrife[x])
else:
    print("Begriff unbekannt")