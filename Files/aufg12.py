zahl1 = int(input("Geben Sie die erste Zahl ein:"))
zahl2 = int(input("Geben Sie die zweite Zahl ein:"))
runthrough = 1
Alpha = False
Beta = False

while runthrough < 100:
    alpha = runthrough % zahl1
    if alpha == 0:
        Alpha = True
    beta = runthrough % zahl2
    if beta == 0:
        Beta = True
    if Alpha == True and Beta == True:
        print("Alphabeta")
    elif Alpha == True and Beta == False:
        print("Alpha")
    elif Alpha == False and Beta == True:
        print("Beta")
    else:
        print(runthrough)
    runthrough += 1
    Alpha = False
    Beta = False