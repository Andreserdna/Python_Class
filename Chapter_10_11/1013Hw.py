# 10.13

# (Eliminate duplicates) Write a function that returns a new list by eliminating the
# duplicate values in the list. Use the following function header:
# def eliminateDuplicates(lst):
# Write a test program that reads in a list of integers, invokes the function, and dis-
# plays the result. Here is the sample run of the program:

def eliminateDuplicated(lst):

	lst1 = []
	for i in range(len(lst)):
		for items in lst:
			print(items)

def main():
	#creating the empty list to append the users numbers
	upn = [] 
	#prompting the user to provide the ten numbers
	NUMBER_OF_INT = 5
	print("enter ten numbers")
	for i in range(NUMBER_OF_INT):
		user_provided_numbers = eval(input(": "))
		#appending the numbers
		upn.append(user_provided_numbers)

	#calling the eliminateDup function to get rid of dupe numbers
	print("removing duplicte numbers")
	eliminateDuplicated(upn)


main()