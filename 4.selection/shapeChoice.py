def setup():
    size(400, 400)
    no_loop()


def draw():
    background(55)
    translate(width / 2, height / 2)
    draw_shape(0, 0, 70, color(255, 0, 0))


def draw_shape(x, y, r, c):
    stroke(c)
    fill(c)
    shape_choice = int(random(3))  # randomly choose between 3 shapes
    if shape_choice == 0:
        ellipse(x, y, r, r)
    elif shape_choice == 1:
        rect(x, y, r, r)
    else:
        triangle(x, y - r / 2, x - r / 2, y + r / 2, x + r / 2, y + r / 2)


def mouse_pressed():
    redraw()
