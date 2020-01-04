import cv2


class Pic2Sketch:
    def __init__(self, img, path):
        self.__img = img
        self.__path = path

    def to_sketch(self):
        img_rgb = cv2.imread(self.__img)  # 读入图片
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)  # 转成灰度图
        img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21),
                                    sigmaX=0, sigmaY=0)  # 模糊化
        img_edge = cv2.divide(img_gray, img_blur, scale=255)  # 原图与上面的模糊图像融合
        print(self.__path)
        cv2.imwrite(self.__path, img_edge)  # 保存图像

    def __repr__(self):
        return f'Pic2Sketch(img={self.__img!r}, path={self.__path!r})'


if __name__ == '__main__':
    file_name = input('请输入图片：')
    p = Pic2Sketch(file_name, r'.\1.jpg')
    p.to_sketch()
