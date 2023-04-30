def setup():
    size(400, 400)

def draw():
    background(255)
    draw_rect(50, 50, 100, 50, color(255, 0, 0))
    draw_rect(200, 200, 50, 100, color(0, 255, 0))


def draw_rect(x, y, w, h, color):
    fill(color)
    no_stroke()
    rect(x, y, w, h)