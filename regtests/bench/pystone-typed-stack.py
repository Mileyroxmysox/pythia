'''
static typed pystone
'''

from time import clock

TRUE = 1
FALSE = 0
IntGlob = 0
BoolGlob = FALSE
Char1Glob = '\0'
Char2Glob = '\0'
Ident1 = 1
Ident2 = 2 
Ident3 = 3
Ident4 = 4
Ident5 = 5

with stack:
	let PtrGlb     : Record = None
	let PtrGlbNext : Record = None

	def create_array1glob(n:int) -> []int:
		comp = []int( 0 for i in range(n) )
		return comp

	def create_array2glob(n:int) -> [][]int:
		comp = [][]int(
			create_array1glob(n) for i in range(n)
		)
		return comp

	Array1Glob = create_array1glob(51)
	Array2Glob = create_array2glob(51)


	class Record:

		def __init__(self, PtrComp:Record = None, Discr = 0, EnumComp = 0, IntComp = 0, StringComp = '\0'):
			self.PtrComp = PtrComp
			self.Discr = Discr
			self.EnumComp = EnumComp
			self.IntComp = IntComp
			self.StringComp = StringComp

		def copy(self) ->Record:
			r = Record(
				PtrComp=self.PtrComp,
				Discr=self.Discr, 
				EnumComp=self.EnumComp,
				IntComp=self.IntComp, 
				StringComp=self.StringComp
			)
			return r


	def Func1(CharPar1:string, CharPar2:string) ->int:
		CharLoc1 = CharPar1
		CharLoc2 = CharLoc1
		if CharLoc2 != CharPar2:
			return Ident1
		else:
			return Ident2

	def Func2(StrParI1:string, StrParI2:string) -> int:
		IntLoc = 1
		CharLoc = '\0'  ## c++ scope style
		while IntLoc <= 1:
			if Func1(StrParI1[IntLoc], StrParI2[IntLoc+1]) == Ident1:
				CharLoc = 'A'
				IntLoc = IntLoc + 1
		if CharLoc >= 'W' and CharLoc <= 'Z':
			IntLoc = 7
		if CharLoc == 'X':
			return TRUE
		else:
			if StrParI1 > StrParI2:
				IntLoc = IntLoc + 7
				return TRUE
			else:
				return FALSE

	def Func3(EnumParIn:int) ->int:
		EnumLoc = EnumParIn
		if EnumLoc == Ident3: return TRUE
		return FALSE

	def Proc2(IntParIO:int) ->int:
		IntLoc = IntParIO + 10
		EnumLoc = -1  ## c++ scope style
		while True:
			if Char1Glob == 'A':
				IntLoc = IntLoc - 1
				IntParIO = IntLoc - IntGlob
				EnumLoc = Ident1
			if EnumLoc == Ident1:
				break
		return IntParIO

	def Proc4():
		global Char2Glob
		BoolLoc = Char1Glob == 'A'
		BoolLoc = BoolLoc or BoolGlob
		Char2Glob = 'B'

	def Proc5():
		global Char1Glob
		global BoolGlob
		Char1Glob = 'A'
		BoolGlob = FALSE

	def Proc6(EnumParIn:int) ->int:
		EnumParOut = EnumParIn
		if not Func3(EnumParIn):
			EnumParOut = Ident4
		if EnumParIn == Ident1:
			EnumParOut = Ident1
		elif EnumParIn == Ident2:
			if IntGlob > 100:
				EnumParOut = Ident1
			else:
				EnumParOut = Ident4
		elif EnumParIn == Ident3:
			EnumParOut = Ident2
		elif EnumParIn == Ident4:
			pass
		elif EnumParIn == Ident5:
			EnumParOut = Ident3
		return EnumParOut

	def Proc7(IntParI1:int, IntParI2:int) ->int:
		IntLoc = IntParI1 + 2
		IntParOut = IntParI2 + IntLoc
		return IntParOut

	def Proc8(Array1Par:[]int, Array2Par:[][]int, IntParI1:int, IntParI2:int):
		global IntGlob
		print 'enter Proc8'
		IntLoc = IntParI1 + 5
		Array1Par[IntLoc] = IntParI2
		Array1Par[IntLoc+1] = Array1Par[IntLoc]
		Array1Par[IntLoc+30] = IntLoc
		for IntIndex in range(IntLoc, IntLoc+2):
			Array2Par[IntLoc][IntIndex] = IntLoc
		Array2Par[IntLoc][IntLoc-1] = Array2Par[IntLoc][IntLoc-1] + 1
		Array2Par[IntLoc+20][IntLoc] = Array1Par[IntLoc]
		IntGlob = 5
		print 'proc8 ok'

	def Proc3(PtrParOut:Record) ->Record:
		global IntGlob
		if PtrGlb is not None:
			PtrParOut = PtrGlb.PtrComp
			#PtrParOut = PtrGlb->PtrComp
		else:
			IntGlob = 100
		PtrGlb.IntComp = Proc7(10, IntGlob)
		return PtrParOut

	def Proc1(PtrParIn:Record ) ->Record:
		NextRecord = PtrGlb.copy()
		#NextRecord = PtrGlb->copy()

		PtrParIn.PtrComp[...] = NextRecord
		PtrParIn.IntComp = 5
		NextRecord.IntComp = PtrParIn.IntComp
		NextRecord.PtrComp = PtrParIn.PtrComp

		NextRecord.PtrComp[...] = Proc3(NextRecord.PtrComp[...])

		if NextRecord.Discr == Ident1:
			NextRecord.IntComp = 6
			NextRecord.EnumComp = Proc6(PtrParIn.EnumComp)
			NextRecord.PtrComp = PtrGlb.PtrComp
			NextRecord.IntComp = Proc7(NextRecord.IntComp, 10)
		else:
			PtrParIn = NextRecord.copy()
		NextRecord.PtrComp = None
		return PtrParIn

	def Proc0(loops:int):
		global IntGlob
		global BoolGlob
		global Char1Glob
		global Char2Glob
		global Array1Glob
		global Array2Glob
		global PtrGlb
		global PtrGlbNext
		print 'enter proc0'
		print 'setting PtrGlbNext...'
		# can not use addr(...) on Record error: taking address of temporary
		PtrGlbNext[...] =  Record( PtrComp=None, Discr=0, EnumComp=0, IntComp=0, StringComp='\0' )  ## segfaults here
		print 'this never prints'
		print 'PtrGlbNext set'

		PtrGlb[...] = Record(
			PtrComp=PtrGlbNext, 
			Discr=Ident1, 
			EnumComp=Ident3, 
			IntComp=40, 
			StringComp="DHRYSTONE PROGRAM, SOME STRING"
		)

		String1Loc = "DHRYSTONE PROGRAM, 1'ST STRING"
		print String1Loc

		Array2Glob[8][7] = 10
		#print Array2Glob

		## c++ has different variable scope rules that are safer (and better)
		## than regular Python, where IntLoc3 is created in while loop below `while IntLoc1 < IntLoc2:`
		## IntLoc3 then bleeds into the outer scope, this is bad, what if `IntLoc1 > IntLoc2` then IntLoc3 is what?
		IntLoc3 = -1  ## c++ scope hack
		for i in range(loops):
			print i
			Proc5()
			Proc4()
			IntLoc1 = 2
			IntLoc2 = 3
			String2Loc = "DHRYSTONE PROGRAM, 2'ND STRING"
			EnumLoc = Ident2
			BoolGlob = not Func2(String1Loc, String2Loc)
			while IntLoc1 < IntLoc2:
				IntLoc3 = 5 * IntLoc1 - IntLoc2
				IntLoc3 = Proc7(IntLoc1, IntLoc2)
				IntLoc1 = IntLoc1 + 1

			#Proc8(Array1Glob, Array2Glob, IntLoc1, IntLoc3)
			Proc8(
				addr(Array1Glob), 
				addr(Array2Glob), 
				IntLoc1, IntLoc3
			)


			#PtrGlb[...] = Proc1( *PtrGlb )  # C++ style works up to two stars
			PtrGlb[...] = Proc1( PtrGlb[...] )

			CharIndex = 'A'
			while CharIndex <= Char2Glob:
				if EnumLoc == Func1(CharIndex, 'C'):
					EnumLoc = Proc6(Ident1)
				CharIndex = chr(ord(CharIndex)+1)
			IntLoc3 = IntLoc2 * IntLoc1
			IntLoc2 = IntLoc3 / IntLoc1
			IntLoc2 = 7 * (IntLoc3 - IntLoc2) - IntLoc1
			IntLoc1 = Proc2(IntLoc1)


	def pystones(loops:int):
		starttime = clock()
		Proc0(loops)
		benchtime = clock() - starttime
		#print(benchtime)
		loopsPerBenchtime = ( double(loops) / benchtime)
		print(loopsPerBenchtime)
		#print("#Pystone(%s) time for %s passes = %s" % (__version__, LOOPS, benchtime))
		#print("#This machine benchmarks at pystones/second: %s" %stones)


def main():
	LOOPS = 100000
	pystones( LOOPS )
