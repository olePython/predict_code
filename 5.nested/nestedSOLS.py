def setup():
    size(500, 500)
    no_fill()
    stroke(0)
    stroke_weight(3)
    translate(10, 50)

    # 1_____
    for y in range(20, 200, 10):
        for x in range(20, y, 10):
            line(x, y, x - 10, y - 10)

    # 2_____
    for x in range(20, 200, 20):
        for y in range(20, x, 20):
            line(x, y, x + 20, y + 20)

    # 3_____
    for y in range(10, 200, 20):
        for x in range(10, y, 20):
            line(x, y, x + 10, y + 10)
            line(x + 10, y, x, y + 10)

    # 4_____
    for y in range(10, 200, 10):
        for x in range(10, 100, 10):
            ellipse(x, y, 10, 10)

    # 5_____
    for y in range(0, 100, 20):
        for x in range(0, 100, 20):
            ellipse(x, y, 10, 10)


def draw():
    pass


