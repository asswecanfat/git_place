from PIL import Image

image = Image.open('C:\\Users\\10248\\Desktop\\textpit2.jpg')
image_L = image.convert('L')

asc = '@%#*+=-:. '
text = ''
zoom = 1
nem = 0.3
weight, height = image_L.size
out = image_L.resize((int(weight*zoom), int(height*zoom*nem)))
weight, heught = out.size
for row in range(int(height)):
    for line in range(int(weight)):
        gay = image_L.getpixel((line, row))
        text += asc[int(gay/255*9)]
    text += '\n'
with open('C:\\Users\\10248\\Desktop\\尼禄.txt', 'w') as f:
    f.write(text)
