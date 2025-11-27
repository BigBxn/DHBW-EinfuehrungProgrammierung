import random

liste = [0, 0, 0, 0, 0, 0]
addednumber = False

for x in range(len(liste)):
    while (addednumber == False):
        random_zahl = random.randint(1, 49)
        if not liste.__contains__(random_zahl):
            liste[x] = random_zahl
            addednumber = True
    addednumber = False

print(liste)