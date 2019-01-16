class A:
	def __init__(self,on):
		self.__on = on
	def getPropertyValue(self):
		return self.__on
	def getItem(self):
		print("inside get")
		print(self.__on)
def main():
	a = A(True)
	a.getPropertyValue()
	print(a.getItem())
main()
