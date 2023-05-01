#1
def setup():
    size(400, 400)

def draw():
    background(255)
    no_stroke()
    if mouse_x < width / 2:
        fill(255, 0, 0)
        rect(0, 0, width / 2, height)
    else:
        fill(0, 0, 255)
        rect(width / 2, 0, width / 2, height)

    stroke(5)
    # black lines
    stroke_weight(4)
    line(width / 2, 0, width / 2, height)


#2
def setup():
    size(400, 400)

def draw():
    background(50)
    no_stroke()
    fill(200, 0, 0)
    if mouse_y < height * 0.33:
        ellipse(200, 66, 100, 100)
    elif mouse_y < height * 0.67:
        ellipse(200, 200, 100, 100)
    else:
        ellipse(200, 333, 100, 100)


#3 Version 1
def setup():
    size(400, 400)
    background(255)
def draw():
    background(255)
    line(200, 0, 200, 400)
    line(0, 200, 400, 200)

    if mouse_x <= 200 and mouse_y <= 200:
        fill(255, 0, 0)
        rect(0, 0, 200, 200)
    elif mouse_x >= 200 and mouse_y >= 200:
        fill(0, 255, 0)
        rect(200, 200, 200, 200)
    elif mouse_x >= 200 and mouse_y <= 200:
        fill(0, 0, 255)
        rect(200, 0, 200, 200)
    elif mouse_x <= 200 and mouse_y >= 200:
        fill(0)
        rect(0, 200, 200, 200)

#3 Version 2
def setup():
    size(400, 400)
    background(255)

def draw():
    background(255)
    line(200, 0, 200, 400)
    line(0, 200, 400, 200)

    if mouse_x <= 200 and mouse_y <= 200:
        fill(255, 0, 0)
        rect(0, 0, 200, 200)

    if mouse_x >= 200 and mouse_y >= 200:
        fill(0, 255, 0)
        rect(200, 200, 200, 200)

    if mouse_x >= 200 and mouse_y <= 200:
        fill(0, 0, 255)
        rect(200, 0, 200, 200)

    if mouse_x <= 200 and mouse_y >= 200:
        fill(0)
        rect(0, 200, 200, 200)

