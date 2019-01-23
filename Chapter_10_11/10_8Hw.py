# 10.8 (Find the index of the smallest element) Write a function that returns the index of
# the smallest element in a list of integers. If the number of such elements is greater
# than 1, return the smallest index. Use the following header:

# def indexOfSmallestElement(lst):
# Write a test program that prompts the user to enter a list of numbers, invokes this
# function to return the index of the smallest element, and displays the index.

def indexOfSmallestElement(lst):
	mini = min(lst)
	where = lst.index(mini)
	print("smallest number in list is " + str(mini) + " and the index is "  + str(where))
def main():
	#empty list
	#user_answer = []
	user_anw = []
	number_of_number = eval(input("how many number will you include in your list: "))
	for i in range(number_of_number):
		answer = eval(input("enter a number: "))
		user_anw.append(answer)

	indexOfSmallestElement(user_anw)

main()