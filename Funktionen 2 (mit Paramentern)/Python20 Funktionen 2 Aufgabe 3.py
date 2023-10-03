from daten import punkte_liste
from turtle import *

def gehe_wenn_nah(punkt):
    if distance(punkt) < 100:
        goto(punkt)
    else:
        goto(0, 0)

# Bei jedem Schleifendurchlauf wird point ein Werd aus der Liste Punkteliste zugewiesen.
for point in punkte_liste:
    gehe_wenn_nah(point)