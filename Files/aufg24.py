import random

aktivitaeten = [
    ("Lesen", 30),
    ("Sport", 45),
    ("Spazierengehen", 20),
]

try:
    verfuegbare_zeit = int(input("Wie viel Zeit hast du (in Minuten)? "))
except ValueError:
    print("Bitte eine gültige Zahl eingeben.")
    exit()

passende_aktivitaeten = [a for a in aktivitaeten if a[1] <= verfuegbare_zeit]

if passende_aktivitaeten:
    aktivitaet = random.choice(passende_aktivitaeten)
    print(f"Vorschlag: {aktivitaet[0]} (Dauer: {aktivitaet[1]} Minuten)")
else:
    print("Leider passt keine Aktivität in deine verfügbare Zeit.")
