class Account:
	def __init__(self, id1=0,balance =100,annualInterestRate=0):
		self.__id1 = id1
		self.__balance = balance
		self.__annualInterestRate = annualInterestRate
	def getId(self):
		return self.__id1
	def getBalance(self):
		return self.__balance
	def getAnnualInterestRate(self):
		return self.__annualInterestRate
	def getMonthlyInterestRate(self):
		return self.__annualInterestRate / 12 
	def getMonthlyInterest(self):
		return self.__balance * self.getMonthlyInterestRate()
	def setId(self,id1):
		self.__id1 = id1
	def setBalance(self,balance):
		self.__balance = balance
	def setAnnualInterestRate(self,annualInterestRate):
		self.__annualInterestRate = annualInterestRate
	def withdraw(self):
		withdraw_amount = eval(input("Enter an amount of money to withdraw: "))
		return self.__balance - withdraw_amount
	def deposit(self):
		deposit_amount = eval(input("enter an amount of money to deposit: "))
		return self.__balance + deposit_amount

