liste = input("Liste: ")
liste2 = liste.split(",")
liste3 = []

for x in liste2:
    if x not in liste3:
        (liste3.append(x))

print(liste2)
print(liste3)