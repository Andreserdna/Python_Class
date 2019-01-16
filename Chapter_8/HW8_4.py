
class checkString:
	def __init__(self,string = '', char = ''):
		self.string = string
		self.char = char
	def checkOccurances(self):
		count = 0
		for letter in self.string:
			if letter == self.char:
				count += 1
		return count
	def print_result(self):
		print("total count of " + self.char + " in " + self.string + " is " + str(self.checkOccurances()))
