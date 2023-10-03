from turtle import *
from definitionen import *

def interpretiere_eingabe(x, y):
    if (x >= 150 and x <= 170 and y >= -190 and y <= -170):
        nach_unten_ausrichten()
    elif (x >= 170 and x <= 190 and y >= -170 and y <= -150):
        nach_rechts_ausrichten()
    elif (x >= 130 and x <= 150 and y >= -170 and y <= -150):
        nach_links_ausrichten()
    elif (x >= 150 and x <= 170 and y >= -150 and y <= -130):
        nach_oben_ausrichten()

onclick(interpretiere_eingabe)
