class Money:
	def usua(self,man,kid):
		self.MOney = 100
		self.money = 50
		self.man = man
		self.kid = kid
		print('平日票价：成人为：%d,小孩为：%d,%d个成人+%d个小孩平日票价为：%d' % (self.MOney, self.money,man,kid,man*self.MOney+kid*self.money))
	def week(self):
		print('周末票价：成人为：%d,小孩为：%d,%d个成人+%d个小孩平日票价为：%d' % (self.MOney*1.2, self.money*1.2,self.man,self.kid,self.man*self.MOney*1.2+self.kid*self.money*1.2))
while 1:
        try:
            man = int(input('请输入成人人数：'))
            kid = int(input('请输入小孩人数：'))
            m = Money()
            m.usua(man,kid)
            m.week()
        except ValueError:
            print('输入错误！请重新尝试！')
        else:
                break
