import random


class QuickSort(object):
    def __init__(self, need_sort_list=None):
        self.need_sort_list = need_sort_list
        if self.need_sort_list is None:
            self.need_sort_list = [i for i in range(10)]
            random.shuffle(self.need_sort_list)
        else:
            self.need_sort_list = need_sort_list

    def start(self, arr):
        if len(arr) < 2:
            return arr
        else:
            point = arr[0]  # 暂时使用第一个
            min_ = [i for i in arr[1:] if i < point]
            max_ = [j for j in arr[1:] if j >= point]
            return self.start(min_) + [point] + self.start(max_)


if __name__ == '__main__':
    qs = QuickSort()
    print(qs.need_sort_list)
    print(qs.start(qs.need_sort_list))
