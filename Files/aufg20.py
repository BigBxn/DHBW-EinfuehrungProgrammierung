
anzahl = 0

with open('aufg20.txt', 'r') as reader:
    for zeilen in reader.readlines():
        anzahl += 1

print(anzahl)