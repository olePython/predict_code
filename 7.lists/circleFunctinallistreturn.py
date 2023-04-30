import random


def setup():
    size(400, 400)
    no_loop()


def draw():
    background(255)
    circle_x, circle_y, circle_r, circle_c = update_circle_state()
    draw_circle(circle_x, circle_y, circle_r, circle_c)


def draw_circle(x, y, r, c):
    stroke(c)
    fill(c)
    ellipse(x, y, r, r)


def update_circle_state():
    circle_x = 100
    circle_y = 100
    circle_r = int(random.uniform(20, 100))
    circle_c = color(
        random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)
    )
    circle_x += random.uniform(-50, 50)
    circle_y += random.uniform(-50, 50)
    return [circle_x, circle_y, circle_r, circle_c]


def mouse_pressed():
    redraw()
