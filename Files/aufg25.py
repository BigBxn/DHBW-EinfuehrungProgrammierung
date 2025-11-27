import csv
from collections import defaultdict

medien = defaultdict(list)

with open("medien.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")

    for name, typ, dauer, bewertung in reader:
        eintrag = {
            "name": name,
            "dauer": int(dauer),
            "bewertung": int(bewertung)
        }
        medien[typ].append(eintrag)

for typ, eintraege in medien.items():

    durchschnitt = sum(e["dauer"] for e in eintraege) / len(eintraege)

    bester = max(eintraege, key=lambda e: e["bewertung"])

    print(f"Durchschnittliche Dauer für {typ}: {durchschnitt:.1f} Minuten")
    print(f"Bester {typ}: {bester['name']} mit Bewertung {bester['bewertung']}")