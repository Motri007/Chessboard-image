from PIL import Image
from itertools import chain


img = Image.new('RGB' , (256,256))

for y in chain(range(1,32), range(64,96), range(128,160), range(192,224)):
    for x in chain(range(1,32), range(64,96), range(128,160), range(192,224)):
        img.putpixel((x,y),(255,255,255))

for y in chain(range(32,64), range(96,128), range(160,192), range(224,256)):
    for x in chain(range(32,64), range(96,128), range(160,192), range(224,256)):
        img.putpixel((x, y), (255, 255, 255))


img.show()
