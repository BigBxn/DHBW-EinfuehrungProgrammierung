x = int(input("Welche Temperatur hat es gerade? "))

if x < 0:
    print("Es ist eisig!")
elif x > 0 and x <= 15:
    print("Es ist kühl!")
elif x > 15 and x <= 25:
    print("Es ist angenehm!")
else:
    print("Es ist warm!")