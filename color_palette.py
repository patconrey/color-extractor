import requests
import colorgram
import cairo
import boto3
import random
import string

N = 15
OUTPUT_FILENAME = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
INPUT_FILENAME = 'input.png'

def rgb2hex(r, g, b):
    hexadec = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hexadec


def drawLabel(cr, color, index, padding):

    cr.set_line_width(0.1)

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(0.02)

    cr.move_to(index * 0.2 + padding, 0.03)
    cr.set_source_rgba(1, 1, 1, 0.9)
    cr.show_text(color)
    cr.fill_preserve()


def drawPalette(WIDTH, HEIGHT, colors_rgb):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)

    index = 0.0

    for i in range(len(colors_rgb)):
        color_rgb = colors_rgb[i]
        ctx.rectangle(0.2 * index, 0, (0.2 * index) + 0.2, 1)
        ctx.set_source_rgb(color_rgb['r'] / 255, color_rgb['g'] / 255, color_rgb['b'] / 255)
        ctx.fill_preserve()
        ctx.fill()
        index += 1.0

    surface.write_to_png(OUTPUT_FILENAME + '.jpg')


colors = colorgram.extract(INPUT_FILENAME, 5)
colors_rgb = []
colors_hex = []

for color in colors:
        colors_rgb.append(
            {'r': color.rgb.r,
             'g': color.rgb.g,
             'b': color.rgb.b})
        colors_hex.append(rgb2hex(color.rgb.r, color.rgb.g, color.rgb.b))

drawPalette(1000, 750, colors_rgb)

s3 = boto3.resource('s3')
data = open(OUTPUT_FILENAME + '.jpg', 'rb')
s3.Bucket('color-palette-twitter-bot').put_object(Key=OUTPUT_FILENAME + '.jpg', Body=data, ACL='public-read')

c1 = colors_hex[0]
c2 = colors_hex[1]
c3 = colors_hex[2]
c4 = colors_hex[3]
c5 = colors_hex[4]
body = {'token': 'no',
        'username': 'patconrey',
        'c_1': c1,
        'c_2': c2,
        'c_3': c3,
        'c_4': c4,
        'c_5': c5,
        'url': 'https://s3.amazonaws.com/color-palette-twitter-bot/' + OUTPUT_FILENAME + '.jpg'}
url = "http://localhost:8000/new_palette"

r = requests.get(url, params=body)