
# 9.2(Create an investment-value calculator) Write a program that calculates the future
# value of an investment
# at a given interest rate for a specified number of years. 
# formula for the calculation is as follows:
# futureValue = investmentAmount * (1 + monthlyInterestRate) years ** 12

from tkinter import *
class InvestmentCalc:
	def __init__(self):
		window = Tk()
		window.title("Investment Calculator")
		#window.pack()
		#Creating the labels for window
		Label(window,text="Annual Interest Rate").grid(row=1,column=1,sticky=W)
		window.mainloop()



InvestmentCalc()