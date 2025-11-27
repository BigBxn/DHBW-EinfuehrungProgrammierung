import datetime

eingabe = input("Eingabe: ")
date = datetime.date.today()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
time = str(hour) + ":" + str(minute)

with open('aufg19.txt', 'a') as writer:
    writer.writelines(str(date) + " " + str(time) + " - " + str(eingabe) + "\n")