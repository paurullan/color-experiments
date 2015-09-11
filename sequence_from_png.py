from png import Reader

FILENAME = "target_gradent.png"
background = Actor("background")
background.web_color = "#000000"


with open(FILENAME, 'rb') as f:
    reader = Reader(file=f)
    file_data = reader.read()

    """
    (686,
     300,
     <map at 0x7f153a04aa20>,
     {'alpha': True,
      'size': (686, 300),
      'planes': 4,
      'interlace': 0,
      'bitdepth': 8,
      'greyscale': False,
      'background': (255, 255, 255)})
    """

    image_width, image_height = file_data[0], file_data[1]
    # take the three ranges (drop alpha) for the whole width
    #colors = [c[:3] for c in list(zip(*list(file_data[2])))[:image_width]]
    #colors = list(file_data[2])
    raw = list(file_data[2])[0]
    colors = list(zip(raw[::4], raw[1::4], raw[2::4]))

go_and_back_colors = colors + colors[::-1]

# pygame stuff
import itertools
from colour import Color

MAX_FRAMES = 1
CURRENT_FRAME = MAX_FRAMES

WIDTH = 2500
HEIGHT = 1400

def get_color():
    infinite_color = itertools.cycle(go_and_back_colors)
    while True:
        current_color = next(infinite_color)
        new_color = Color()
        new_color.set_rgb(map(lambda x: x/256, current_color))
        yield new_color.get_hex()


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
    background.web_color = next(get_color_call)
