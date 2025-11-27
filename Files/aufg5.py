wort = input("Was ist dein Wort? ")
wort.lower()

buchstabenliste = []

for x in wort:
    buchstabenliste.insert(0,x)

palindrom = ""
for x in buchstabenliste:
    palindrom += x

if palindrom == wort:
    print("Palindrom!")
else:
    print("kein Palindrom!")
