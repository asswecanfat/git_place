import random

class New_node():
    def __init__(self, elem, _next):
        self.elem = elem
        self._next = _next

class Struct():
    def __init__(self):
        head_node = New_node(None, None)
        self.b = head_node

    def isemput(self):
        if self.b.elem ==  None:
            print('该单链表为空')
        else:
            print('该单链表不为空')

    def prin(self):
        c = self.b
        while c != None:
            print(c.elem)
            c = c._next

    def in_add_node(self,a):
        self.b._next = a

    def out_add_node(self, d):
        c = self.b
        while c._next != None:
            c = c._next
        c._next = d

    def del_final_node(self):
        c = self.b
        while c._next._next != None:
            c = c._next
        del_node = c._next
        c._next = None
        del del_node

    def del_order_num_node(self, n):
        num = 1
        c = self.b
        while num < n:
            c = c._next
            num += 1
        del_node = c._next
        c._next = c._next._next
        del del_node

    def elem_num(self):
        c = self.b
        e_num = 0
        while c._next != None:
            e_num += 1
            c = c._next
        return e_num

    def search_elem(self,s_elem):
        c = self.b
        elem_num = 0
        ensure = False
        while c != None:
            if c.elem == s_elem:
                ensure = True
                print('%d在该单链表中，位置在%d' % (s_elem, elem_num))
                break
            elem_num += 1
            c = c._next
        if not ensure:
            print('%d不存在于该单链表中' % (s_elem))




print('·········单链表测试·········')
print('1.创建单链表')
print('2.单链表判空')
print('3.随机加入n个元素（n为自己添加）')
print('4.打印其中元素')
print('5.随机加入一个元素')
print('6.删除最后一个元素')
print('7.删除第n个元素')
print('8.计算元素个数')
print('9.销毁单链表')
print('10.查找元素')
print('10.退出')
str = 0
while 1:
    choose = int(input('请输入操作：'))
    if choose == 1:
        str = Struct()
        print('创建成功··')
    elif choose == 2:
        if str == 0:
            print('未创建单链表··')
        else:
            str.isemput()
    elif choose == 3:
        if str == 0:
            print('未创建单链表··')
        else:
            n = int(input('请输入n的个数：'))
            a = New_node(random.randint(0, 1000), None)
            for i in range(n - 1):
                a = New_node(random.randint(0, 1000), a)
            str.in_add_node(a)
            print('元素导入完成···')
    elif choose == 4:
        if str == 0:
            print('未创建单链表··')
        else:
            str.prin()
            print('打印完成··')
    elif choose == 5:
        if str == 0:
            print('未创建单链表··')
        else:
            one_num = New_node(random.randint(0,1000), None)
            str.out_add_node(one_num)
            print('加入完成··')
    elif choose == 6:
        if str == 0:
            print('未创建单链表··')
        else:
            if str.elem_num() == 0:
                print('该单链表已为空，请加入元素再进行删除··')
            else:
                str.del_final_node()
                print('删除成功··')
    elif choose == 7:
        if str == 0:
            print('未创建单链表··')
        else:
            order_num = int(input('请输入第n个数：'))
            elmit_num = str.elem_num()
            if order_num >= elmit_num or order_num <= 0:
                print('无法删除')
            else:
                str.del_order_num_node(order_num)
                print('删除成功··')
    elif choose == 8:
        print('该链表有%d个元素' % (str.elem_num()))
    elif choose == 9:
        if str == 0:
            print('未创建单链表··')
        else:
            del str
            print('销毁成功··')
            str = 0
    elif choose == 10:
        if str == 0:
            print('未创建单链表··')
        else:
            s_elem = int(input('请输入要查找的元素：'))
            str.search_elem(s_elem)
    else:
        print('已退出··')
        break