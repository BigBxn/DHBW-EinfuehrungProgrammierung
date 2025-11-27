def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def minutes_to_hours(min):
    return min / 60

print("Einheiten-Umrechner")
print("1: km → miles")
print("2: °C → °F")
print("3: Minuten → Stunden")

wahl = input("Bitte eine Option wählen (1-3): ")

if wahl == "1":
    km = float(input("Kilometer: "))
    miles = km_to_miles(km)
    print(f"{km} km sind {miles:.2f} miles.")
elif wahl == "2":
    c = float(input("Grad Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C sind {f:.2f}°F.")
elif wahl == "3":
    min = float(input("Minuten: "))
    stunden = minutes_to_hours(min)
    print(f"{min} Minuten sind {stunden:.2f} Stunden.")
else:
    print("Ungültige Auswahl.")
