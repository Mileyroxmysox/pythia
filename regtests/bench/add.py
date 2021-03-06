'''
loop and add (integer)
'''
from time import clock

class A:
	def __init__(self, x,y,z):
		self.x = x; self.y = y; self.z = z

	def add(self, other):
		return A(self.x+other.x, self.y+other.y, self.z+other.z)

	def iadd(self, other):
		self.x += other.x
		self.y += other.y
		self.z += other.z

class M:

	def f2(self, step, a, b, c, x,y,z):
		s = A(0,0,0)
		for j in range(step):
			u = A(x,y,z)
			w = a.add(u).add(b).add(c)
			s.iadd(w)
		return s

	def f1(self, x, y, a, b, c ):
		w = A(0,0,0)
		flip = False
		for i in range(x):
			if flip:
				flip = False
				w.iadd(self.f2(y, a,b,c, 1,2,3))
			else:
				flip = True
				w.iadd(self.f2(y, a,b,c, 4,5,6))
		return w

def main():
	m = M()
	xsteps = 1000
	ysteps = 500
	start = clock()
	n = -1000000
	a = A(n,n+1,n)
	b = A(n,n+2,n)
	c = A(n,n+3,n)
	w = m.f1(xsteps, ysteps, a,b,c)
	print(clock()-start)
	print(w)  ## go will not allow unused variables

main()