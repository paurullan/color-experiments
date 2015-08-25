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
color_list_text = """
Blue #0074D9
Aqua #7FDBFF
TEAL #39CCCC
OLIVE #3D9970
GREEN #2ECC40
LIME #01FF70
YELLOW #FFDC00
ORANGE #FF851B
RED #FF4136
MAROON #85144b
FUCHSIA #F012BE
PURPLE #B10DC9
"""

def get_color():

    color_list = [c for c in color_list_text.split() if c.startswith("#")]
    infinite_color = itertools.cycle(color_list)
    first = Color(next(infinite_color))
    second = Color(next(infinite_color))
    steps = 16
    while True:
        first, second = second, Color(next(infinite_color))
        for c in first.range_to(second, steps):
            yield c

def draw():
    #SCREEN_COLOR = (background.red, background.green, background.blue)
    #screen.fill(SCREEN_COLOR)
    screen.fill(background.web_color)

get_color_call = get_color()

def update():
    global CURRENT_FRAME
    if not CURRENT_FRAME:
        new_color = next(get_color_call)
        background.web_color = new_color.get_web()
        CURRENT_FRAME = MAX_FRAMES
    else:
        CURRENT_FRAME -= 1
