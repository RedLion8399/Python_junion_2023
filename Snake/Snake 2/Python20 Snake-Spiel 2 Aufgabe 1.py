from random import *
from turtle import *
from definitionen import *

segmente = []
def checke_kollision_mit_essen():
    if kopf.distance(essen) < 20:
        while True:
            new_x_pos = randint(-9, 9) * 20
            new_y_pos = randint(-9, 9) * 20
            if new_x_pos > -160 or new_y_pos > -140:
                essen.goto(new_x_pos, new_y_pos)
                
                neues_segment = Turtle()
                neues_segment.shape("square")
                neues_segment.color("yellow")
                neues_segment.speed(0)
                neues_segment.penup()
                neues_segment.goto(0, 0)
                segmente.append(neues_segment)
                break