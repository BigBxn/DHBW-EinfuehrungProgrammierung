stop = False
zahlen_liste = []

while(stop == False):
    eingabe = input("Bitte geben Sie eine Zahl oder ,,Stop'' ein: ")
    if eingabe.isdigit():
        zahlen_liste.append(int(eingabe))
    elif eingabe == "Stop" or eingabe == "":
        stop = True
    else:
        print("Bitte geben Sie eine Zahl oder ,,Stop'' ein.")

summe = 0
schnittzahl = 0
kleinste_zahl = zahlen_liste[0]
groeßte_zahl = 0


for zahl in zahlen_liste:
    summe += zahl
    schnittzahl += 1
    if zahl > groeßte_zahl:
        groeßte_zahl = zahl
    if kleinste_zahl > zahl:
        kleinste_zahl = zahl

print(f"Die Summe ist: {summe}")
schnitt = summe / schnittzahl
print(f"Der Durschnitt ist: {schnitt}")
print(f"Die größte Zahl ist: {groeßte_zahl}")
print(f"Die kleinste Zahl ist: {kleinste_zahl}")