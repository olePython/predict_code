x = 0
y = 0


def setup():
    size(400, 400)
    no_fill()
    stroke(255, 0, 0)
    stroke_weight(5)


def draw():
    global x, y
    background(55)
    translate(width / 2, height / 2)
    ellipse(x, y, 200, 200)
    no_loop()
