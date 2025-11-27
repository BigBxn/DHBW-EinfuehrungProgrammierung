vorname = input("Was ist dein Vorname? ")
name = input("Was ist dein Name? ")
titel = input("Was ist dein Titel? ")

if titel == "":
    print(f"{name}, {vorname}")
    print(f"{vorname} {name}")
else:
    print(f"{name}, {vorname} {titel}")
    print(f"{titel} {vorname} {name}")