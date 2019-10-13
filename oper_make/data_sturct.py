class Node(object):
    def __init__(self, operator=None, num=None, right_child=None, left_child=None, answer=None, _min=None):
        self.operator = operator
        self.num = num
        self.right_child = right_child
        self.left_child = left_child
        self.answer = answer
        self._min = _min


class DataSave(object):
    mathop_dict = {
    }
