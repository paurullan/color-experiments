WIDTH = 900
HEIGHT = 900

colors = Actor("colors")
colors.red = 0
colors.green = 0
colors.blue = 0

moix = Actor("moix")
moix.pos = 200, 200

# colrd.com/palette/22780/
# http://clrs.cc/
"""
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

# https://docs.python.org/3.4/library/colorsys.html
# colorsys.rgb_to_hls(r, g, b)
# colorsys.hls_to_rgb(h, s, v)

#def update_pattern(self):
#    pass


#colors.update_pattern = update_pattern

def draw():
    SCREEN_COLOR = (colors.red, colors.green, colors.blue)
    screen.fill(SCREEN_COLOR)

def update():
    colors.red = (colors.red + 1) % 255
