def main():
	max = 0
	getMax(1,2,max)
	print(max)
	print('hh')
def getMax(value1,value2,max):
	if value1 > value2:
		max = value1
	else:
		max = value2
	print(value2)
	print(str(value1))
main()