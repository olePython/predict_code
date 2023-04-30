currentColor = (255, 0, 0)  # initial color is red
#import ran

def setup():
    size(400, 400)

def draw():
    global currentColor
    background(55)
    fill(*currentColor)
    no_stroke()
    circle(width/2, height/2, 100)

def mouse_pressed():
    global currentColor
    # check if mouse is over the circle
    if dist(mouse_x, mouse_y, width/2, height/2) <= 50:
        currentColor = (random(255), random(255), random(255))

def mouse_released():
    pass  # do nothing when mouse is released

