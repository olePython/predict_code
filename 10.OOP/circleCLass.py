import random

class Circle:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        
    def draw(self):
        stroke(self.c)
        fill(self.c)
        ellipse(self.x, self.y, self.r, self.r)
        
    def update(self):
        self.x += random.uniform(-50, 50)
        self.y += random.uniform(-50, 50)
        self.r = int(random.uniform(20, 100))
        self.c = color(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))

def setup():
    size(400, 400)
    global circl
    circl = Circle(100, 100, 50, color(255, 0, 0))

def draw():
    background(255)
    circl.draw()

def mouse_pressed():
    circl.update()
    redraw()
