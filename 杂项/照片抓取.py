import easygui as ey
import urllib.request as urr

#先让用户输入尺寸
list1 = ['宽:','高:']
a = ey.multenterbox(msg='请填写喵的尺寸', title='下载一只喵', fields=(list1))
#判断用户有没有输入
if a == None:
    a = [400,600]
#抓取图片
ur = 'http://placekitten.com/g/%d/%d' % (int(a[0]), int(a[1])) 
'''异常处理（一会）'''
respone = urr.urlopen(ur)
cat_img = respone.read()
#先选取位置
file_place = ey.diropenbox()
if file_place:
    file_name = '%s\cat_%d_%d.jpg' % (file_place, int(a[0]), int(a[1]))
else:
    file_name = 'cat_%d_%d.jpg' % (int(a[0]), int(a[1]))
with open(file_name, 'wb') as f:
    f.write(cat_img)



