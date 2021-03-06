'''
C fixed size arrays decay to pointers in C++.

'''
with stack:
	class A:
		pass

	class Bar:
		def __init__(self, x:[2]int ):
			#self.x[:] = x  ## this works but is not required
			## the translator is able to detect in this case 
			## that this needs to be an array copy.
			self.x = x

	class Foo( Bar ):
		def __init__(self, x:[2]int, y:[4]A ):
			self.x = x
			self.y = y

	def test_normal_array( arr:[]int )->int:
		return len(arr)

	def test_pointer_decay( arr:[2]int )->int:
		let b : [2]int
		#b[...] = addr(arr[0])  ## error: invalid conversion from ‘int*’ to ‘int’
		#b[...] = arr[0]  ## compiles but fails asserts below

		## explicit copy
		#b[:] = arr
		## in this simple case, the translator knows that `b` is a fixed size array,
		## and that it needs to copy all items from `arr`
		b = arr

		assert b[0]==arr[0]
		assert b[1]==arr[1]
		return len(arr)

	def stack_test():
		let alist : [4]A
		let i4 : [4]int
		i4[0]=1
		i4[1]=2

		i2 = [2]int(10,20)
		assert i2[0]==10
		assert i2[1]==20

		## pointer assignment only catches the first item
		i2[...] = i4[0]
		assert i2[0]==i4[0]
		#assert i2[1]==i4[1]  ## this will fail

		## explicit copy ok
		i2[:] = i4
		assert i2[0]==i4[0]
		assert i2[1]==i4[1]

		test_pointer_decay(i2) == len(i2)

		a = Bar(i2)
		arr = [2]int(6,7)
		b = Bar(arr)
		## test fixed size array assignment from object to object
		assert a.x[0]==i2[0]
		assert a.x[1]==i2[1]
		## direct assignment not allowed
		#a.x = b.x  # error: invalid array assignment
		#a.x[:] = b.x  ## error unknown array fixed size
		a.x[:2] = b.x  ## workaround: slice assignment with upper bound
		assert a.x[0]==b.x[0]
		assert a.x[1]==b.x[1]

def main():
	stack_test()
