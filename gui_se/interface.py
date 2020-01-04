import PySimpleGUI as Pg
import time
import re
from pathlib import Path
from sketch import Pic2Sketch


def _path_check(path):
    p = Path(path)
    if p.exists():
        return p
    return False


def _file_check(file):
    f = Path(file)
    if f.exists():
        if f.match('*.jpg') or f.match('*.png'):
            return True
    return False


if __name__ == '__main__':
    # 窗口内的所有控件
    layout1 = [[Pg.Text('该应用可以将图片转换成素描图', text_color='blue')],
               [Pg.Text('文件名：'), Pg.InputText(), Pg.FilesBrowse('图片文件选择')],
               [Pg.Text('保存路径：'), Pg.InputText(), Pg.FolderBrowse('保存路径选择')],
               [Pg.Button('转换且保存', button_color=('red', 'white')),
                Pg.Button('退出', button_color=('red', 'white'))],
               ]

    # 生成窗口
    window1 = Pg.Window('素描画生成', layout1)
    # 消息处理和输入消息接收
    while True:
        event, values = window1.read()
        print(values)
        if event in (None, '退出'):
            break
        if event in ('转换且保存',):
            p = _path_check(values[1])
            if _file_check(values[0]) and p:
                t = re.sub(r'\..+', '', str(time.time()))
                save_path = f'{values[1]}/{t}.jpg'
                path = Pic2Sketch(values[0], save_path)
                path.to_sketch()
                Pg.Popup(f'转换成功！请于{values[1]}目录下查看！')
            else:
                Pg.Popup('文件名或保存路径都不能为空！！')

    window1.close()

