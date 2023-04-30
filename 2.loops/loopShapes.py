angle = 0
x = 0
y = 0

def setup():
    global angle
    size(400, 400)
    stroke(255, 0, 0)
    stroke_weight(5)
    angle = 0

def draw():
    global angle, x, y
    background(55)
    translate(width / 2, height / 2)
    for i in range(0, 500):
        x = cos(angle) * 100
        y = sin(angle) * 100
        angle += 1
        point(x, y)
    no_loop()
