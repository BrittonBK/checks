from check50 import *

class typecast2(Checks):

	@check()
	def exists(self):
		"""typecast2.c exists"""
		self.require("typecast2.c")

	@check("exists")
	def compiles(self):
		"""typecast2.c compiles"""
		self.spawn("clang -o typecast2 typecast2.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_3(self):
		"""input 3 yields 3.000000, 3, and 13"""
		self.spawn("./typecast2 3").stdout("3.000000\n3\n13\n", "3.000000\n3\n13\n").exit(0)

	@check("compiles")
	def test_5_5(self):
		"""input 5.5 yields 5.5, 5, and 15"""
		self.spawn("./typecast2 5.5").stdout("5.500000\n5\n15\n", "5.500000\n5\n15\n").exit(0)

	@check("compiles")
	def test_12_55678(self):
		"""input 12.55678 yields 12.556780, 12, and 22"""
		self.spawn("./typecast2 12.55678").stdout("12.556780\n12\n22\n", "12.556780\n12\n22\n").exit(0)
