import math
import random

def setup():
    size(400, 400)
    stroke(0)
    stroke_weight(2)
    no_fill()

def draw():
    background(255)
    translate(width/2, height/2)
    numsides=random.randrange(3, 9)
    draw_poly(numsides, 100)
    no_loop()

def draw_poly(num_sides, siz):
    angle = 360 / num_sides
    radius = siz / (2 * math.sin(math.radians(angle/2)))

    begin_shape()
    for i in range(num_sides):
        x = radius * math.cos(math.radians(angle * i))
        y = radius * math.sin(math.radians(angle * i))
        vertex(x, y)
    end_shape(CLOSE)
    
def mouse_pressed():
    redraw()