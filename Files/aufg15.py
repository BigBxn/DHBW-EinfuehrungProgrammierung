eingabe = input("Eingabe: ")
liste = {}

for buchstabe in eingabe:
    if buchstabe in liste:
        liste[buchstabe] += 1
    else:
        liste[buchstabe] = 1

print(liste)