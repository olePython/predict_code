import random

circle_params = {"x": 100, "y": 100, "r": 50, "c": color(255, 0, 0)}

def setup():
    size(400, 400)

def draw():
    background(255)
    draw_shape(circle_params["x"], circle_params["y"], circle_params["r"], circle_params["c"])

def draw_shape(x, y, r, c):
    stroke(c)
    fill(c)
    ellipse(x, y, r, r)

def update_circle_state():
    circle_params["x"] += random.uniform(-50, 50)
    circle_params["y"] += random.uniform(-50, 50)
    circle_params["r"] = int(random.uniform(20, 100))
    circle_params["c"] = color(
        random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)
    )

def mouse_pressed():
    update_circle_state()

