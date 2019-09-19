
class BiNode(object):
    def __init__(self,lchild,data,rchild):
        self.lchild = lchild
        self.data = data
        self.rchild = rchild

class BiTree(object):
    # 采用先序遍历
    i = 0
    def init_Bitree(self):
        return None

    def create_Bitree(self,BT,i = 0):
        ch = BT[BiTree.i]
        BiTree.i += 1
        if ch == '#':
            return self.init_Bitree()
        else:
            T = BiNode(None,ch,None)
            T.lchild = self.create_Bitree(BT,BiTree.i)
            T.rchild = self.create_Bitree(BT,BiTree.i)
        return T

    def remake_i(self):
        BiTree.i = 0

    def destory_BiTree(self,T):
        del T
        return 1

    def empty_BiTree(self,T):
        if T == None:
            return 1
        else:
            return 0

    def break_BiTree(self,T):
        LTree = T.lchild
        RTree = T.rchild
        T = BiNode(None, T.data, None)
        return T,LTree,RTree

    def replace_LTree(self,T,new_LTree):
        old_LTree = T.lchild
        self.remake_i()
        T.lchild = self.create_Bitree(new_LTree)
        self.remake_i()
        return old_LTree

    def replace_RTree(self,T,new_RTree):
        old_RTree = T.rchild
        self.remake_i()
        T.rchild = self.create_Bitree(new_RTree)
        self.remake_i()
        return old_RTree

    def print_BiTree(self,T):
        if T != None:
            print(T.data,end='')
            self.print_BiTree(T.lchild)
            self.print_BiTree(T.rchild)
        else:
            print('#',end='')

def get_tree_num(Tree_list):
    long = str(len(Tree_list))
    n_str = '请输入树的序号（共有' + long + '棵树）：'
    return int(input(n_str))


print('············二叉树（链表）测试·········')
print('1.初始化树')
print('2.创造树')
print('3.销毁树')
print('4.分解树')
print('5.替换子树')
print('6.树判空')
print('7.打印树')
print('8.退出')

Tree_list = []
while 1:
    choose = int(input('请输入操作：'))
    if choose == 1:
        Tree_list.append(BiTree().init_Bitree())
        print('空树已添加··')
    elif choose == 2:
        tree_str = input('请输入树（***##**##*#格式）：')
        a = BiTree().create_Bitree(tree_str)
        for i in Tree_list:
            if i == None:
                Tree_list[Tree_list.index(i)] = a
                break
        if not a in Tree_list:
            Tree_list.append(a)
        BiTree().remake_i()
        print('树构建完成···')
    elif choose == 3:
        tree_num = get_tree_num(Tree_list)
        if BiTree().destory_BiTree(Tree_list[tree_num-1]):
            Tree_list.remove(Tree_list[tree_num-1])
            print('删除成功·····')
    elif choose == 4:
        tree_num = get_tree_num(Tree_list)
        BiTree().print_BiTree(Tree_list[tree_num - 1])
        print('')
        T,LTree,RTree = BiTree().break_BiTree(Tree_list[tree_num-1])
        Tree_list.remove(Tree_list[tree_num-1])
        Tree_list.append(T)
        Tree_list.append(LTree)
        Tree_list.append(RTree)
        print('该树的根节点为：',end='')
        BiTree().print_BiTree(T)
        print('')
        print('该树的左子树为：',end='')
        BiTree().print_BiTree(LTree)
        print('')
        print('该树的右子树为：',end='')
        BiTree().print_BiTree(RTree)
        print('')
    elif choose == 5:
        tree_num = get_tree_num(Tree_list)
        ch = int(input('请输入1或0选择左右子树：'))
        new_tree = str(input('请输入新的子树：'))
        if ch == 1:
            BiTree().replace_LTree(Tree_list[tree_num-1],new_tree)
        else:
            BiTree().replace_RTree(Tree_list[tree_num-1],new_tree)
        BiTree().print_BiTree(Tree_list[tree_num-1])
        print('')
        print('替换完成··')
    elif choose == 6:
        tree_num = get_tree_num(Tree_list)
        if BiTree().empty_BiTree(Tree_list[tree_num-1]):
            print('该树为空··')
        else:
            print('该树不为空··')
    elif choose == 7:
        tree_num = get_tree_num(Tree_list)
        BiTree().print_BiTree(Tree_list[tree_num-1])
        print('')
    else:
        print('已退出··')
        break






