eingabe = input("Eingabe: ")
verbotenes_wort = "Aalen"


with open(eingabe, 'r') as reader:
    for line in reader.readlines():
        if line.strip() != verbotenes_wort:
            with open('aufg22(2).txt', 'a') as writer:
                writer.write(line)