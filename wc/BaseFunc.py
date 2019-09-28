import re
import os
import chardet
from wildcard_deal import wildcard_deal

class BaseFunc(object):

    def c_func(self, file: str) -> dict:  # 返回文件 file.c 的字符数
        char_dict = {}
        file_list = wildcard_deal(file)
        if file_list:
            for i in file_list:
                text = open(i, 'rb').read()
                coding = chardet.detect(text)['encoding']
                if coding is None:  # 判断该文件是否为UTF-8编码，不是则跳过
                    with open(i, 'r', encoding='utf-8') as f:
                        char_num = len(re.findall(r'\S', f.read(), re.M))
                        file_name = os.path.basename(i)
                        char_dict[file_name] = char_num
                else:
                    with open(i, 'r', encoding=coding) as f:
                        char_num = len(re.findall(r'\S', f.read(), re.M))
                        file_name = os.path.basename(i)
                        char_dict[file_name] = char_num
        return char_dict

    def w_func(self, file: str) -> dict:  # 返回文件 file.c 的词的数目
        word_dict = {}
        file_list = wildcard_deal(file)
        if file_list:
            for i in file_list:
                text = open(i, 'rb').read()
                coding = chardet.detect(text)['encoding']
                if coding is None:  # 判断该文件是否为UTF-8编码，不是则跳过
                    with open(i, 'r', encoding='utf-8') as f:
                        word_num = len(re.findall(r'[a-zA-Z]+', f.read(), re.M))
                        file_name = os.path.basename(i)
                        word_dict[file_name] = word_num
                else:
                    with open(i, 'r', encoding=coding) as f:
                        word_num = len(re.findall(r'[a-zA-Z]+', f.read(), re.M))
                        file_name = os.path.basename(i)
                        word_dict[file_name] = word_num
        return word_dict

    def l_func(self, file: str) -> dict:  # 返回文件 file.c 的行数
        line_dict = {}
        file_list = wildcard_deal(file)
        if file_list:
            for i in file_list:
                text = open(i, 'rb').read()
                coding = chardet.detect(text)['encoding']
                if coding is None:  # 判断该文件是否为UTF-8编码，不是则跳过
                    with open(i, 'r', encoding='utf-8') as f:
                        line_num = len(f.readlines())
                        file_name = os.path.basename(i)
                        line_dict[file_name] = line_num
                else:
                    with open(i, 'r', encoding=coding) as f:
                        line_num = len(f.readlines())
                        file_name = os.path.basename(i)
                        line_dict[file_name] = line_num
        return line_dict


if __name__ == '__main__':
    pass
