import random

class Stack(object):
    def __init__(self, room):
        self.room = room
        self.elem = [None for i in range(self.room)]
        self.top = 0
        self.size = 0

class Struct(object):

    def init_stack(self,room):#初始化
        self.room = room
        self.s = Stack(self.room)
        return 1

    def stackEmpty(self):
        if self.s.elem[0] != None:
            print('栈不为空··')
        else:
            print('栈为空··')

    def push_elem(self, e):
        if self.s.top < self.room:
            self.s.elem[self.s.top] = e
            self.s.top += 1
            self.s.size += 1
            print('添加成功··')
        else:
            print('栈已满，若仍需添加请扩充空间··')

    def pop_elem(self):
        if self.s.elem[0] != None:
            e, self.s.elem[self.s.top-1] = self.s.elem[self.s.top-1], None
            self.s.size -= 1
            self.s.top -= 1
            print('弹出的元素为：' + str(e))
            return e
        else:
            print('栈为空，无法弹出元素··')

    def clear_stack(self):
        if self.s.elem[0] != None:
            while self.s.top > 0:
                self.s.top -= 1
                self.s.elem[self.s.top] = None
                self.s.size -= 1
            print('已清空栈··')
        else:
            print('栈已为空，无需清理··')

    def destory_stack(self):
        del self.s
        self.s = 0
        print('已销毁栈')

    def get_top_elem(self):
        if self.s.elem[0] != None:
            e = self.s.elem[self.s.top-1]
            print('取得栈顶元素为' + str(e))
        else:
            print('栈为空，无法取得栈顶元素··')

    def get_elem_size(self):
        i = 0
        print('栈中共有元素%d个'% self.s.size)
        while i < self.s.size:
            if i != self.s.size - 1:
                print(self.s.elem[i], end=' ')
            else:
                print(self.s.elem[i])
            i += 1

    def plus_room(self,room):
        self.room = self.room + room
        self.s.elem += [None for i in range(room)]
        print('空间扩充成功··')

print('········顺序栈测试·········')
print('1.初始化顺序栈')
print('2.销毁顺序栈')
print('3.顺序栈判空')
print('4.清空顺序栈')
print('5.输入元素并压进顺序栈')
print('6.顺序栈栈顶元素出栈')
print('7.获得顺序栈栈顶元素')
print('8.获取元素个数并打印')
print('9.扩充空间')
print('10.退出')
ensure = 0
while 1:
    choose = int(input('请输入相应操作：'))
    if choose == 1:
        room = int(input('请输入顺序栈空间（为大于0的数）：'))
        s = Struct()
        ensure = s.init_stack(room)
        if ensure:
            print('初始化成功··')
    elif choose == 2:
        if ensure:
            s.destory_stack()
            ensure = 0
        else:
            print('顺序栈未建立,无法销毁··')
    elif choose == 3:
        if ensure:
            s.stackEmpty()
        else:
            print('顺序栈未建立··')
    elif choose == 4:
        if ensure:
            s.clear_stack()
        else:
            print('顺序栈未建立··')
    elif choose == 5:
        if ensure:
            in_elem = input('请输入元素：')
            s.push_elem(in_elem)
        else:
            print('顺序栈未建立··')
    elif choose == 6:
        if ensure:
            s.pop_elem()
        else:
            print('顺序栈未建立··')
    elif choose == 7:
        if ensure:
            s.get_top_elem()
        else:
            print('顺序栈未建立··')
    elif choose == 8:
        if ensure:
            s.get_elem_size()
        else:
            print('顺序栈未建立··')
    elif choose == 9:
        if ensure:
            up_room = int(input('请输入需要扩充数量：'))
            s.plus_room(up_room)
        else:
            print('顺序栈未建立··')
    else:
        print('已退出··')
        break