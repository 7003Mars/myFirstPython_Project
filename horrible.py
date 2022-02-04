
# globals().update(name=input('name?'), PIL=__import__('PIL', fromlist=['Image', 'ImageDraw']))
# print(name, PIL.Image)
# from PIL import Image, ImageDraw
# name: str

# ImageDraw.Draw(im:=PIL.Image.new('1', (7*len(name), 10), 255)).text((0, 0), name)
# [('\n' if not i else '')+((' ' if im.getpixel((i, j)) else '*')) for j in range(im.size[1]) for i in range(im.size[0])]
def second():
    (globals().update(name=input('name?'),PIL=__import__('PIL', fromlist=['Image', 'ImageDraw'])) or (PIL.ImageDraw.Draw(im:=PIL.Image.new('1', (7*len(name), 10), 255)).text((0, 0), name) and 0))
    print(''.join([('\n' if not i else '')+((' ' if im.getpixel((i, j)) else '*')) for j in range(im.size[1]) for i in range(im.size[0])]),'\n', name)

#Merged
def final():
    print((globals().update(name=input('name?'),PIL=__import__('PIL', fromlist=['Image', 'ImageDraw'])) or (PIL.ImageDraw.Draw(im:=PIL.Image.new('1', (7*len(name), 10), 255)).text((0, 0), name) and 0) or 0),''.join([('\n' if not i else '')+((' ' if im.getpixel((i, j)) else '*')) for j in range(im.size[1]) for i in range(im.size[0])]),'\n', name)

final()