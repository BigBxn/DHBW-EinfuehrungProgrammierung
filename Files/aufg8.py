satz = input("Satz: ")
länge = int(input("Länge: "))
wörter = satz.split(" ")
ausgw = 0

for x in wörter:
    if len(x) > länge:
        print(f"Das Wort ,,{x}'' ist länger als die Angegebene Länge von {länge}")
        ausgw += 1

if(ausgw == 0):
    print(f"Es konnten leider keine Wörter gefunden werden die größer sind als die angegebene Länge von {länge}.")