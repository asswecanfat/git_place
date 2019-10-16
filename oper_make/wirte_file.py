import re
from num_creat import NumCreat
from duplicate_check import creat_tree, is_equal
import chardet


def deal_math_op(math_op, postfix, answer, data_save):  # 处理数学表达式以便于查重
    if answer in data_save:
        if not data_save[answer]:
            data_save[answer].append(creat_tree(postfix))
        else:
            new_tree = creat_tree(postfix)
            for i in data_save[answer]:
                if is_equal(i, new_tree):
                    return None
    else:
        data_save[answer] = []
        data_save[answer].append(creat_tree(postfix))
    return replace_math_op(math_op)


def replace_math_op(math_op):  # 处理数学表达式中的假分数
    faker_list = re.findall(r'\d+/\d+', math_op)
    for i in faker_list:
        math_op = math_op.replace(i, str(NumCreat.fake2real_2_show(i)))
    return math_op


def deal_answer(answer):  # 处理答案的假分数
    if '/' in answer:
        return NumCreat.fake2real_2_show(answer)
    return answer


def write_in_file(creat, data_save):  # 写入文件
    with open(r'./Exercises.txt', 'a', encoding='utf-8') as q:
        with open(r'./Answers.txt', 'a', encoding='utf-8') as a:
            for num, (math_op, answer) in enumerate(creat.creat_more(data_save)):
                answer = deal_answer(answer)
                q.write('{}.{} = {}'.format(num + 1,
                                            math_op,
                                            '\n', ))
                a.write('{}.{}{}'.format(num + 1,
                                         answer,
                                         '\n'))
                print('{}{}{}'.format('\r第', num + 1, '条题目已生成！！'), sep='', end='', flush=True)


def compare_2_file(f1, f2):  # f1是题目文件，f2是答案文件
    coding1 = _get_coding(f1)
    coding2 = _get_coding(f2)
    if coding1 is not None and coding2 is not None:
        with open(f1, 'r', encoding=coding1) as f1:
            with open(f2, 'r', encoding=coding2) as f2:
                with open(r'.\Grade.txt', 'w', encoding='utf-8') as g:
                    right_num = 0
                    right_answer = []
                    wrong_num = 0
                    wrong_answer = []
                    f1_dict = _deal_lsit(f1)
                    f2_dict = _deal_lsit(f2)
                    for i in f1_dict.keys():
                        if f1_dict[i] == f2_dict[i]:
                            right_num += 1
                            right_answer.append(i)
                        else:
                            if f1_dict[i] != '':
                                wrong_num += 1
                                wrong_answer.append(i)
                    g.write(f'Correct: {right_num} ({right_answer[0]}')
                    for i in right_answer[1:]:
                        g.write(f', {i}')
                    g.write('){}Wrong: {} ({}'.format('\n', wrong_num, wrong_answer[0]))
                    for i in wrong_answer[1:]:
                        g.write(f', {i}')
                    g.write('){}'.format('\n'))


def _deal_lsit(f) -> dict:
    f_list = list(map(lambda x: re.split(r'\.(.+= ?)?', x), f.readlines()))  # 用于分开题目序号和答案
    return {i[0]: i[2].rstrip('\n') for i in f_list}


def _get_coding(f):  # 处理文件的编码，以防报错
    text = open(f, 'rb').read()
    return chardet.detect(text)['encoding']
