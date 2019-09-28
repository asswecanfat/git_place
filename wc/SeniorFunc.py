import tkinter as tk
import os
from tkinter import filedialog
from BaseFunc import BaseFunc
from ExpandFunc import ExpandFunc


class WcUi:
    def __init__(self, root: tk, base_func: BaseFunc, expand_func: ExpandFunc):
        self.base_func = base_func
        self.expand_func = expand_func
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.the_lable = tk.Label(self.frame, text='Word Count小程序')
        self.the_lable.pack(side=tk.TOP)

        self.the_text = tk.Text(self.frame, width=40, height=20)
        self.the_text.config(state=tk.DISABLED)
        self.the_text.pack()

        self.the_button = tk.Button(self.frame, text='选取文件', width=15, height=2, command=self.__button_click)
        self.the_button.pack()

    def __button_click(self):
        func = [self.base_func.l_func, self.base_func.w_func,
                self.base_func.c_func, self.expand_func.a_func]
        self.the_text.config(state=tk.NORMAL)
        self.the_text.delete(1.0, "end")
        file_name = filedialog.askopenfilename()
        self.the_text.insert('end', '{}{}'.format(os.path.basename(file_name), '文件：\n'))
        for i in func:
            if i == self.base_func.l_func:
                file_data = i(file_name)
                if file_data:
                    self.the_text.insert('end', '{}{}{}'.format('共有',
                                                                file_data[os.path.basename(file_name)],
                                                                '行\n'))
                else:
                    self.the_text.insert('end', '文件不合法！！！')
                    break
            if i == self.base_func.w_func:
                file_data = i(file_name)
                self.the_text.insert('end', '{}{}{}'.format('共有',
                                                            file_data[os.path.basename(file_name)],
                                                            '个单词\n'))
            if i == self.base_func.c_func:
                file_data = i(file_name)
                self.the_text.insert('end', '{}{}{}'.format('共有',
                                                            file_data[os.path.basename(file_name)],
                                                            '个字符\n'))
            if i == self.expand_func.a_func:
                file_data = i(file_name)
                real_file = os.path.basename(file_name)
                self.the_text.insert('end', '{}{}{}'.format('共有',
                                                            file_data[real_file][0],
                                                            '行空行\n'))
                self.the_text.insert('end', '{}{}{}'.format('共有',
                                                            file_data[real_file][1],
                                                            '行注释行\n'))
                self.the_text.insert('end', '{}{}{}'.format('共有',
                                                            file_data[real_file][2],
                                                            '行代码行\n'))
        self.the_text.config(state=tk.DISABLED)


def run_ui():
    root = tk.Tk()
    base_func = BaseFunc()
    expand_func = ExpandFunc()
    root.title('WC小程序')
    WcUi(root, base_func, expand_func)
    root.mainloop()
