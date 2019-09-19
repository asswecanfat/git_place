class A:
	num = 0
	def __init__(self):
		self.num = 1+A.num
		A.num += 1
		print('共产生了%d个对象~' % self.num)
	def __del__(self):
		self.num = A.num-1
		A.num -= 1
		print('共删除了%d个对象~' % self.num)
