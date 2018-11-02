from check50 import *

class typecast1(Checks):

	@check()
	def exists(self):
		"""typecast1.c exists"""
		self.require("typecast1.c")

	@check("exists")
	def compiles(self):
		"""typecast1.c compiles"""
		self.spawn("clang -o typecast1 typecast1.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_a(self):
		"""input a yields 97\na\nAdding 3 letters gives you d"""
		self.spawn("./typecast1 a").stdout("97\na\nAdding 3 letters gives you d\n", "97\na\nAdding 3 letters gives you d\n").exit(0)
