def main():
	a = A()
	a.print()
class A:
	def __init__(self,newS="Welcome"):
		self.__s = newS
	def print(self):
		print(self.__s)
main()