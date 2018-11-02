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
		"""input 2 + 3 - 1 yields 4.000000"""
		self.spawn("./calc2 2 + 3 - 1").stdout("4.000000\n", "4.000000\n").exit(0)

	@check("compiles")
	def test_244_plus_32_plus_49(self):
		"""input 2.44 + 3.2 + 4.9 yields 10.540001"""
		self.spawn("./calc2 2.44 + 3.2 + 4.9").stdout("10.540001\n", "10.540001\n").exit(0)

	@check("compiles")
	def test_2_plus_3_times_4(self):
		"""input 2 + 3 x 4 yields 14.000000"""
		self.spawn("./calc2 2 + 3 x 4").stdout("14.000000\n", "14.000000\n").exit(0)

	@check("compiles")
	def test_32_minus_5525_div_4(self):
		"""input 32 - 55.25 / 4 yields 18.187500"""
		self.spawn("./calc2 32 - 55.25 / 4").stdout("18.187500\n", "18.187500\n").exit(0)
