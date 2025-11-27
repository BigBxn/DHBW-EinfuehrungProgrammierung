x = ""
with open('aufg21.txt', 'r') as reader:
    for zeilen in reader.readlines():
        if zeilen[1] == " ":
            x = zeilen[4:]
            with open('aufg21(2).txt', 'a') as writer:
                writer.write(x)
with open('aufg21(2).txt', 'a') as writer:
    writer.write("\n")