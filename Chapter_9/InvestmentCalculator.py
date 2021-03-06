from tkinter import *
import math


# 9.2(Create an investment-value calculator) Write a program that calculates the future
# value of an investment
# at a given interest rate for a specified number of years. 
# formula for the calculation is as follows:
# futureValue = investmentAmount * (1 + monthlyInterestRate) years ** 12




class InvestmentCalculator:
	def __init__(self):
		window = Tk()
		window.title("Investment Calculator")
		Label(window,text="Invesetment Amount").grid(row=1,column=1,sticky=W)
		Label(window,text="Interest Rate").grid(row=2,column=1,sticky=W)
		Label(window,text="Number of Years").grid(row=3,column=1,sticky=W)
		Label(window,text="Future Invesetment return").grid(row=4,column=1,sticky=W)
		
		self.annualInterestRateVar = DoubleVar() 
		Entry(window,textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
		self.numberOfYearsVar = IntVar()
		Entry(window,textvariable=self.numberOfYearsVar,justify=RIGHT).grid(row=2,column=2) 
		self.userInvestmentAmount = DoubleVar()
		Entry(window,textvariable=self.userInvestmentAmount,justify=RIGHT).grid(row=3,column=2)
		self.investmentReturn = DoubleVar()
		lblInvestmentReturn = Label(window,textvariable=self.investmentReturn).grid(row=4,column=2,sticky=E)
		#self.investmentReturn = StringVar()
		#lblTotalPaymentVar = Label(window,textvariable=self.totalPaymentVar).grid(row=5,column=2,sticky=E)
		btComputePayment = Button(window,text="Compute Future Invesetment",command=self.computePayment).grid(row=6,column=2,sticky=E)

		window.mainloop()

	def computePayment(self):

		futureInvestmentTotal = self.getFutureInvestment(float(self.userInvestmentAmount.get()),float(self.annualInterestRateVar.get()),float(self.numberOfYearsVar.get()))
		self.investmentReturn.set(format(futureInvestmentTotal,"10.2f"))


	def getFutureInvestment(self,investmentAmount,annualInterestRate,years):
		annualInterestRate = annualInterestRate / 12
		futureAmount = investmentAmount * math.pow((1 + annualInterestRate),years*12)
		return futureAmount

InvestmentCalculator()