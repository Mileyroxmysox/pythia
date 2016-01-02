Embed CPython Script
-------------

To run in OSv
```
cd pythia/examples
pythia cpython_embed.md --osv
```

The script below is marked with `@embed` which turns it into a static string in the final C++,
and is run after `cpython.initalize()` is called.


@/myfolder/somefile.json
```
my-data
```

@embed
```python

class A():
	def __init__(self):
		self.value = 100
	def pymethod(self):
		print 'from cpython: self.value=', self.value
		if hasattr(self, 'my_dynamic_var'):
			print self.my_dynamic_var

	def add(self, a,b):
		return a+b

def foo():
	print 'foo'
	print open('myfolder/somefile.json', 'r').read()
	return A()

```

OSv image manifest
------------------
Below is the minimal set of files required to run Python.

@usr.manifest
```
/usr/lib/python2.7/site.py: /usr/lib/python2.7/site.py
/usr/lib/python2.7/os.py: /usr/lib/python2.7/os.py
/usr/lib/python2.7/posixpath.py: /usr/lib/python2.7/posixpath.py
/usr/lib/python2.7/stat.py: /usr/lib/python2.7/stat.py
/usr/lib/python2.7/genericpath.py: /usr/lib/python2.7/genericpath.py
/usr/lib/python2.7/warnings.py: /usr/lib/python2.7/warnings.py
/usr/lib/python2.7/linecache.py: /usr/lib/python2.7/linecache.py
/usr/lib/python2.7/types.py: /usr/lib/python2.7/types.py
/usr/lib/python2.7/UserDict.py: /usr/lib/python2.7/UserDict.py
/usr/lib/python2.7/_abcoll.py: /usr/lib/python2.7/_abcoll.py
/usr/lib/python2.7/abc.py: /usr/lib/python2.7/abc.py
/usr/lib/python2.7/_weakrefset.py: /usr/lib/python2.7/_weakrefset.py
/usr/lib/python2.7/copy_reg.py: /usr/lib/python2.7/copy_reg.py
/usr/lib/python2.7/traceback.py: /usr/lib/python2.7/traceback.py
/usr/lib/python2.7/sysconfig.py: /usr/lib/python2.7/sysconfig.py
/usr/lib/python2.7/re.py: /usr/lib/python2.7/re.py
/usr/lib/python2.7/sre_compile.py: /usr/lib/python2.7/sre_compile.py
/usr/lib/python2.7/sre_parse.py: /usr/lib/python2.7/sre_parse.py
/usr/lib/python2.7/sre_constants.py: /usr/lib/python2.7/sre_constants.py
/usr/lib/python2.7/_sysconfigdata.py: /usr/lib/python2.7/_sysconfigdata.py
/usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata_nd.py: /usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata_nd.py
```


CPython CAPI
------------
The code below shows how to use the `cpython` module that wraps around the CPython C-API.
https://docs.python.org/2/c-api/object.html

Below `a.value as int` it is trival to know that `a` is a PyObject and that using the `.` operator
on it makes Pythia generate the code that calls the CPython C-API.
Translation to C++:
```
auto v = static_cast<int>(PyInt_AS_LONG(PyObject_GetAttrString(a,"value")));
```

The syntax is used `->` to make it explicit that the object is a PyObject,
and to make Pythia generate the required CPython C-API calls.  
For example `b->pymethod()` becomes this C++:
```
PyObject_Call(
	PyObject_GetAttrString(b,"pymethod"),
	Py_BuildValue("()"),
	NULL
);
```




Build Options
-------------
* @link:python2.7
* @include:/usr/include/python2.7
```rusthon
#backend:c++
import cpython

def main():
	print readfile( open('myfolder/somefile.json','r'))
	print 'init cpython...'
	state = cpython.initalize()
	with gil:
		a = cpython.foo()
		print 'addr of a:', a
		print a..value as int
		a..pymethod()

		b = a
		b..pymethod()
		print b..value as int
		v = b..value as int
		print v + 400
		c = b..pymethod()

		r = b..add(1, 2) as int
		print r
		u = b..add(
			b..value, 
			b..value 
		) as int
		print u

		if hasattr(b, "value"):
			print('builtin `hasattr` works on b')
			print str(b)
			b..value = 'set from c++' as pystring
			b..pymethod()
			b..my_dynamic_var = 'hello dynamic var' as pystring
			a..pymethod()
			setattr(a, 'my_dynamic_var', 'setattr OK' as pystring)
			a..pymethod()

			s = b..my_dynamic_var as string
			print s

		pyob = cpython.foo()
		b..my_dynamic_var = pyob
		b..pymethod()

	cpython.finalize(state)

```