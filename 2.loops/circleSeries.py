def setup():
    size(400, 400)
    no_stroke()


def draw():
    background(55)
    for i in range(5):
        fill(random(255), random(255), random(255))
        ellipse(20 + i * 80, height / 2, (i + 1) * 18, (i + 1) * 18)
