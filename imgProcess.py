#! /usr/bin/env python3

from PIL import Image
from PIL import ImageFilter
import pytesseract

threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

imgry = Image.open('gry.png')
out = imgry.point(table, '1')
out = out.filter(ImageFilter.EDGE_ENHANCE_MORE)
out.show()
out.save('test2.png')

result = pytesseract.image_to_string(out)
print(result)
