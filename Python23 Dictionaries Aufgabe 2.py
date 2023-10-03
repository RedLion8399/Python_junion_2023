from daten import woerterbuch, satz

englisch = satz.split()
deutsch = []

# Jedes wort des gesplitteten stzes wird im dictionary nachgeschlagen und der zugehörige Value in der Lisre deutsch gespeichert. 
for word in englisch:
    deutsch.append(woerterbuch[word])
print(deutsch)