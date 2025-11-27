import random

anzahl_kurze_aufgaben = int(input("Wie viele kurze Aufgaben sollen maximal verteilt werden? "))
anzahl_mittlere_aufgaben = int(input("Wie viele mittlere Aufgaben sollen maximal verteilt werden? "))
anzahl_pausen_aktivitäten = int(input("Wie viele pausen Aktivitäten sollen maximal verteilt werden? "))
kurze_aufgaben = ["Zähne putzen", "duschen", "Hunde Napf tauschen", "Kühlschrank auffüllen", "Spühlmaschine ausräumen"]
mittlere_aufgaben = ["gassi gehen", "kochen", "gym gehen", "Rasen mähen"]
pausen_aktivitäten = ["dehnen", "Kaffe trinken", "rauchen", "tiktok scrollen"]
anzahl_kurze_durchläufe = random.randint(0, anzahl_kurze_aufgaben - 1)
anzahl_mittlere_durchläufe = random.randint(0, anzahl_mittlere_aufgaben - 1)
anzahl_pausen_durchläufe = random.randint(0, anzahl_pausen_aktivitäten - 1)
kurze_durchläufe = 0
mittlere_durchläufe = 0
pausen_durchläufe = 0

print("Deine kurzen Aufgaben für den heutigen Tag sind: ")
while kurze_durchläufe <= anzahl_kurze_durchläufe:
    kurze_durchläufe += 1
    auswahl = random.randint(0, len(kurze_aufgaben) - 1)
    print(str(kurze_durchläufe) + ". " + kurze_aufgaben[auswahl])
    kurze_aufgaben.remove(kurze_aufgaben[auswahl])

print("\nDeine mittleren Aufgaben für den heutigen Tag sind: ")
while mittlere_durchläufe <= anzahl_mittlere_durchläufe:
    mittlere_durchläufe += 1
    auswahl = random.randint(0, len(mittlere_aufgaben) - 1)
    print(str(mittlere_durchläufe) + ". " + mittlere_aufgaben[auswahl])
    mittlere_aufgaben.remove(mittlere_aufgaben[auswahl])

print("\nDeine pausen Aktivitäten für den heutigen Tag sind: ")
while pausen_durchläufe <= anzahl_pausen_durchläufe:
    pausen_durchläufe += 1
    auswahl = random.randint(0, len(pausen_aktivitäten) - 1)
    print(str(pausen_durchläufe) + ". " + pausen_aktivitäten[auswahl])
    pausen_aktivitäten.remove(pausen_aktivitäten[auswahl])