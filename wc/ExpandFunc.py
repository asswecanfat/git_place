import os
import re


class ExpandFunc(object):

    def a_func(self, file):
        blank_line_num = None
        comment_row_num = None
        code_line_num = None
        if os.path.exists(file):
            blank_line_num = self.__count_blank_line(file)
            comment_row_num = self.__count_comment_row(file)
            code_line_num = self.__count_code_line(file, blank_line_num, comment_row_num)
        return blank_line_num, comment_row_num, code_line_num

    """    
    目前只针对Python文件
    """
    def __count_blank_line(self, file):  # 本行全部是空格或格式控制字符，如果包括代码，则只有不超过一个可显示的字符，例如“{”。
        blank_line_num = 0
        with open(file, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                if i == '\n' or re.match(r'^\s*$', i):
                    blank_line_num += 1
        return blank_line_num

    def __count_comment_row(self, file):  # 本行不是代码行，并且本行包括注释。一个有趣的例子是有些程序员会在单字符后面加注释：
        comment_row_num = 0
        flag = False
        with open(file, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                if '#' in i and not flag:
                    comment_row_num += 1
                if '"""' in i:
                    flag = bool(1 - flag)
                if flag:
                    comment_row_num += 1
        return comment_row_num

    def __count_code_line(self, file, blank_line_num, comment_row_num):  # 本行包括多于一个字符的代码。即总行数-空白行-注释行
        with open(file, 'r', encoding='utf-8') as f:
            return len(f.readlines()) - blank_line_num - comment_row_num
