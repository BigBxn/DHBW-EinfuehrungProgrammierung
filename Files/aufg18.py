lieblingsfilme = {"Anna": "Star Wars Episode 3", "Beta": "Star Wars Episode 2", "Christina": "Star Wars Episode 1", "Drake": "Star Wars Episode 4"}
lieblingsessen = {"Anna": "Annanas", "Beta": "Blaubeeren", "Christina": "Chinesen", "Drake": "Drachenfrucht"}

for film in lieblingsfilme:
    for essen in lieblingsessen:
        if essen == film:
            print(f"{film} mag am liebsten den film {lieblingsfilme[film]} und isst am liebsten {lieblingsessen[essen]}")