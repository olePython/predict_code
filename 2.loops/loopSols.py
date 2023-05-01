def setup():
    size(500, 500)
    no_fill()
    stroke(0)
    stroke_weight(2)
    translate(10, 50)

    # ___1.
    for i in range(0, 3):
        rect(400 - i * 80, i * 80, 80, 80)

    # ____2.
    for i in range(0, 3):
        rect(i * 80, i * 80, 160, 160)

    # ____3.
    for i in range(0, 200, 40):
        line(0, i, i, 200)

        # ____4.
    for siz in range(20, 120, 20):
        ellipse(200, 200, siz, siz)

    # ____5.
    for i in range(50, 10, -10):
        rect(50 - i, 0, i, i)


   # ____6.
   for i in range(20, 400, 20):
       line(i, 0, 1.5 * i, 120)
       line(1.5 * i, 120, 1.2 * i, 240)

def draw():
    pass