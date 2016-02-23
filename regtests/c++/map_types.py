'''
std::map<KEY, VALUE>
'''
mymap = {
	'key1' : [1,2,3],
	'key2' : [4,5,6,7]
}

with stack:
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

def main():
	print mymap
	assert mymap['key1'][0]==1
	assert mymap['key2'][1]==5
	test_heap()
	test_stack()
	print 'OK'
	