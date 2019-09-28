import os
import re


def wildcard_deal(file: str) -> list:
    if os.path.exists(file):
        if os.path.isfile(file):
            return [file]
        else:
            return []
    if '*' in file:
        file_name = os.path.basename(file)
        file_path = os.path.dirname(file)
        if '.' in file_name:
            deal = file_name.replace('.', '\.')
            p = re.compile('{}{}'.format(deal.replace('*', '\w+'), '$'))
            return [os.path.join(file_path, i) for i in os.listdir(file_path) if re.match(p, i)]
            # 应用列表推导式返回符合条件的文件
        else:
            return []
    elif '?' in file:
        file_name = os.path.basename(file)
        file_path = os.path.dirname(file)
        if '?' in file_name:
            deal = file_name.replace('.', '\.')
            p = re.compile('{}{}'.format(deal.replace('?', '\w'), '$'))
            return [os.path.join(file_path, i) for i in os.listdir(file_path) if re.match(p, i)]
        else:
            return []
    return []


if __name__ == '__main__':
    print(wildcard_deal(r'C:\Users\10248\Desktop\ass\算法\*.py'))
