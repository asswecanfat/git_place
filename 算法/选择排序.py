from attr import attrib, attrs
import random


@attrs
class ChooseSort(object):
    need_list = attrib(default=[i for i in range(0, 20)])

    def init_need_list(self):
        random.shuffle(self.need_list)

    def __find_smallest(self):
        target = self.need_list[0]
        smallest_index = 0
        for j in range(1, len(self.need_list)):
            if self.need_list[j] < target:
                target = self.need_list[j]
                smallest_index = j
        return smallest_index

    def start(self):
        print(self.need_list)
        new_list = []
        for i in range(len(self.need_list)):
            smallest_index = self.__find_smallest()
            new_list.append(self.need_list.pop(smallest_index))
        return new_list


if __name__ == '__main__':
    test = ChooseSort()
    test.init_need_list()
    print(test.start())
