from time import time
from PIL.Image import Image as PImage
from PIL import ImageDraw, ImageFont
import time
from PIL import Image
ImageFont.ImageFont()
txt = 'Hello World'

im = Image.new('1', (7*len(txt), 10), 255)
ImageDraw.Draw(im).text((0, 0), txt)
out = [('\n' if i == 0 else '')+((' ' if im.getpixel((i, j)) else '*'))
       for j in range(im.size[1]) for i in range(im.size[0])]
print(im.size[0] * im.size[1], len(out))
im.show()
print(''.join(out))
# a = list(im.getpixel((x, y)) for y in range(im.size[1]) for x in range(im.size[0]))
# print(a)
#Start
