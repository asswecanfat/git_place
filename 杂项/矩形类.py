class A:
    def jiao(self, jao1,jao2,jao3,jao4):
        self.jao1 = jao1
        self.jao2 = jao2
        self.jao3 = jao3
        self.jao4 = jao4
    def ju(self):
        if self.jao1 == self.jao2 == self.jao3 == self.jao4 == 90:
            print('是矩形~')
        else:
            print('不是矩形！')
jao1 = int(input('请输入角度：'))
jao2 = int(input('请输入角度：'))
jao3 = int(input('请输入角度：'))
jao4 = int(input('请输入角度：'))
a = A()
a.jiao(jao1,jao2,jao3,jao4)
a.ju()
