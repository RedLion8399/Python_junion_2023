from turtle import *
from definitionen import *

def koerper_bewegen():
    for index in range(len(segmente) - 1, 0, -1):
        segmente[index].goto(segmente[index - 1].position())
    if len(segmente) != 0:
        segmente[0].goto(kopf.position())