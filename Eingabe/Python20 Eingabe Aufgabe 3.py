from daten import woerterbuch
from random import randint

words = []

# Bei jedem Schleifendurchlauf wird der Variablen schluessel ein ein Key aus Wörterbuch zugewiesen.
for schluessel in woerterbuch.keys():
    words.append(schluessel)


while True:
    # Bei jedem Schleifendurchlauf wird i ein zufällig gewählter Key des Eörterbuchs zugewiesen.
    i = randint(0, len(woerterbuch.keys()) - 1)
    eingabe = input(f"Was heißt {words[i]}").lower()
    # Die Schleife wird wiederholr, bis sie mit break unterbrochen wird.
    if eingabe == "ende":
        break
    elif eingabe == woerterbuch[words[i]]:
        print("Das ist richtig.")
    elif eingabe != woerterbuch[words[i]]:
        print("Das ist falsch.")