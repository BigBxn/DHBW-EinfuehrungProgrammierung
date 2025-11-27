punkte = int(input("Was ist deine Punktzahl? "))

note = 0

if punkte <= 29:
    note = 6
elif punkte > 29 and punkte <= 49:
    note = 5
elif punkte > 49 and punkte <= 64:
    note = 4
elif punkte > 64 and punkte <= 79:
    note = 3
elif punkte > 79 and punkte <= 89:
    note = 2
elif punkte > 89 and punkte <= 100:
    note = 1
else:
    print("Das kann nicht sein!")

print("Deine note ist: " + str(note))