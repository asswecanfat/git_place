#顺序表实现
import random

class SqBitree(object):

    def __init__(self,T):#初始化二叉树
        self.tree = T

    def is_Desendant(self,u,v): #判断v结点是否是u结点的子孙
        if u and v in self.tree:
            u_index = self.tree.index(u)
            v_index = self.tree.index(v)
            if (v_index > u_index) and (u_index and v_index >= 1):
                while v_index > u_index:
                    v_index = v_index // 2
                    if v_index == u_index:
                        return 1
            else:
                return 0
        else:
            print('其中一结点不存在')

T = [str(random.randint(0,100)) for i in range(10)]
T.insert(0,None)
print(T[1:])
tree = SqBitree(T)
u = input('请输入结点：')
v = input('请输入结点：')
if tree.is_Desendant(u,v):
    print(str(v) + '是' + str(u) + '的子孙结点··')
else:
    print(str(v) + '不是' + str(u) + '的子孙结点··')



