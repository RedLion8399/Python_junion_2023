from turtle import *
from definitionen import *

def kopf_bewegen():
    if kopf.direction == "down":
        y = kopf.ycor()
        kopf.sety(y - 20)

    elif kopf.direction == "right":
        x = kopf.xcor()
        kopf.setx(x + 20)
    
    elif kopf.direction == "up":
        y = kopf.ycor()
        kopf.sety(y + 20)
        
    
    elif kopf.direction == "left":
        x = kopf.xcor()
        kopf.setx(x - 20)
        