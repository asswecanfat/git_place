from collections import namedtuple
import re


def check_text(s, c_dict):
    roo = list(re.sub(r'\d|', '', s))
    print(roo)
    c = re.findall(r'\(\d(.)\d\)', s)
    print(c)
    roo.sort(key=lambda x: (x == '+' or x == '-', x == '*' or x == '/'))
    for i in c:
        roo.insert(0, c)

    print(roo)
    '''group = s
    for i in roo:
        a = re.findall(c_dict[i], group)[0]
        group = re.sub(c_dict[i], str(eval(a)), group)
        print(a,group)'''


if __name__ == '__main__':
    NewTuple = namedtuple('NewTuple', ['data', 'ensure', 'next'])
    c_dict = {
        '+': r'\d\+\d?',
        '*': r'\d\*\d?',
        '/': r'\d/\d?',
        '-': r'\d-\d?'
    }
    s = '(1+2)+(4+3)'
    check_text(s, c_dict)
    #check_2(s)
