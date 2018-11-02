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

	@check("compiles")
	def test_K(self):
		"""input K yields 75\na\nAdding 3 letters gives you N"""
		self.spawn("./typecast1 K").stdout("75\nK\nAdding 3 letters gives you N\n", "75\nK\nAdding 3 letters gives you N\n").exit(0)

	@check("compiles")
	def test_y(self):
		"""input y yields 121\ny\nAdding 3 letters gives you b"""
		self.spawn("./typecast1 y").stdout("121\ny\nAdding 3 letters gives you b\n", "121\ny\nAdding 3 letters gives you b\n").exit(0)

	@check("compiles")
	def test_X(self):
		"""input X yields 88\nX\nAdding 3 letters gives you A"""
		self.spawn("./typecast1 X").stdout("88\nX\nAdding 3 letters gives you A\n", "88\nX\nAdding 3 letters gives you A\n").exit(0)
