'''
std::map<KEY, VALUE>
'''
mymap = {
	'key1' : [1,2,3],
	'key2' : [4,5,6,7]
}

FOO = 1.1
tuplemap = {
	'A': ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0], FOO),
	'B': ([7.0, 8.0, 9.0], [0.0, 0.0, 0.0], FOO*2.2)
}

class MyClass:
	def mymethod(self):
		return 99
	def somefloat(self):
		return 1.1
	def somestring(self):
		return 'hi'

with stack:
	tuplemap_stack = {
		'A': ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0], FOO),
		'B': ([7.0, 8.0, 9.0], [0.0, 0.0, 0.0], FOO*2.2)
	}

	def test_stack():
		print 'stack test...'
		m1 = {
			'K1' : [0,1],
			'K2' : [2,3]
		}
		assert m1['K1'][0]==0
		assert m1['K1'][1]==1
		assert m1['K2'][0]==2
		assert m1['K2'][1]==3

		vecx = tuple.get( tuplemap_stack['A'], 0 )
		assert vecx[0]==1.0


def test_heap():
	print 'heap test...'
	m1 = {
		'K1' : [0,1],
		'K2' : [2,3]
	}
	assert m1['K1'][0]==0
	assert m1['K1'][1]==1
	assert m1['K2'][0]==2
	assert m1['K2'][1]==3

	with get as 'std::get<%s>(*%s)':
		vec = get(0, tuplemap['A'])
		assert vec[0]==1.0

	vecx = tuple.get( tuplemap['A'], 0 )
	assert vecx[0]==1.0

	print 'testing loop over map keys'
	for key in m1:
		print 'key:', key

	print 'testing loop over map keys and values'
	for (key,val) in m1:
		print 'key:', key
		print 'value:', val

	keys = dict.keys(m1)
	assert len(keys)==2
	for key in keys:
		print key

	assert 'K1' in keys
	assert 'invalid-key' not in keys

	values = dict.values(m1)
	assert len(values)==2

	## golang style maps ##
	mymap = map[string]int{
		'foo':10, 
		'bar':100 
	}
	assert mymap['foo']==10
	assert mymap['bar']==100

	obmap = map[string]MyClass{ 'xx': MyClass() }
	#obmap = map[string]MyClass{}
	#obmap['xx'] = MyClass()
	assert obmap['xx'].mymethod()==99
	print obmap['xx'].somefloat()
	print obmap['xx'].somestring()

def main():
	print mymap
	assert mymap['key1'][0]==1
	assert mymap['key2'][1]==5
	test_heap()
	test_stack()
	print 'OK'
	