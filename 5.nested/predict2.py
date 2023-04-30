def setup():
    size(400, 400)
    no_stroke()
    rect_mode(CENTER)

def draw():
    background(55)
    translate(25, 25)
    for x in range(0, width + 1, 50):
        for y in range(0, height + 1, 50):
            fill(200, 50, 100)
            rect(x, y, 40, 40)
            fill(255, 200, 50)
            ellipse(x, y, 40, 40)

