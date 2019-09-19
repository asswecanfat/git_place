
class ANode(object):
    def __init__(self, tag, atom):
        self.tag = tag
        self.atom = atom
class GLNode(object):
    def __init__(self, tag, hp = None, tp = None):
        self.tag = tag
        self.hp = hp
        self.tp = tp

class Glist(object):
    def init_glist(self, glist):
        i = 1
        if len(glist) > 2:
            b = i
            count = 0
            if glist[i] == '(':
                while 1:
                    if glist[b] == '(':
                        count += 1
                    if glist[b] == ')':
                        count -= 1
                        if count == 0:
                            break
                    b += 1
            tou = glist[i:b + 1]
            wei = '(' + glist[b + 2:-1] + ')'
            if wei == '()':
                return GLNode('list', self.init_glist(tou), None)
            else:
                return GLNode('list',self.init_glist(tou),self.init_glist(wei))
            '''print(tou)
            print(wei)'''
        else:
            return ANode('Atom',glist)


glist = '((),(a),(b,(c,(d),e)))'
gl = Glist()
a = gl.init_glist(glist)
def get(a):
    if a.tag == 'Atom':
        print(a.atom)
        return a.atom
    else:
        if a.hp != None:
            return  get(a.hp)
        if a.tp != None:
            return  get(a.tp)
get(a)










