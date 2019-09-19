import os

image_path = 'C:\\Users\\10248\\Desktop\\sbz\\'
image_list = os.listdir(image_path)
print([image_path + i for i in image_list])
