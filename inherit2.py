class A(list):
	def __sub__(self,other):
        m = len(self)
		n = len(other)
		list3=[]
		for i in range(m):
			for j in range(n):
				if self[i] - other[j] != 0:
					list3.append(self[i])
		return list3
