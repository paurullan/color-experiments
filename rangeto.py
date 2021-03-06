import itertools
from colour import Color

MAX_FRAMES = 5
CURRENT_FRAME = MAX_FRAMES

WIDTH = 900
HEIGHT = 900

background = Actor("background")
background.web_color = "#00ff00"
background.red = 0
background.green = 0
background.blue = 0

# colrd.com/palette/22780/
# http://clrs.cc/
# http://colrd.com/gradient/22272/
color_list_text = """
Blue #0074D9
Aqua #7FDBFF
TEAL #39CCCC
YELLOW #FFDC00
ORANGE #FF851B
RED #FF4136
FUCHSIA #F012BE
PURPLE #B10DC9
MAROON #85144b
"""

def get_color():
    color_list = [c for c in color_list_text.split() if c.startswith("#")]
    infinite_color = itertools.cycle(color_list)
    second = Color(next(infinite_color))
    steps = 16
    while True:
        first, second = second, Color(next(infinite_color))
        for c in first.range_to(second, steps):
            yield c

def draw():
    screen.fill(background.web_color)

get_color_call = get_color()
def update():
    global CURRENT_FRAME
    if CURRENT_FRAME:
        CURRENT_FRAME -= 1
        return
    else:
        CURRENT_FRAME = MAX_FRAMES
    new_color = next(get_color_call)
    background.web_color = new_color.get_hex()
