
# 10.1 (Assign grades) Write a program that reads a list of scores and then assigns grades
# based on the following scheme:
# The grade is A if score is 7= best – 10.
# The grade is B if score is 7= best – 20.
# The grade is C if score is 7= best – 30.
# The grade is D if score is 7= best – 40.
# The grade is F otherwise.
# Here is a sample run:
	

	#where = lst.index(mini)


def readGrade(score,best):
	for numbers in score:
		if numbers >= best - 10:
			a = "A"
			print("student " + str(score.index(numbers)) + " score is " + str(numbers) + " and grade is " + a)
		elif numbers >= best - 20:
			b = "B"			
			print("student " + str(score.index(numbers)) + " score is " + str(numbers) + " and grade is " + b)
		elif numbers >= best - 30:
			c = "C"
			print("student " + str(score.index(numbers)) + " score is " + str(numbers) + " and grade is " + c)
		elif numbers >= best - 40:
			d = "D"
			print("student " + str(score.index(numbers)) + " score is " + str(numbers) + " and grade is " + d)
		else:
			f = "F"
			print("student " + str(score.index(numbers)) + " score is " + str(numbers) + " and grade is " + f)


def main():
	BEST = 100
	scores = eval(input("Enter scores: "))
	scores_list = []
	for s in scores:
		scores_list.append(s)
	readGrade(scores_list,BEST)
main()