class Count:
	def __init__(self,count=0):
		self.count = count # initializing out class count = 0
def main():
	c = Count() #assigning c to variable class,
	n = 1 # asssing value 1 to n for calling function m
	m(c,n) #assininig count class and 1 to m function

	print("count is",c.count) #what is count? 5
	print("n is", n) # n should be 3

def m(c,n):
	c = Count(5)
	#print("inside m function c is :",c)
	n = 3
	#print("inside m function n is : ", n)
main()