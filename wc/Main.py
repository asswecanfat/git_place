from BaseFunc import BaseFunc
from ExpandFunc import ExpandFunc
from directory_processing import deal_directory
from SeniorFunc import run_ui
import click
import os


@click.command()
@click.option('-c', nargs=1, type=str, help='参数应为文件+文件路径或通配符(若有-s可以为文件目录)')
@click.option('-l', nargs=1, type=str, help='参数应为文件+文件路径或通配符(若有-s可以为文件目录)')
@click.option('-w', nargs=1, type=str, help='参数应为文件+文件路径或通配符(若有-s可以为文件目录)')
@click.option('-a', nargs=1, type=str, help='返回更复杂的数据（代码行 / 空行 / 注释行），且参数应为文件+文件路径或通配符(若有-s则需要通配符)')
@click.option('-s', nargs=2, type=str, help='以递归的方式处理文件')
@click.option('-x', nargs=0, help='启用图形页面')
def run(**cmd):
    base_func = BaseFunc()
    expand_func = ExpandFunc()
    if cmd['c'] is not None:  # 返回文件 file.c 的字符数
        char_dict = base_func.c_func(cmd['c'])
        easy_show('c', char_dict)
    elif cmd['l'] is not None:  # 返回文件 file.c 的行数
        line_dict = base_func.l_func(cmd['l'])
        easy_show('l', line_dict)
    elif cmd['w'] is not None:  # 返回文件 file.c 的词的数目
        word_dict = base_func.w_func(cmd['w'])
        easy_show('w', word_dict)
    elif cmd['a'] is not None:  # 返回更复杂的数据（代码行 / 空行 / 注释行）。
        dict_list = expand_func.a_func(cmd['a'])
        easy_show('a', dict_list)
    elif len(cmd['s']) != 0:
        if cmd['s'][0] == '-s':
            click.echo('第二名令不可为自身')
        else:
            if not os.path.isfile(cmd['s'][1]):
                if cmd['s'][0] == '-c':
                    deal_directory(cmd['s'][1], base_func.c_func, base_func, expand_func)
                elif cmd['s'][0] == '-l':
                    deal_directory(cmd['s'][1], base_func.l_func, base_func, expand_func)
                elif cmd['s'][0] == '-w':
                    deal_directory(cmd['s'][1], base_func.w_func, base_func, expand_func)
                elif cmd['s'][0] == '-a':
                    deal_directory(cmd['s'][1], expand_func.a_func, base_func, expand_func)
                else:
                    click.echo('-s后的命令无效！！')
            else:
                click.echo('单个文件无需-s命令！！')
    else:
        run_ui()


def easy_show(func, data_dict):
    if func == 'c':
        if data_dict:
            for file_name, _num in data_dict.items():
                click.echo('%s文件共有%d个字符' % (file_name, _num))
        else:
            click.echo('无该文件')
    if func == 'l':
        if data_dict:
            for file_name, _num in data_dict.items():
                click.echo('%s文件共有%d行' % (file_name, _num))
        else:
            click.echo('无该文件')
    if func == 'w':
        if data_dict:
            for file_name, _num in data_dict.items():
                click.echo('%s文件共有%d个单词' % (file_name, _num))
        else:
            click.echo('无该文件')
    if func == 'a':
        if data_dict:
            for file_name, counter in data_dict.items():
                click.echo('%s文件:' % file_name)
                click.echo('共有空行%d行' % counter[0])
                click.echo('共有注释行%d行' % counter[1])
                click.echo('共有代码行%d行' % counter[2])
        else:
            click.echo('无该文件')




if __name__ == '__main__':
    run()
