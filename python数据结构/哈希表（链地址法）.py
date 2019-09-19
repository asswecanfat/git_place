import random

def h(n, num): #哈希函数
    return n % num

class Node(object):
    def __init__(self, elem, _next):
        self.elem = elem
        self._next = _next

class Hash_b(object):
    def init_hash(self, room, count = 0):
        self.room = room
        self.count = count
        self.hash = [Node(None, None) for i in range(self.room)]

    def insert_elem(self, elem, hash):
        ie = 0
        ensure_num = hash.search_hash(elem)
        if ensure_num != 1:
            elem_pos = h(elem, self.room - 1)
            if self.hash[elem_pos]._next == None:
                self.hash[elem_pos]._next = Node(elem, None)
            else:
                self.hash[elem_pos]._next = Node(elem, self.hash[elem_pos]._next)
            self.count += 1
            ie = 1
        return ie

    def destory_hash(self):
        del self.hash

    def search_hash(self, elem):
        elem_pos = h(elem, self.room - 1)
        a = self.hash[elem_pos]
        search_ensure = 0
        while a != None:
            if a.elem == elem:
                search_ensure = 1
            a = a._next
        return search_ensure

    def delete_hash(self, elem, hash):
        ensure_num = hash.search_hash(elem)
        dh = 0
        if ensure_num == 1:
            elem_pos = h(elem, self.room - 1)
            a = self.hash[elem_pos]
            while a._next != None:
                if a._next.elem == elem:
                    bo, a._next = a._next, a._next._next
                    dh = 1
                    self.count -= 1
                    break
                a = a._next
        return dh
    def elem_count(self):
        return self.count

    def print_hash(self):
        num_i = 0
        for i in self.hash:
            print('[' + str(num_i) + ']:', end = '')
            i = i._next
            while i != None:
                if i._next != None:
                    print(str(i.elem), end = '->')
                else:
                    print(str(i.elem), end = '')
                i = i._next
            print('\n')
            num_i += 1

print('··········哈希表（链地址法）测试··········')
print('1.初始化哈希表')
print('2.销毁哈希表')
print('3.查找')
print('4.插入')
print('5.删除')
print('6.打印哈希表')
print('7.获取哈希表元素个数')
print('8.随机测试数据')
print('9.退出')
init_sure = 0
while 1:
    choose = int(input('请输入操作：'))
    if choose == 1:
        room = int(input('请输入空间：'))
        hash = Hash_b()
        hash.init_hash(room)
        init_sure = 1
        print('哈希表初始化成功··')
    elif choose == 2:
        if init_sure:
            hash.destory_hash()
            init_sure = 0
            print('哈希表销毁成功··')
        else:
            print('哈希表未创建··')
    elif choose == 3:
        if init_sure:
            search_elem = int(input('请输入元素进行查找：'))
            if hash.search_hash(search_elem):
                print(str(search_elem) + ' 存在于该哈希表中··')
            else:
                print(str(search_elem) + ' 不存在于该哈希表中··')
        else:
            print('哈希表未创建··')
    elif choose == 4:
        if init_sure:
            insert_elem = int(input('请输入元素进行插入：'))
            if hash.insert_elem(insert_elem, hash):
                print(str(insert_elem) + ' 插入成功··')
            else:
                print(str(insert_elem) + ' 已存在··')
        else:
            print('哈希表未创建··')
    elif choose == 5:
        if init_sure:
            delete_elem = int(input('请输入元素进行删除：'))
            if hash.delete_hash(delete_elem, hash):
                print(str(delete_elem) + '已删除··')
            else:
                print(str(delete_elem) + '不存在于该哈希表中··')
        else:
            print('哈希表未创建··')
    elif choose == 6:
        hash.print_hash()
    elif choose == 7:
        print('该哈希表共有%d 个元素··' % hash.elem_count())
    elif choose == 8:
        if init_sure:
            elem_num = int(input('请输入n（n代表元素个数）:'))
            for i in range(elem_num):
                hash.insert_elem(random.randint(0,100),hash)
            print('随机数据插入成功··')
        else:
            print('哈希表未创建··')
    else:
        print('已退出··')
        break