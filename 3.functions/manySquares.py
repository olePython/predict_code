import random


def setup():
    size(400, 400)
    color_mode(HSB, 360, 100, 100)


def draw():
    background(55)

    for i in range(5):
        x = random.randint(0, width - 100)
        y = random.randint(0, height - 100)
        w = random.randint(50, 100)
        h = random.randint(50, 100)
        col = color(
            random.randint(60, 360), random.randint(60, 100), random.randint(60, 100)
        )
        draw_rect(x, y, w, h, col)
        no_loop()


def draw_rect(x, y, w, h, color):
    fill(color)
    no_stroke()
    rect(x, y, w, h)


def mouse_pressed():
    redraw()
