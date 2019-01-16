from Loan import Loan

def main():
	annualInterestRate = eval(input("enter yearly interest rate, for example, 5.86: "))

	numberOfYears = eval(input("enter number of years as an integer: "))

	loanAmount = eval(input("ENter loan amount 188999:"))

	borrower = input("enter borrower name: ")

	#create the load object

	loan = Loan(annualInterestRate,numberOfYears,loanAmount,borrower)

	#display the loan data, monthly payment, and total payment
	print("the loas is for",loan.getBorrower())
	print("the monthly payment is ", format(loan.getMonthlyPayment(),".2f"))
	print("the total payment is", format(loan.getTotalPayment()),".2f")
main()
