import os
import re


class BaseFunc(object):
    """
    编码问题需解决
    """
    def c_func(self, file):  # 返回文件 file.c 的字符数
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                return len(re.findall(r'\S', f.read(), re.M)) # [0-9a-zA-Z ]
        else:
            return None

    def w_func(self, file):  # 返回文件 file.c 的词的数目
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                return len(re.findall(r'[a-zA-Z]+', f.read(), re.M))
        else:
            return None

    def l_func(self, file):  # 返回文件 file.c 的行数
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                return len(f.readlines())
        else:
            return None
