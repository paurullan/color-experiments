from colour import Color

colors = ['#D24D57', '#DB0A5B', '#663399', '#4183D7', '#87D37C', '#E87E04']
gradient_colors = []

def group(it, n):
    return zip(*[iter(it)]*n)
    
for color_a, color_b in group(colors, 2):
    ca = Color(color_a)
    gradient_colors.extend(list(ca.range_to(Color(color_b), 10)))
    
for gc in gradient_colors:
    print(gc)
