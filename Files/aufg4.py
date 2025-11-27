durchläufe = 0

zahlen_lsite = []

while durchläufe < 5:
    zahl = int(input("Was ist die Zahl? "))
    zahlen_lsite.append(zahl)
    durchläufe += 1
    print(zahlen_lsite)

gerade_liste = []
ungerade_liste = []

for x in zahlen_lsite:
    if x % 2 == 0:
        gerade_liste.append(x)
    else:
        ungerade_liste.append(x)

print(gerade_liste)
print(ungerade_liste)