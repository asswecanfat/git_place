import click


@click.command()
@click.option('-n',
              nargs=1,
              type=int,
              help='使用 -n 参数控制生成题目的个数',)
@click.option('-r',
              nargs=1,
              type=int,
              help='使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围',)
@click.option('-e',
              nargs=1,
              type=str,
              help='对给定的题目文件和答案文件，'
                   '判定答案中的对错并进行数量统计，输入参数如下：'
                   'XXX -e <exercisefile>.txt -a <answerfile>.txt',)
@click.option('-a',
              nargs=1,
              type=str,)
def run(**kwargs):
    if kwargs['n'] is not None and kwargs['r'] is None:
        click.echo('-r指令必须执行，且必须要有一个参数！！')
    if not kwargs['e'] and kwargs['a']:
        click.echo('-e和-a指令后必须要有参数！！')

if __name__ == '__main__':
    run()
