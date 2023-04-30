currentColor = (255, 0, 0)  # initial color is red
import random

def setup():
    size(400, 400)

def draw():
    background(55)
    fill(*currentColor)
    no_stroke()
    circle(width / 2, height / 2, 100)

def mouse_pressed():
    global currentColor
    currentColor = (random.randrange(255), random.randrange(255), random.randrange(255))

def mouse_released():
    pass  # do nothing when mouse is released