import re
from num_creat import NumCreat
from duplicate_check import creat_tree, isEqual


def deal_math_op(math_op, postfix, answer, data_save):
    print(postfix)
    if answer in data_save:
        if not data_save[answer]:
            data_save[answer].append(creat_tree(postfix))
        else:
            new_tree = creat_tree(postfix)
            for i in data_save[answer]:
                if isEqual(i, new_tree):
                    return None
    else:
        data_save[answer] = []
        data_save[answer].append(creat_tree(postfix))
    return replace_math_op(math_op)


def replace_math_op(math_op):
    faker_list = re.findall(r'\d+/\d+', math_op)
    for i in faker_list:
        math_op = math_op.replace(i, str(NumCreat.fake2real_2_show(i)))
    return math_op


def deal_answer(answer):
    if '/' in answer:
        return NumCreat.fake2real_2_show(answer)
    return answer


def write_in_file(math_op, postfix, answer, data_save, num):
    math_op = deal_math_op(math_op, postfix, answer, data_save)
    answer = deal_answer(answer)
    with open(r'./Exercises.txt', 'a+', encoding='utf-8') as q:
        with open(r'./Answers.txt', 'a+', encoding='utf-8') as a:
            q.write('{}.{} = {}'.format(num,
                                        math_op,
                                        '\n',))
            a.write('{}.{}{}'.format(num,
                                     answer,
                                     '\n'))
    return True
