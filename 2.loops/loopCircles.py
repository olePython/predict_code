import random

def setup():
    size(400, 400)
    no_loop()

def draw():
    background(255)
    for i in range(10):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(20, 100)
        c = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_circle(x, y, r, c)

def draw_circle(x, y, r, c):
    stroke(c)
    fill(c)
    ellipse(x, y, r, r)

def mouse_pressed():
    redraw()
