def setup():
    size(400, 400)
    rect_mode(CENTER)


def draw():
    background(255)
    for i in range(width, 0, -40):
        fill(i)
        rect(width / 2, height / 2, i, i)
