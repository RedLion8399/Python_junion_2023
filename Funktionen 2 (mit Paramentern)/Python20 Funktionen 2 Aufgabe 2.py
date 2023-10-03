from daten import liste, buchstabe, anzahl

def stadt_mit(Staedte, letter, number):
    data = []
    # Bei jedem Schleifendurchlauf wird der Variable Stadt ein Element aus Staedte zugewiesen, welches auf die Bedingungen geprüft wird.
    for Stadt in Staedte:
        if (len(Stadt) <= number) and Stadt[0] == letter:
            data.append(Stadt)
    return(data)

# Die Funktion wird mit den in Zeile 1 importierten Parametern aufgerufen
print(stadt_mit(liste, buchstabe, anzahl))