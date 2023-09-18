import random

def setup():
    size(400, 400)

def draw():  # runs at 60 frames/second
    background(200)  # color

    translate(width / 2, height / 2)  # move the origin to the center of the canvas
    radius = 10  # starting radius of the spiral
    angle = 0  # starting angle

    for i in range(1000):  # loop 1000 times
        x = radius * cos(angle)  # compute x-coordinate
        y = radius * sin(angle)  # compute y-coordinate
        fill(random.random() * i, 0, 0)  # random red
        ellipse(x, y, 10, 10)  # draw a circle at (x, y)
        radius += 0.09  # increase radius
        angle += 0.08  # increase angle

    no_loop()  # stops drawing
