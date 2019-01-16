from HW7_3 import Account

def main():
	account_id = 122
	balance = 20000
	annual_interest_rate = 4.5
	acc1 = Account(account_id,balance,annual_interest_rate)
	w = acc1.withdraw(2500)
	d = acc1.deposit()
	print("account_id is", acc1.getId())
	print("current Balance is after withdraw ", acc1.getBalance() - w)
	print("current valance affter deposit is" ,acc1.getBalance() + d)
	print("monthly InterestRate is ",acc1.getMonthlyInterestRate())
	print("monthly interest is ",acc1.getMonthlyInterest())
main()
