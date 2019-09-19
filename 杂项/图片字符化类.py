from PIL import Image

class Imgchange():
    def __init__(self, img_name, zoom = 1, gum = 1):
        self.img_name = 'C:\\Users\\10248\\Desktop\\' + img_name
        self.zoom = zoom
        self.gum = gum

    def change(self):
        img = Image.open(self.img_name)
        out = img.convert('L')
        weight, height = out.size
        out = out.resize((int(weight*self.zoom),int(height*self.zoom*self.gum)))
        asc = '@%#*+=-:. '
        text = ''
        for row in range(int(height)):
            for line in range(int(weight)):
                gary = out.getpixel((line, row))
                text += asc[int(gary/255*9)]
            text += '\n'
        self.text = text

    def get_txt(self):
        with open('C:\\Users\\10248\\Desktop\\字符画.txt',  'w') as f:
            f.write(self.text)

if __name__ == '__main__':
    str = input('请输入图片名称：')
    a = Imgchange(str)
    a.change()
    a.get_txt()
    print('字符化成功！')


