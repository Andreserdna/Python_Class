# Account: class
# -id1 :int
# -balance: int
# -annualInterestRate:Float
# Account(id:int,balance:float,annualInterestRate:float)
# getId():int
# getBalance():float
# getAnnualInterestRate():float
# getMonthlyInterestRate(annualInterestRate:float)
# getMonthlyInterest(annualInterestRate:float)
# setId(id1:int)none
# setBalance(getBalance():none)
# setAnnualInterestRate(annualInterestRate(): none)
# withdraw():float
# deposit():float



class Account:
	def __init__(self, id1=0,balance =100.0,annualInterestRate=0.0):
		self.__id1 = id1
		self.__balance = balance
		self.__annualInterestRate = annualInterestRate
	def getId(self):
		return self.__id1
	def getBalance(self):
		return self.__balance
	def getAnnualInterestRate(self):
		return self.__annualInterestRate / 100
	def getMonthlyInterestRate(self):
		return (self.__annualInterestRate / 100) / 12
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
		return self.balance - withdraw_amount
	def deposit(self):
		deposit_amount = eval(input("enter an amount of money to deposit: "))
		return deposit_amount
