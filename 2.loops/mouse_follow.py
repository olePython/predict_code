import py5_tools

def setup():
    size(400, 400)
    
def draw():
    background(100)
    stroke(255)
    stroke_weight(4)
    line(mouse_x - 10, mouse_y, mouse_x - 25, mouse_y)
    line(mouse_x + 10, mouse_y, mouse_x + 25, mouse_y)
    line(mouse_x, mouse_y - 10, mouse_x, mouse_y - 25)
    line(mouse_x, mouse_y + 10, mouse_x, mouse_y + 25)
    
    text_size(30)
    text(str(mouse_x) + "      " + str(mouse_y), 40, 40)
    
    
py5_tools.animated_gif("technique.gif", 100, 0.05, 0.05)