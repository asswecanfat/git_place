def triangles():
	n = 1
	while True:
		lis = []
		if n == 1:
			lis = [1 for x in range(n)]
			yield lis
		elif n == 2:
			lis = [1 for x in range(n)]
			n_lis = lis
			yield lis
		else:
			lis.append(1)
			for i in range(len(n_lis)):
				if not i == len(n_lis)-1:
					lis.append(n_lis[i]+n_lis[i+1])
			lis.append(1)
			n_lis = lis
			yield lis
		n += 1
n = 0
result = []
for t in triangles():
	print(t)
	result.append(t)
	n = n+1
	if n == 20:
		break