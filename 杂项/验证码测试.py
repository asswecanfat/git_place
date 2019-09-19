import tesserocr
from PIL import Image

image = Image.open('captcha.jpg')
image = image.convert('L')
image.show()
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
print(tesserocr.image_to_text(image))
