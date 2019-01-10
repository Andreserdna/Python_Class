investmentAmount = eval(input("Enter investment amount e.g., 300000: "))
annualInterestRate = eval(input("Enter annual interest rate e.g., 3.8: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = annualInterestRate * 100 / 12
numberOfMonths = numberOfYears * 12

futureInvestmentAmount =  investmentAmount * (1 + monthlyInterestRate) **numberOfMonths

print("Accumalated value is", futureInvestmentAmount)
