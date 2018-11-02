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
	def test_5.5(self):
		"""input 5.5 yields 5.5, 5, and 15"""
		self.spawn("./typecast2 5.5").stdout("5.500000\n5\n15\n", "5.500000\n5\n15\n").exit(0)
