def setup():
    size(400, 400)
    color_mode(HSB, 360, 100, 100)  # Set the color mode to HSB
    no_loop()
    stroke_weight(10)


def draw():
    background(55)
    num_lines = 10
    y = 50
    for row in range(1, num_lines + 1):
        x = (width - 50) - row * 20
        for s in range(1, num_lines - row + 1):
            x += 20
        for a in range(1, 2 * row):
            stroke(random(360), 100, 100)  # Set the stroke color to a random HSB value
            point(x, y)
            x += 20
        y += 20
