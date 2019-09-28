import os
import re
import chardet


def deal_directory(file_path: str, func, base_func, expand_func):
    new_file_path = file_path
    if '*' in file_path:
        file_name = os.path.basename(file_path)
        new_file_path = os.path.dirname(file_path)
        deal = file_name.replace('.', '\.')
        p = re.compile('{}{}'.format(deal.replace('*', '.+'), '$'))
    elif '?' in file_path:
        file_name = os.path.basename(file_path)
        new_file_path = os.path.dirname(file_path)
        deal = file_name.replace('.', '\.')
        p = re.compile('{}{}'.format(deal.replace('?', '.'), '$'))
    else:
        p = re.compile(r'.+')
    if os.path.exists(new_file_path):
        all_file(new_file_path, func, p, base_func, expand_func)
    else:
        print('不存在该目录！！')


def all_file(base_path: str, func, p, base_func, expand_func):
    file = os.listdir(base_path)
    for item in file:  # 循环目录下的每一个元素（目录或文件）
        path = os.path.join(base_path,item)  # 路径拼接：要查询目录 + 第一级目录/文件
        if os.path.isfile(path) and not re.match(r'.+\.mp4|.+\.png|.+\.jpg',item):  # 判断：若果为文件且符合标准，直接运行对应方法
            if re.match(p, item) :
                dataDict = func(path)
                if func == base_func.l_func:
                    print('%s文件共有%d行' % (os.path.basename(path), dataDict[os.path.basename(path)]))
                elif func == base_func.w_func:
                    print('%s文件共有%d个单词' % (os.path.basename(path), dataDict[os.path.basename(path)]))
                elif func == base_func.c_func:
                    print('%s文件共有%d个字符' % (os.path.basename(path), dataDict[os.path.basename(path)]))  # [0-9a-zA-Z ]
                elif func == expand_func.a_func:
                    print('%s:' % os.path.basename(path))
                    print('共有%d行空行' % dataDict[os.path.basename(path)][0])
                    print('共有%d行注释行' % dataDict[os.path.basename(path)][1])
                    print('共有%d行代码行' % dataDict[os.path.basename(path)][2])
        elif re.match(r'.+\.mp4|.+\.png|.+\.jpg',item):
            continue
        else:
            all_file(path, func, p, base_func, expand_func)  # 如果仍是是目录，递归调用当前函数


def test():
    from BaseFunc import BaseFunc
    from ExpandFunc import ExpandFunc
    base_func = BaseFunc()
    expand_func = ExpandFunc()
    file_path = r'C:\Users\10248\Desktop\ass\wc'
    deal_directory(file_path, base_func.l_func, base_func, expand_func)