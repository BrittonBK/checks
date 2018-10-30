from check50 import *

class calc2(Checks):

	@check()
	def exists(self):
		"""calc2.c exists"""
		self.require("calc2.c")

	@check("exists")
	def compiles(self):
		"""calc2.c compiles"""
		self.spawn("clang -o calc2 calc2.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_2_plus_3_minus_1(self):
		"""input 2 + 3 - 1 yields 4"""
		self.spawn("./calc2 2 + 3 - 1").stdout("4.000000\n", "4.000000\n").exit(0)

	@check("compiles")
	def test_2_plus_3_times_4(self):
		"""input 2 + 3 * 4 yields 14"""
		self.spawn("./calc2 2 + 3 x 4").stdout("14.000000\n", "14.000000\n").exit(0)
