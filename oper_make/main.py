import click
from math_op import Creat
from data_sturct import DataSave
from wirte_file import write_in_file, compare_2_file
from pathlib import Path


@click.command()
@click.option('-n',
              nargs=1,
              type=int,
              default=0,
              help='使用 -n 参数控制生成题目的个数',)
@click.option('-r',
              nargs=1,
              type=int,
              default=0,
              help='使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围',)
@click.option('-e',
              nargs=1,
              type=str,
              help='对给定的题目文件和答案文件，'
                   '判定答案中的对错并进行数量统计，输入参数如下：'
                   'XXX -e <exercisefile>.txt -a <answerfile>.txt',)
@click.option('-a',
              nargs=1,
              type=str,
              help='与e指令同时使用',)
def run(**kwargs):
    data_save = DataSave().mathop_dict
    if kwargs['r'] > 0 and kwargs['n'] > 0:
        _choices_method('r')(data_save, kwargs['r'], kwargs['n'])
    elif kwargs['r'] == 0 and kwargs['n'] > 0:
        _choices_method('r')(data_save=data_save, formula_num=kwargs['n'])
    elif kwargs['r'] > 0 and kwargs['n'] == 0:
        _choices_method('r')(data_save=data_save, max_num=kwargs['r'])
    elif kwargs['e'] and kwargs['a']:
        if Path(kwargs['e']).exists() and Path(kwargs['a']).exists():
            _e_a(kwargs['e'], kwargs['a'])
        else:
            click.echo('-e和-a指令的参数为文件且存在！！')
    else:
        click.echo('-r和-a指令后都需一个参数,且参数不能小于等于0,-e和-a指令后需同时使用，且都需一个参数！！')


def _choices_method(choice):  # 方法字典
    method_dict = {
        'r': _r_n,
        'e': _e_a,
    }
    return method_dict[choice]


def _r_n(data_save, max_num=10, formula_num=10):
    c = Creat(max_num, formula_num)
    write_in_file(c, data_save)


def _e_a(exercisefile, answerfile):
    compare_2_file(exercisefile, answerfile)


if __name__ == '__main__':
    run()