from BaseFunc import BaseFunc
from ExpandFunc import ExpandFunc
import click
import re

@click.command()
@click.option('-c', nargs=1, type=str,help='参数应为文件+文件路径(若有-s则需要通配符)')
@click.option('-l', nargs=1, type=str,help='参数应为文件+文件路径(若有-s则需要通配符)')
@click.option('-w', nargs=1, type=str,help='参数应为文件+文件路径(若有-s则需要通配符)')
@click.option('-a', nargs=1, type=str, help='返回更复杂的数据（代码行 / 空行 / 注释行），且参数应为文件+文件路径(若有-s则需要通配符)')
@click.option('-s', nargs=3, type=str)
def run(**cmd):
    print(cmd)
    if cmd['c'] is not None:  # 返回文件 file.c 的字符数
        char_num = base_func.c_func(cmd['c'])
        if char_num is not None:
            click.echo('该文件总共有%d个字符！' % char_num)
        else:
            click.echo('未找到该文件')
    elif cmd['l'] is not  None:  # 返回文件 file.c 的词的数目
        line_num = base_func.l_func(cmd['l'])
        if line_num is not None:
            click.echo('该文件总共有%d行！' % line_num)
        else:
            click.echo('未找到该文件')
    elif cmd['w'] is not None:  # 返回文件 file.c 的行数
        word_num = base_func.w_func(cmd['w'])
        if word_num is not None:
            click.echo('该文件总共有%d个单词！' % word_num)
        else:
            click.echo('未找到该文件')
    elif cmd['a'] is not None:
        blank_line_num, comment_row_num, code_line_num = senior_func.a_func(cmd['a'])
        if blank_line_num is not None:
            click.echo('该文件有%d行空行' % blank_line_num)
            click.echo('该文件有%d行注释行' % comment_row_num)
            click.echo('该文件有%d行代码行' % code_line_num)
        else:
            click.echo('找不到该文件')
    elif len(cmd['s']) != 0:
        # TODO 未实现递归操作文件
        if cmd['s'][0] == '-s':
            click.echo('第二名令不可为自身')
        else:
            pass


if __name__ == '__main__':
    base_func = BaseFunc()
    senior_func = ExpandFunc()
    run()
