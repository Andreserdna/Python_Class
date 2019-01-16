class A:
	def __init__(self,i):
		self.__i = i
	def printS(self):
		print(self.__i)
def main():
	a = A(5)
	print(a.printS())
main()
