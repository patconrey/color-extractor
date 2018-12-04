import math
import cairo


def draw(cr, width, height):
    cr.scale(width, height)
    cr.set_line_width(0.04)

    utf8 = "cairo"

    cr.select_font_face("Sans",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_NORMAL)

    cr.set_font_size(0.1)
    x_bearing, y_bearing, width, height, x_advance, y_advance = \
        cr.text_extents(utf8)
    x = 0.5 - (width / 2 + x_bearing)
    y = 0.5 - (height / 2 + y_bearing)

    cr.move_to(x, y)
    cr.set_source_rgb(0, 0, 0)
    cr.show_text(utf8)
    cr.fill_preserve()
    cr.fill()


WIDTH, HEIGHT = 1000, 750

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.rectangle(0, 0, 1, 1)
ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()
ctx.fill()

draw(ctx, 200, 200)

#colors = [{'r': 75, 'g': 111, 'b': 63}, {'r': 104, 'g': 93, 'b': 70}, {'r': 33, 'g': 51, 'b': 28}, {'r': 52, 'g': 45, 'b': 33}, {'r': 185, 'g': 159, 'b': 128}]
#index = 0.0
#for color in colors:
#    ctx.rectangle(0.2 * index, 0, (0.2 * index) + 0.2, 1)
#    ctx.set_source_rgb(color['r'] / 255, color['g'] / 255, color['b'] / 255)
#    ctx.fill_preserve()
#    ctx.fill()
#    index += 1.0

surface.write_to_png("example.png")