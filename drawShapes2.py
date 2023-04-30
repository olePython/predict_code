x = 100
y = 100
r = 50
c = color(255, 0, 0)

def setup():
    size(400, 400)

def draw():
    background(255)
    draw_shape(x, y, r, c)

def draw_shape(x, y, r, c):
    stroke(c)
    fill(c)
    ellipse(x, y, r, r)

def mouse_pressed():
    global x, y, r, c
    x = mouse_x
    y = mouse_y
    r = int(random(20, 100))
    c = color(random(255), random(255), random(255))
