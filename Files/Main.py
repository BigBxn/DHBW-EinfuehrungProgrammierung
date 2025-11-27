import aufg2

bodyweight = float(input("Wie schwer bist du? "))
liter = aufg2.trinken(bodyweight)
print("Du musst " + str(liter.__round__(2)) + "l am Tag trinken!")