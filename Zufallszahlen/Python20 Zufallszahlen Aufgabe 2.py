from random import *

def teste(a, b):
    counter = 0
    # Bei jedem Schleifendurchlauf wird x ein intiger zugewiesen, der zwischen 1 und a liebt. 
    for i in range(b):
        x = randint(1, a)
        # Wenn der Zufallswert 1 ist, wird die Zählervariable um 1 erhöht.
        if x == 1:
            counter += 1
    print(counter)
    
# Die funtion wird mit den geforderten Parematern aufgerufen.
teste(4, 200)