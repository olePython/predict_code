import random

def setup():
    size(400, 400)

def draw():
    background(55)
    fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ellipse(width/2, height/2, 100, 100)
    no_loop()

def mouse_pressed():
    redraw()