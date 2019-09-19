#少放一个元素判空
from builtins import print


class SqQueue(object):
    def __init__(self,front,rear,maxsize):
        self.elem = [None for i in range(maxsize)]
        self.front = front
        self.rear = rear
        self.maxsize = maxsize

class SqQ(object):
    def init_sqqueue(self,maxsize):
        front = rear = 0
        self.squeue = SqQueue(front,rear,maxsize)
        print('初始化成功··')

    def sq_isemputy(self):
        if self.squeue.front == self.squeue.rear:
            print('该循环队列为空··')
        else:
            print('该循环队列不为空··')

    def desqueue_sq(self):
        if self.squeue.front != self.squeue.rear:
            e, self.squeue.elem[self.squeue.front] = self.squeue.elem[self.squeue.front], None
            self.squeue.front = (self.squeue.front + 1) % self.squeue.maxsize
            print('队头元素 '+ str(e) +' 已出列··')
            return 1
        else:
            print('该循环队列为空,无法进行出队操作··')
            return 0

    def ensqueue_sq(self,elem):
        if self.squeue.front != (self.squeue.rear + 1) % self.squeue.maxsize:
            self.squeue.elem[self.squeue.rear] = elem
            self.squeue.rear = (self.squeue.rear + 1) % self.squeue.maxsize
            print(str(elem) + ' 元素已加入队尾,在 %d 位置··' % ((self.squeue.rear - 1 + self.squeue.maxsize)% self.squeue.maxsize))
        else:
            print('该循环队列已满,无法进行入队操作··')

    def destroy_squeue(self):
        del self.squeue
        print('销毁成功··')

    def clear_squeue(self, Sq):
        while 1:
            ensure_pop = Sq.desqueue_sq()
            if not ensure_pop:
                break

    def squeue_length(self):
        sq_length = (self.squeue.rear - self.squeue.front + self.squeue.maxsize) % self.squeue.maxsize
        print('该循环队列共有 %d 个元素' % sq_length)

    def getHead_sq(self):
        e = self.squeue.elem[self.squeue.front]
        print('队头元素为 '+ str(e) +'··')

    def prin_sq(self):
        print(self.squeue.elem)

print('·············循环队列测试············')
print('1.初始化循环队列')
print('2.循环队列判空')
print('3.输入元素到循环队列中')
print('4.将循环队列的队尾元素弹出')
print('5.销毁循环队列')
print('6.清空循环队列')
print('7.获取循环队列的队头元素')
print('8.打印循环队列')
print('9.获取队列长度')
print('10.退出')
init_ensure = 0
while 1:
    choose = int(input('请输入相应操作：'))
    if choose == 1:
        maxsize = int(input('请输入最大空间：'))
        sq = SqQ()
        sq.init_sqqueue(maxsize)
        init_ensure = 1
    elif choose == 2:
        if init_ensure:
            sq.sq_isemputy()
        else:
            print('该循环队列未创建··')
    elif choose == 3:
        if init_ensure:
            in_num = input('请输入元素：')
            sq.ensqueue_sq(in_num)
        else:
            print('该循环队列未创建··')
    elif choose == 4:
        if init_ensure:
            sq.desqueue_sq()
        else:
            print('该循环队列未创建··')
    elif choose == 5:
        if init_ensure:
            sq.destroy_squeue()
            init_ensure = 0
        else:
            print('该循环队列未创建,无法销毁··')
    elif choose == 6:
        if init_ensure:
            sq.clear_squeue(sq)
        else:
            print('该循环队列未创建··')
    elif choose == 7:
        if init_ensure:
            sq.getHead_sq()
        else:
            print('该循环队列未创建··')
    elif choose == 8:
        if init_ensure:
            sq.prin_sq()
        else:
            print('该循环队列未创建··')
    elif choose == 9:
        if init_ensure:
            sq.squeue_length()
        else:
            print('该循环队列未创建··')
    else:
        print('已退出··')
        break


